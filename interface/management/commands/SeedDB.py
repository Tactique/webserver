from django.core.management.base import BaseCommand
from interface.models import Cell

import os
import csv

class Command(BaseCommand):
    help = "Seed the database with all available data"

    def handle(self, *args, **options):
        try:
            TERRAIN_PATH = '%s/common/resources/terrain.csv' % (os.environ["DOMOROOT"],)
            self.clearCells()
            # Should be the path to the common types list
            with open(TERRAIN_PATH, 'r') as tFile:
                terrain_reader = csv.reader(tFile)
                next(terrain_reader, None)
                for cType, spriteName in terrain_reader:
                    print("Creating Cell(%s, %s)" % (cType, spriteName))
                    Cell(spriteName=spriteName, cType=cType).save()
        except KeyError:
            print("Please define the $DOMOROOT environment variable to your domoco dir")

    def clearCells(self):
        print("Clearing the Cells")
        for cell in Cell.objects.all():
            cell.delete()
