from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def users(request):
    return HttpResponse('viewing all users page')


def user_by_name(request, username):
    return HttpResponse('viewing page for user with name {}'.format(username))


def user_by_id(request, userid):
    return HttpResponse('viewing page for user with id {}'.format(userid))