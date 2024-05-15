from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from . import forms,models
from django.contrib.auth.models import Group


# Create your views here.
def home_view(request):
    return render(request ,"main/index.html")

#for showing signup/login button for admin
def adminclick_view(request):
    return render(request,'main/adminclick.html')

#for showing signup/login button for doctor
def doctorclick_view(request):
    return render(request,"main/doctorclick.html")


#for showing signup/login button for patient
def patientclick_view(request):
    return render(request,"main/patientclick.html")

def admin_signup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
    return render(request,'main/adminsignup.html',{'form':form})

def doctor_signup_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor=doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('doctorlogin')
    return render(request,'main/doctorsignup.html',context=mydict)