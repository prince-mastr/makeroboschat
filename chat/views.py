from django.shortcuts import render, HttpResponse
from .models import User
from django.views import generic
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Chat
from django.db.models import Q


def index(request):
    User_list  = User.objects.all()
    return render(request, 'chat/index.html',{
        'user_list': list(User_list)
    })


def room(request, room_name):
    try:
        sender = User.objects.get(username = room_name)
        chats = Chat.objects.filter(Q(sender__username__icontains=sender.username) | Q(reciver__username__contains=sender.username))
        old_chat = ""
        for chat in chats[:10]:
            old_chat = old_chat + " \n " +  chat.messages + "\n" + str(chat.created_at)
        chats = Chat.objects.filter(reciver = sender)
        for chat in chats[:10]:
            old_chat = old_chat + " \n " +  chat.messages + "\n" + str(chat.created_at)
        return render(request, 'chat/room.html', {
            "old_chats": chats,
            'room_name': room_name
        })
    except User.DoesNotExist:
        User_list  = User.objects.all()
        return render(request, 'chat/room.html', {
            "no_found": True,
            'room_name': room_name,
            'user_list': list(User_list)
        })
    except:
        User_list  = User.objects.all()
        return render(request, 'chat/room.html', {
            "no_found": True,
            'room_name': room_name,
            'user_list': list(User_list)
        })
        

def users_available(request):
    User_list  = User.objects.all()
    return render(request, 'chat/list_user.html', {
        'user_list': list(User_list)
    })

def ChatUpdate(request):
    if request.method == 'POST':
        if 'message' in request.POST:
            message = request.POST['message']
            reciver = User.objects.get(username = request.POST['reciver'])
            New_chat = Chat.objects.create(
                sender = request.user,
                reciver = reciver,
                messages = message
            )
            New_chat.save()
        return HttpResponse('success') 



# Create your views here.
