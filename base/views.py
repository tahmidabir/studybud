from django.shortcuts import render

rooms=[
    {'id': 1, 'name': 'Lets learn python'},
    {'id': 2, 'name': 'Lets learn django'},
    {'id': 3, 'name': 'Frontend developer'},


]

users=[
    {'name':'Abir','id':1},
    {'name':'Sama','id':2},
    {'name':'Imtiaz','id':3}

]


def home(request):
    params={'rooms':rooms}
    return render(request,'base/home.html', params)


def room(request,pk):
    room=None
    for i in rooms:
        if i['id']==int(pk):
            room=i
        context={'room':room}
    return render(request, 'base/room.html',context)