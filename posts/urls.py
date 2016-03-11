from django.conf.urls import include, url
from django.contrib import admin
from posts import views #gets all our view functions

# dont need an html page for each url route, some just point to funtions in the view (logout, delete, ect)
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),

    url(r'^white$', views.Pick_White.as_view(), name='white'),
    url(r'^black$', views.Pick_Black.as_view(), name='black'),
]

