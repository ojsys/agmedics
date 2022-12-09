from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, View
from django.shortcuts import redirect, render
from .forms import *
from .models import Patient
from account.models import User
from django.conf import settings
from django.contrib import messages


@login_required(login_url='login')
def home(request):
    return render(request, 'hospital/dashboard.html', {
        'page_title': 'Dashboard'
    })



def patients(request):
    patients = Patient.objects.all()

    return render(request, 'hospital/patients.html', {'page_title': 'Patients', 'patients': patients})



def add_patient(request):
    form = AddPatientForm()
    if request.method == 'POST':
        form = AddPatientForm(request.POST)
        if form.is_valid():
            hostpital_no = form.cleaned_data['hostpital_no']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            date_of_birth = form.cleaned_data['date_of_birth']
            age = form.cleaned_data['age']
            address = form.cleaned_data['address']
            mobile_number = form.cleaned_data['mobile_number']
            ailment = form.cleaned_data['ailment']

            # Add New Patient's Record
            new_patient = Patient(
                hostpital_no = hostpital_no,
                firstname=firstname, 
                lastname=lastname,
                date_of_birth = date_of_birth,
                age=age,
                address = address,
                mobile_number=mobile_number,
                ailment=ailment
            )
            new_patient.save()
            return render(request, 'hospital/add_patient.html', {'form': form, 'success': True})

    return render(request, 'hospital/add_patient.html',{'form': form,})