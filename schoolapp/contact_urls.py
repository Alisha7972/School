from django.urls import path
from . import admin_contact_views

urlpatterns = [
    path("contact/", admin_contact_views.admin_contact_list, name='admin_contact_list'),
    path("contact/add/", admin_contact_views.admin_contact_add, name='admin_contact_add'),
    path("contact/delete/<int:pk>/", admin_contact_views.admin_contact_delete, name='admin_contact_delete'),
]