from django.http import HttpResponse
from django.http import Http404
from django.core import serializers
from django.contrib.auth import authenticate

from interface.models import Cell, ResponseTemplate, LoginData

import json, uuid

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

def login(request):
    if request.method != "POST":
        raise Http404
    user = authenticate(username=request.POST["username"],
                        password=request.POST["password"])
    if user is not None:
        info = {"token": str(uuid.uuid4())}
        loginInfo = LoginData(userid=user.id, token=info["token"])
        loginInfo.save()
        return HttpResponse(json.dumps(info),
                            content_type="application/json")
    return HttpResponse("incorrect username or password", status=403)
