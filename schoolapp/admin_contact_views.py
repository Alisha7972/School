from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

#List 
def admin_contact_list(request):
    contacts = Contact.objects.all().order_by('-id')
    return render(request, 'admin_contact/contact_list.html', {"contacts":contacts})

#Add 
def admin_contact_add(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_contact_list")
    else:
        form = ContactForm()
    return render(request, 'admin_contact/contact_add.html', {"form":form})

#Delete
def admin_contact_delete(request,pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('admin_contact_list')
    return render(request, 'admin_contact/contact_confirm_delete.html', {'contact':contact})        
