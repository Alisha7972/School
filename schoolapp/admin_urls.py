from django.urls import path
from . import admin_views

urlpatterns = [
    path('teacher/', admin_views.teacher_list, name='admin_teacher_list'),
    path('teacher/add/', admin_views.teacher_add, name='admin_teacher_add'),
    path('teacher/edit/<int:pk>/', admin_views.teacher_edit, name='admin_teacher_edit'),
    path('teacher/delete/<int:pk>/', admin_views.teacher_delete, name='admin_teacher_delete'),

            #===================
            # CLIENT FEEDBACK
            #===================
    path('feedback/', admin_views.feedback_list, name='admin_feedback_list'),
    path('feedback/add/', admin_views.feedback_add, name='admin_feedback_add'),
    path('feedback/edit/<int:pk>/', admin_views.feedback_edit, name='admin_feedback_edit'),
    path('feedback/delete/<int:pk>/', admin_views.feedback_delete, name='admin_feedback_delete'),


]