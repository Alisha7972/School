from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

#=================
#   CONTACT
#=================  

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name  

#=====================
#   CLIENT FEEDBACK
#=====================  

class clientFeedback(models.Model):
    student_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=190, blank=True, help_text="e.g. Grade 8 student or participant")
    feedback = models.TextField()
    photo = models.ImageField(upload_to='feedback/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name


# Create your models here.
