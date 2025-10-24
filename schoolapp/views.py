from django.shortcuts import render, redirect
from . models import Teacher, Contact, clientFeedback
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_dashboard(request):
    contacts = Contact.objects.all().order_by('-id')[:5]
    teachers = Teacher.objects.all().order_by('name')
    feedbacks = clientFeedback.objects.all().order_by('-created_at')[:5]
    return render(request, 'admin_dashboard.html', {'contacts': contacts, 'teachers': teachers, 'feedbacks':feedbacks})

def index(request):
    contacts = Contact.objects.all().order_by('-id')[:5]
    teachers = Teacher.objects.all()[:3]
    feedbacks = clientFeedback.objects.all()
    return render(request, 'main/index.html', {"teachers": teachers, "feedbacks":feedbacks, "contacts":contacts})

# def index(request):
#     teachers = Teacher.objects.all()[:4]
#     if request.method == 'POST':
#         name = request.POST.get("name")
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         Contact.objects.create(name=name, phone=phone, email=email, message=message)
#         return redirect('index')
#     return render(request, 'main/index.html', {"teachers":teachers})
def about(request):
    return render(request, 'main/about.html')
def contact(request):
    return render(request, 'main/contact.html')
def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, phone=phone, email=email, message=message)
        return redirect('index')
    return render('main/index.html')

def teacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'main/teacher.html', {"teachers":teachers})
def vehicle(request):
    return render(request, 'main/vehicle.html')





from django.core.files.storage import default_storage

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        uploaded = request.FILES.get('image')

        image_url = None
        if uploaded:
            path = default_storage.save('uploads/' + uploaded.name, uploaded)
            image_url = default_storage.url(path)

        # Save contact data
        Contact.objects.create(
            name=name,
            phone=phone,
            email=email,
            message=message,
        )

        # Re-render page with success message or image preview
        return render(request, 'main/contact.html', {'submitted_image_url': image_url, 'success': True})

    # 👇 Always return something on GET
    return render(request, 'main/contact.html')


# Create your views here.
