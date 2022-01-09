from . import views
from django.urls import path, include 

urlpatterns = [
    path("", views.index, name = "index"),
    path("dataentry/", views.dataentry, name = "dataentry"),
    path("dbsearch/", views.dbsearch, name= "dbsearch"),
    path("dataentry/edit/<str:pk>", views.edit, name = "edit"),
    path("logout", views.logoutuser, name="logout")
]