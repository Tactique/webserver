from django.core.management.base import BaseCommand
from interface.models import (
    Team,
    Cell,
    WeaponType,
    Weapon,
    ArmorType,
    Armor,
    SpeedMap,
    Movement,
    Unit,
)

import os
import csv

class Command(BaseCommand):
    help = "Seed the database with all available data"

    def handle(self, *args, **options):
        try:
            self.resource_path = '%s/common/resources/' % (os.environ['DOMOROOT'],)
        except KeyError:
            print("Please define the $DOMOROOT environment variable to your domoco dir")
            return
        self.clearAllTables()
        self.seed_entries(Team, "Team", 'teams.csv')
        self.seed_entries(Cell, "Cell", 'terrain.csv', unique_name='cellType')
        weapon_types  = self.seed_entries(WeaponType, "WeaponType", 'weaponTypes.csv')
        weapons = self.seed_entries(Weapon, "Weapon", 'weapons.csv', reference_information={'weaponType': weapon_types})
        armor_types = self.seed_entries(ArmorType, "ArmorType", 'armorTypes.csv')
        armors = self.seed_entries(Armor, "Armor", 'armors.csv', reference_information={'armorType': armor_types})
        speed_maps = self.seed_entries(SpeedMap, "SpeedMap", 'speedMaps.csv')
        movements = self.seed_entries(Movement, "Movement", 'movements.csv', reference_information={'speedMap': speed_maps})
        self.seed_entries(Unit, "Unit", 'units.csv', reference_information={
            'attack_one': weapons,
            'attack_two': weapons,
            'armor': armors,
            'movement': movements})

    def clearAllTables(self):
        print("Clearing all Tables")
        def delete_me(x):
            print("deleting %s" % x)
            x.delete()

        map(delete_me, Team.objects.all())
        map(delete_me, Cell.objects.all())
        map(delete_me, WeaponType.objects.all())
        map(delete_me, Weapon.objects.all())
        map(delete_me, ArmorType.objects.all())
        map(delete_me, Armor.objects.all())
        map(delete_me, SpeedMap.objects.all())
        map(delete_me, Movement.objects.all())
        map(delete_me, Unit.objects.all())

    def seed_entries(self, constructor, model_name, csv_file, reference_information={}, unique_name='name'):
        dbEntries = {}
        with open(self.resource_path + csv_file, 'r') as file_:
            reader = csv.reader(file_, quotechar='\'')
            names = next(reader, None)
            for pieces in reader:
                index = names.index(unique_name)
                kwargs = dict(zip(names, pieces))
                for reference_name, reference_table in reference_information.items():
                    if reference_name in kwargs:
                        if kwargs[reference_name] != 'null':
                            kwargs[reference_name] = reference_table[kwargs[reference_name]]
                        else:
                            kwargs[reference_name] = None
                    else:
                        raise Exception("reference name %s was given, but is not in header of csv for %s" % (
                            reference_name, csv_file))
                print("Creating %s(%s)" % (
                    model_name, ', '.join(pieces)))
                dbEntry = constructor(**kwargs)
                dbEntry.save()
                dbEntries[pieces[index]] = dbEntry
        return dbEntries
