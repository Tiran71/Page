from django.urls import path
from . import views

urlpatterns = [
    path('', views.Getlist.as_view(), name='list'),
    path('<int:pk>', views.Getdetail.as_view(), name='detail'),
    path('create/', views.create , name='create'),
    path('<int:pk>/delete', views.Getdelete.as_view() , name='delete'),
    path('<int:pk>/update', views.Getupdate.as_view() , name='update'),
]
