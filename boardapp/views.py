from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView,DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import models


def boardsignup(request):
    if request.method == "POST":
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request,'boardapp/signup.html',{'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '',password2)
            return render(request,'boardapp/login.html')

    return render(request,'boardapp/signup.html')

def boardlogin(request):
    if request.method == "POST":
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('boardlist')
        else:
            return render(request,'boardapp/login.html',{'error':'正しいユーザー名とパスワードを入力してください'})

    return render(request,'boardapp/login.html',)

def boardlogout(request):
    logout(request)
    return redirect('boardlogin')

def boardlist(request):
    if request.user.is_authenticated:
        object_list = models.BoardModel.objects.all().reverse()
        return render(request,'boardapp/board.html',{'object_list':object_list})
    else:
        return redirect('boardlogin')


class BoardDetail(DetailView):
    template_name='boardapp/detail.html'
    model = models.BoardModel

class BoardCreate(CreateView):
    template_name='boardapp/create.html'
    model= models.BoardModel
    fields=('title','content','author','images')
    success_url = reverse_lazy('boardlist')

def boardgood(request, pk):
    post=models.BoardModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('boardlist')

def boardread(request,pk):
    post = models.BoardModel.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('boardlist')
    else:
        post.read += 1
        post.readtext = post.readtext +" "+post2
        post.save()
        return redirect('boardlist')








#
