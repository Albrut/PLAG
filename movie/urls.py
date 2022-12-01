from django.urls import path
from . import views
from django.urls import path
from movie import views




urlpatterns = [
    path("", views.index),
    path("create/", views.create),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
]
