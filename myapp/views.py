from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.urls import reverse_lazy
from myapp.forms import EnquiryForm
from myapp.models import Enquiry
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from myapp.models import Student
from django.views.generic.list import ListView

# Create your views here.
def homePage(request):
    return render(request,'home.html')

def aboutPage(request):
    time = datetime.now()
    return render(request,'about.html',{'now':time,'student1':'Jagadeesh','student2':'kumar'})

def coursePage(request):
    return render(request,'course.html')

def addEnquiry(request):
    myform = EnquiryForm(request.POST or None)
    if myform.is_valid():
        myform.save()
        return HttpResponse("SAVED SUCCESSFULLY!")
    return render(request,'enquiry.html',{'sample':myform})

def staffPage(request):
    return render(request,'staff.html')

def viewEnquiries(request):
    data = Enquiry.objects.all()
    return render(request,'enquiries.html',{'data':data})

def editPage(request,id):
    data = get_object_or_404(Enquiry,pk=id)
    form = EnquiryForm(request.POST or None,instance=data)
    if form.is_valid():
        form.save()
        return redirect('/staff/view')
    return render(request,'edit.html',{'data':form})

def deletePage(request,id):
    data = get_object_or_404(Enquiry,pk=id)
    if request.method=="POST":
        data.delete()
        return redirect('/staff/view')
    return render(request,'delete.html',{'data':data})

class AddStudent(CreateView):
    model = Student
    fields = "__all__"
    template_name = 'addStudent.html'
    success_url = reverse_lazy('staff')

class ViewStudents(ListView):
    model = Student
    template_name = 'viewStudent.html'
    queryset = Student.objects.all()
    context_object_name = 'student'

class EditStudent(UpdateView):
    model = Student
    fields = ('name','course','mobile','date','fees','mail','status')
    template_name = 'editStudent.html'
    success_url = reverse_lazy('viewStu')

    def get_object(self, queryset=None):
        obj = get_object_or_404(Student,stdId=self.kwargs['id'])
        return obj

class DeleteStudent(DeleteView):
    model = Student
    template_name = 'deleteStudent.html'
    success_url = reverse_lazy('viewStu')
    context_object_name = 'obj'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Student, stdId=self.kwargs['id'])
        return obj