from django.core.management.base import BaseCommand
from interface.models import Cell

import json
import os

class Command(BaseCommand):
    help = "Seed the database with all available data"

    def handle(self, *args, **options):
        try:
            TERRAIN_PATH = '%s/common/resources/terrain.json' % (os.environ["DOMOROOT"],)
            self.clearCells()
            # Should be the path to the common types list
            with open(TERRAIN_PATH, 'r') as tFile:
                terrain = json.loads(tFile.read())
                for cell in terrain["terrain"]:
                    print("Creating Cell(%s, %s)" % (cell["spriteName"], cell["cType"]))
                    newCell = Cell(spriteName=cell["spriteName"], cType=cell["cType"])
                    newCell.save()
        except KeyError:
            print("Please define the $DOMOROOT environment variable to your domoco dir")

    def clearCells(self):
        print("Clearing the Cells")
        for cell in Cell.objects.all():
            cell.delete()
