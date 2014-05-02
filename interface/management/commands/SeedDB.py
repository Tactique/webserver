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
            resources_path = '%s/common/resources/' % (os.environ['DOMOROOT'],)
        except KeyError:
            print("Please define the $DOMOROOT environment variable to your domoco dir")
            return
        self.clearCells()
        self.seed_teams(resources_path)
        self.seed_cells(resources_path)
        weapon_types = self.seed_weapon_types(resources_path)
        weapons = self.seed_weapons(resources_path, weapon_types)
        armor_types = self.seed_armor_types(resources_path)
        armors = self.seed_armors(resources_path, armor_types)
        speed_maps = self.seed_speed_maps(resources_path)
        movements = self.seed_movements(resources_path, speed_maps)
        self.seed_units(resources_path, weapons, armors, movements)

    def clearCells(self):
        print("Clearing the Cells")
        for cell in Cell.objects.all():
            cell.delete()

    def seed_teams(self, resources_path):
        with open(resources_path + 'teams.csv', 'r') as file_:
            reader = csv.reader(file_)
            next(reader, None)
            for nationType, color in reader:
                print("Creating Team(%s)" % (
                    ', '.join((nationType, color, color))))
                Team(nationType=nationType, spriteName=color, color=color).save()

    def seed_cells(self, resources_path):
        with open(resources_path + 'terrain.csv', 'r') as file_:
            reader = csv.reader(file_)
            next(reader, None)
            for cellType, spriteName in reader:
                print("Creating Cell(%s)" % (
                    ', '.join((cellType, spriteName))))
                Cell(spriteName=spriteName, cellType=cellType).save()

    def seed_weapon_types(self, resources_path):
        dbWeaponTypes = {}
        with open(resources_path + 'weaponTypes.csv', 'r') as file_:
            reader = csv.reader(file_)
            next(reader, None)
            for weaponType, name in reader:
                print("Creating WeaponType(%s)" % (
                    ', '.join((weaponType, name))))
                dbWeaponType = WeaponType(name=name, weaponType=weaponType)
                dbWeaponType.save()
                dbWeaponTypes[name] = dbWeaponType
        return dbWeaponTypes

    def seed_weapons(self, resources_path, weapon_types):
        dbWeapons = {}
        with open(resources_path + 'weapons.csv', 'r') as file_:
            reader = csv.reader(file_)
            next(reader, None)
            for name, weaponType, power, minRange, maxRange in reader:
                print("Creating WeaponType(%s)" % (
                    ', '.join((name, weaponType, power, minRange, maxRange))))
                weapon = Weapon(
                    name=name,
                    weaponType=weapon_types[weaponType],
                    power=power,
                    minRange=minRange,
                    maxRange=maxRange)
                weapon.save()
                dbWeapons[name] = weapon
        return dbWeapons

    def seed_speed_maps(self, resources_path):
        dbSpeedMaps = {}
        with open(resources_path + 'speedMaps.csv', 'r') as file_:
            reader = csv.reader(file_, quotechar='\'')
            next(reader, None)
            for name, jsonSpeeds in reader:
                print("Creating SpeedMap(%s)" % (
                    ', '.join((name, jsonSpeeds))))
                dbSpeedMap = SpeedMap(name=name, speeds=jsonSpeeds)
                dbSpeedMap.save()
                dbSpeedMaps[name] = dbSpeedMap
        return dbSpeedMaps

    def seed_movements(self, resources_path, speed_maps):
        dbMovements = {}
        with open(resources_path + 'movements.csv', 'r') as file_:
            reader = csv.reader(file_)
            next(reader, None)
            for name, distance, speedMap in reader:
                print("Creating Movement(%s)" % (
                    ', '.join((name, distance, speedMap))))
                movement = Movement(
                    name=name,
                    distance=distance,
                    speedMap=speed_maps[speedMap])
                movement.save()
                dbMovements[name] = movement
        return dbMovements

    def seed_armor_types(self, resources_path):
        dbArmorTypes = {}
        with open(resources_path + 'armorTypes.csv', 'r') as file_:
            reader = csv.reader(file_)
            next(reader, None)
            for armorType, name in reader:
                print("Creating ArmorType(%s)" % (
                    ', '.join((armorType, name))))
                dbArmorType = ArmorType(name=name, armorType=armorType)
                dbArmorType.save()
                dbArmorTypes[name] = dbArmorType
        return dbArmorTypes

    def seed_armors(self, resources_path, armor_types):
        dbArmors = {}
        with open(resources_path + 'armors.csv', 'r') as file_:
            reader = csv.reader(file_)
            next(reader, None)
            for name, strength, armorType in reader:
                print("Creating Armor(%s)" % (
                    ', '.join((name, armorType, strength))))
                armor = Armor(
                    name=name,
                    armorType=armor_types[armorType],
                    strength=strength)
                armor.save()
                dbArmors[name] = armor
        return dbArmors

    def seed_units(self, resources_path, weapons, armors, movements):
        with open(resources_path + 'units.csv', 'r') as file_:
            reader = csv.reader(file_)
            next(reader, None)
            for name, health, attack_one, attack_two, armor, movement in reader:
                print("Creating Unit(%s)" % (
                    ', '.join((name, health, attack_one, attack_two, armor, movement))))
                if attack_two != 'null':
                    second_weapon = weapons[attack_two]
                else:
                    second_weapon = None
                Unit(
                    name=name,
                    health=health,
                    attack_one=weapons[attack_one],
                    attack_two=second_weapon,
                    armor=armors[armor],
                    movement=movements[movement]).save()
