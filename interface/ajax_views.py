from django.http import HttpResponse
from django.core import serializers

from interface.models import Cell

import json

def get_cells(request, type_id=0):
    if type_id == 0:
        cells = Cell.objects.all()
    else:
        cells = Cell.objects.get(type_id)
    return HttpResponse(serializers.serialize("json", cells),
                        content_type="application/json")