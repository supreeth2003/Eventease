from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.register, name="register"),
    path("events/", views.event_list, name="events"),
    path("events/add/", views.add_event, name="add_event"),
    path("events/<int:event_id>/", views.event_details, name="event_details"),
    path("events/edit/<int:event_id>/", views.edit_event, name="edit_event"),
    path("events/delete/<int:event_id>/", views.delete_event, name="delete_event"),
]
