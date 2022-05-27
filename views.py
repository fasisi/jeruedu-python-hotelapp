from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader

from pyairtable import Table

import json, hashlib

from .models import User

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

apikey = 'keyZpJXiECaT38IYT'
baseid = 'appkQIJ82hsUHmpox'

# Create your views here.
def login(request):

    template = loader.get_template('hotelapp/login.html')

    if request.method == 'POST':
        is_username = 'username' in request.POST
        is_password = 'password' in request.POST

        if is_username == True and is_password == True :
            username = request.POST['username']
            password = request.POST['password']

            if username == "" or password == "" :
                context = {}

                return HttpResponse(template.render(context, request))
            else:
                salted_password = '123' + password + '123'
                salted_password = hashlib.md5(salted_password.encode('utf-8')).hexdigest()

                test = User.objects.filter(
                    username__exact=username,
                    password__exact=salted_password
                )

                if len(test) == 0:
                    context = {}

                    return HttpResponse(template.render(context, request))
                else:
                    return HttpResponseRedirect('/hotelapp/reservasi/')

        else:
            context = {}

            return HttpResponse(template.render(context, request))

    else:
        context = {}

        return HttpResponse(template.render(context, request))


def reservasi(request):
    table = Table(apikey, baseid, 'booking')
    pages = table.iterate()

    records = []
    for page in pages:
        for record in page:
            records.append(record)

    context = {
        "records": records
    }

    template = loader.get_template('hotelapp/reservasi.html')

    return HttpResponse(template.render(context, request))


def rooms(request):
    table = Table(apikey, baseid, 'hotel')
    pages = table.iterate()

    records = []
    for page in pages:
        for record in page:
            records.append(record)

    template = loader.get_template("hotelapp/rooms.html")

    context = {
        "records": records
    }

    return HttpResponse(template.render(context, request))

@method_decorator(csrf_exempt, name="dispatch")
def rooms_get(request):
    recordid = request.POST['recordid']

    table = Table(apikey, baseid, 'hotel')
    record = table.get(recordid)

    result = {
        "recordid": record['id'],
        'name': record['fields']['Name'],
        'description': record['fields']['Description'],
        'images': record['fields']['Images'],
        'price': record['fields']['Price'],
    }

    return JsonResponse(result, status=201)

@method_decorator(csrf_exempt, name="dispatch")
def rooms_submit(request):
    recordid = request.POST['recordid']
    name = request.POST['name']
    description = request.POST['description']
    price = request.POST['price']
    images = request.POST['images']

    table = Table(apikey, baseid, 'hotel')
    table.update(
        recordid,
        {
            'Name': name,
            'Description': description,
            'Price': price,
            'Images': images,
        }
    )

    return JsonResponse({"status": "ok"}, status=201)

def rooms_delete(request):
    recordid = request.POST['recordid']

    table = Table(apikey, baseid, 'hotel')
    table.delete(recordid)

    return JsonResponse({"status": "ok"}, status=201)

def rooms_add(request):
    name = request.POST['name']
    description = request.POST['description']
    price = request.POST['price']
    images = request.POST['images']

    table = Table(apikey, baseid, 'hotel')
    table.create(
        {
            'Name': name,
            'Description': description,
            'Price': price,
            'Images': images,
        }
    )

    return JsonResponse({"status": "ok"}, status=201)



