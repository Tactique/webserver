from django.http import HttpResponse
from django.http import Http404
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.http import require_POST

from interface.models import LoginData
from engine import engine
from tables.templates import ResponseTemplate
from tables.game_engine import Cell

import json
import uuid


def _get_sprite_name(cell):
    #TODO better sprite names here
    return cell.name


def get_cells(request):
    try:
        session = engine.get_session()
        cells_json = []
        for cell in session.query(Cell):
            cells_json.append({
                "cellType": cell.cellType,
                "spriteName": _get_sprite_name(cell)})
        return HttpResponse(
            json.dumps(cells_json),
            content_type="application/json")
    finally:
        session.close()

def get_response_templates(request, responseName):
    try:
        session = engine.get_session()
        resp = session.query(ResponseTemplate).filter(ResponseTemplate.name==responseName)
        try:
            return HttpResponse(resp[0].json, content_type="application/json")
        except IndexError:
            raise Http404
    finally:
        session.close()

def save_login_info(user):
    info = {"token": str(uuid.uuid4())}
    loginInfo = LoginData(userid=user.id, token=info["token"])
    loginInfo.save()
    return HttpResponse(json.dumps(info),
                        content_type="application/json")

def player_info(request):
    info = {"id": str(request.user.id)}
    return HttpResponse(json.dumps(info),
                        content_type="application/json")

@require_POST
def register_ajax(request):
    registration_form = UserCreationForm(data=request.POST)
    if registration_form.is_valid():
        user = registration_form.save()
        user = authenticate(username=request.POST["username"],
                            password=request.POST["password1"])
        login(request, user)
        return save_login_info(user)
    return HttpResponse(str(registration_form.errors), status=403)

@require_POST
def login_ajax(request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return save_login_info(user)
    return HttpResponse(str(form.errors), status=403)

@require_POST
def logout_ajax(request):
    logout(request)
    result = {}
    return HttpResponse(json.dumps(result),
                        content_type="application/json")
