from django.urls import path
from .views import *

urlpatterns = [
    path("", homepage, name="homepage"),
    path('login', login, name = "login"),
    path('register', register, name = "register"),
    path("dash", dash, name = "dash"),
    path('add_note', add_note, name="add_note"),
    path("edit_note", edit_note, name = "add_note"),
    path('delete/<slug:note_id>', delete_note, name = "delete_note"),
]