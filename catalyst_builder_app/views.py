from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.http import JsonResponse
from .models import UploadedFile, CompanyData
from .forms import UploadFileForm, QueryForm
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CompanyDataSerializer
import csv


def handle_uploaded_file(f, user):
    uploaded_file = UploadedFile(user=user, file=f)
    uploaded_file.save()

    with open(uploaded_file.file.path, newline='', encoding='utf-8', errors='replace') as file:
        reader = csv.DictReader(file)
        for row in reader:
            locality_data = row['locality'].split(', ')
            city = locality_data[0] if len(locality_data) > 0 else ''
            state = locality_data[1] if len(locality_data) > 1 else ''
            country = locality_data[2] if len(locality_data) > 2 else ''

            year_founded = row['year founded']
            year_founded = int(year_founded) if year_founded.isdigit() else None 

            CompanyData.objects.create(
                name=row['name'],
                domain=row['domain'] if row['domain'] else None,
                year_founded=year_founded,
                industry=row['industry'],
                size_range=row['size range'],
                city=city,
                state=state,
                country=country,
                linkedin_url=row['linkedin url'] if row['linkedin url'] else None,
                current_employee_estimate=int(row['current employee estimate']) if row['current employee estimate'].isdigit() else 0,
                total_employee_estimate=int(row['total employee estimate']) if row['total employee estimate'].isdigit() else 0
            )

@login_required
def upload_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], request.user)
            return JsonResponse({'success': True})
    else:
        form = UploadFileForm()
    uploaded_files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'catalyst_builder_app/upload_data.html', {'form': form, 'uploaded_files': uploaded_files})



@login_required
def query_builder(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            filters = {key: value for key, value in form.cleaned_data.items() if value}
            if 'keyword' in filters:
                filters['name__icontains'] = filters.pop('keyword')
            data = CompanyData.objects.filter(**filters)
            count = data.count()
            return render(request, 'catalyst_builder_app/query_builder.html', {'form': form, 'count': count})
    else:
        form = QueryForm()
    return render(request, 'catalyst_builder_app/query_builder.html', {'form': form})

@api_view(['GET'])
def query_data(request):
    filters = request.GET.dict()
    if 'keyword' in filters:
        filters['name__icontains'] = filters.pop('keyword')
    data = CompanyData.objects.filter(**filters)
    serializer = CompanyDataSerializer(data, many=True)
    return Response({'count': data.count(), 'results': serializer.data})



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, 'Account created successfully')
        return redirect('login')
    return render(request, 'catalyst_builder_app/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'catalyst_builder_app/login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('login')

def base(request):
    return render(request, 'catalyst_builder_app/base.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'catalyst_builder_app/user_list.html', {'users': users})
