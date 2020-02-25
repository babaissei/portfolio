from django.urls import path
from . import views

urlpatterns = [
    path('',views.TodoIndex.as_view(),name='todoindex'),
    path('create/',views.TodoCreate.as_view(),name='todocreate'),
    path('detail/<int:pk>', views.TodoDetail.as_view(), name='tododetail'),
    path('update/<int:pk>', views.TodoUpdate.as_view(), name='todoupdate'),
    path('delete/<int:pk>', views.TodoDelete.as_view(), name='tododelete'),
]
