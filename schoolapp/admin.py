# from django.contrib import admin
# from .models import Teacher

# admin.site.register(Teacher)
# # admin.site.register(Contact)

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.shortcuts import redirect
from .models import Contact, Teacher, clientFeedback

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "open_crud_page")

    # ✅ Redirect the main admin page for Team2 to your custom list
    def changelist_view(self, request, extra_context=None):
        return redirect(reverse("admin_contact_list"))

    # ✅ Hide Django's default add/edit/delete pages
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # ✅ Add clickable link per row (optional, just for convenience)
    def open_crud_page(self, obj):
        url = reverse("admin_contact_list")  # Your custom URL name
        return format_html(f'<a href="{url}">🔗 Open contact CRUD</a>')

    open_crud_page.short_description = "Custom CRUD"



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "open_crud_page")

    # ✅ Redirect the main admin page for Team2 to your custom list
    def changelist_view(self, request, extra_context=None):
        return redirect(reverse("admin_teacher_list"))

    # ✅ Hide Django's default add/edit/delete pages
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # ✅ Add clickable link per row (optional, just for convenience)
    def open_crud_page(self, obj):
        url = reverse("admin_teacher_list")  # Your custom URL name
        return format_html(f'<a href="{url}">🔗 Open contact CRUD</a>')

    open_crud_page.short_description = "Custom CRUD"    


@admin.register(clientFeedback)
class clientFeedbackAdmin(admin.ModelAdmin):
    list_display = ("student_name", "open_crud_page")

    # ✅ Redirect the main admin page for Team2 to your custom list
    def changelist_view(self, request, extra_context=None):
        return redirect(reverse("admin_feedback_list"))

    # ✅ Hide Django's default add/edit/delete pages
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # ✅ Add clickable link per row (optional, just for convenience)
    def open_crud_page(self, obj):
        url = reverse("admin_feedback_list")  # Your custom URL name
        return format_html(f'<a href="{url}">🔗 Open feedback CRUD</a>')

    open_crud_page.short_description = "Custom CRUD"

# Register your models here.
