from django.http import HttpResponse
from django.http import Http404
from django.core import serializers

from interface.models import Cell, ResponseTemplate

import json

def get_cells(request, type_id=0):
    if type_id == 0:
        cells = Cell.objects.all()
    else:
        cells = Cell.objects.get(type_id)
    return HttpResponse(serializers.serialize("json", cells),
                        content_type="application/json")

def get_response_templates(request, responseName):
    try:
        resp = ResponseTemplate.objects.get(name=responseName)
        return HttpResponse(resp.JSON, content_type="application/json")
    except ResponseTemplate.DoesNotExist:
        raise Http404
