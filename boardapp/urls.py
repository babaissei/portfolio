from django.urls import path
from . import views

urlpatterns = [
    path('',views.boardsignup,name='boardsignup'),
    path('login/',views.boardlogin,name='boardlogin'),
    path('list/',views.boardlist,name='boardlist'),
    path('detail/<int:pk>',views.BoardDetail.as_view(),name='boarddetail'),
    path('logout/',views.boardlogout,name='boardlogout'),
    path('create/',views.BoardCreate.as_view(),name='boardcreate'),
    path('read/<int:pk>',views.boardread,name='boardread'),
    path('good/<int:pk>',views.boardgood,name='boardgood'),
]
