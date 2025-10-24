from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required , user_passes_test
from .models import Teacher, clientFeedback
from .forms import TeacherForm, clientFeedbackForm

def staff_required(user):
    return user.is_active and user.is_staff

#List
@user_passes_test(staff_required, login_url='/admin/login/')
def teacher_list(request):
    teachers = Teacher.objects.all().order_by('-created_at')
    return render(request, 'admin_pages/teacher_list.html', {"teachers":teachers})

#ADD
@user_passes_test(staff_required, login_url='/admin/login/')
def teacher_add(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("admin_teacher_list")
    else:
        form = TeacherForm()
    return render(request, 'admin_pages/teacher_form.html', {"form":form, 'action':'Add'})
    
    #Edit
@user_passes_test(staff_required, login_url='/admin/login/')
def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect("admin_teacher_list")
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'admin_pages/teacher_form.html', {'form':form, 'action':'Edit'})

#Delete
@user_passes_test(staff_required, login_url='/admin/login/')
def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect("admin_teacher_list")
    return render(request, 'admin_pages/teacher_confirm_delete.html', {"teacher":teacher, })        



            #===================
            #  CLIENT FEEDBACK
            #===================

#CLIENT FEEDBACK LIST
@user_passes_test(staff_required, login_url='/admin/login/')
def feedback_list(request):
    feedbacks = clientFeedback.objects.all().order_by('-created_at')
    return render(request, 'admin_Feedback/feedback_list.html', {"feedbacks":feedbacks})

# ADD FEEDBACK
@user_passes_test(staff_required, login_url='/admin/login/')
def feedback_add(request):
    if request.method == 'POST':
        form = clientFeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_feedback_list')
    else:
        form = clientFeedbackForm()
    return render(request, 'admin_Feedback/feedback_form.html', {'form':form, 'action':'Add'})

# EDIT FEEDBACK
@user_passes_test(staff_required, login_url='/admin/login/')
def feedback_edit(request, pk):
    feedback = get_object_or_404(clientFeedback, pk=pk)
    if request.method == 'POST':
        form = clientFeedbackForm(request.POST, request.FILES, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('admin_feedback_list')
    else:
        form = clientFeedbackForm(instance=feedback)
    return render(request, 'admin_Feedback/feedback_form.html', {'form':form, 'action':'Edit'})

# DELETE FEEDBACK
@user_passes_test(staff_required, login_url='/admin/login/')
def feedback_delete(request, pk):
    feedback = get_object_or_404(clientFeedback, pk=pk)
    if request.method == 'POST':
        feedback.delete()
        return redirect('admin_feedback_list')
    return render(request, 'admin_Feedback/feedback_confirm_delete.html', {'feedback':feedback})                



