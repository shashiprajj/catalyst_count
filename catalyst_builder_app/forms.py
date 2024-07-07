from django import forms
from .models import CompanyData

class UploadFileForm(forms.Form):
    file = forms.FileField()

class QueryForm(forms.Form):
    keyword = forms.CharField(required=False)
    industry = forms.ModelChoiceField(queryset=CompanyData.objects.values_list('industry', flat=True).distinct(), required=False)
    year_founded = forms.ModelChoiceField(queryset=CompanyData.objects.values_list('year_founded', flat=True).distinct(), required=False)
    city = forms.ModelChoiceField(queryset=CompanyData.objects.values_list('city', flat=True).distinct(), required=False)
    state = forms.ModelChoiceField(queryset=CompanyData.objects.values_list('state', flat=True).distinct(), required=False)
    country = forms.ModelChoiceField(queryset=CompanyData.objects.values_list('country', flat=True).distinct(), required=False)
    current_employee_estimate = forms.IntegerField(required=False)
    total_employee_estimate = forms.IntegerField(required=False)
