from django.shortcuts import render
from django.http import HttpResponse

def get_name(request, name):
    return HttpResponse(f"<h1 style=color:red>Ваша имя: {name}</h1>")

def get_sername(request, sername):
    return HttpResponse(f"<h1 style=color:red>Ваша фамилия: {sername}</h1>")

def get_age(request, age):
    return HttpResponse(f"<h1 style=color:red>Скоко вам лет: {age}</h1>")

def get_birthday(request, birthday):
    return HttpResponse(f"<h1 style=color:red>Ваша день рождение: {birthday}</h1>")

def get_long(request, long):
    return HttpResponse(f"<h1 style=color:red>Ваша длина: {long}</h1>")

