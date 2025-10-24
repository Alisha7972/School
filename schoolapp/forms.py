from django import forms
from .models import Teacher, Contact, clientFeedback

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'subject', 'bio', 'photo']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']  

class clientFeedbackForm(forms.ModelForm):
    class Meta:
        model = clientFeedback
        fields = ['student_name', 'designation', 'feedback', 'photo']

