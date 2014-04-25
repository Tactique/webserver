from django.core.management.base import BaseCommand
from interface.models import ResponseTemplate

import json
import os

class Command(BaseCommand):
    help = "Import JSON response templates for protocol verification on the client"

    def handle(self, *args, **options):
        try:
            RESPONSE_DIR = '%s/common/responses' % (os.environ["DOMOROOT"],)
            self.clearTemplates();
            for responsePath in os.listdir(RESPONSE_DIR):
                fullPath = "%s/%s" % (RESPONSE_DIR, responsePath)
                with open(fullPath, 'r') as rFile:
                    templates = json.loads(rFile.read())
                    for template in templates:
                        print("Adding template for response %s" % template)
                        JSONstr = json.dumps(templates[template])
                        newTemplate = ResponseTemplate(name=template,
                                                       JSON=JSONstr)
                        newTemplate.save()
        except KeyError:
            print("Please define the $DOMOROOT environment variable to your domoco dir")

    def clearTemplates(self):
        print("Clearing templates")
        for template in ResponseTemplate.objects.all():
            template.delete() 
