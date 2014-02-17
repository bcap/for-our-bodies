from django.shortcuts import render
from django.http import HttpResponse

from for_our_bodies.models import User, Entry

def index(request):
    users = User.objects.all()
    context = { 'users': users }
    return render(request, 'index.html', context)


def users(request):
    return HttpResponse('viewing all users page')


def user_by_name(request, username):
    return HttpResponse('viewing page for user with name {}'.format(username))


def user_by_id(request, userid):
    return HttpResponse('viewing page for user with id {}'.format(userid))