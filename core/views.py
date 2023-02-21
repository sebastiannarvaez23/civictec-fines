from .forms import OfficerCreationFormExtensible
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django import forms
from .models import (
    Citation as CitationModel, 
    Officer as OfficerModel,
)

# Create your views here.

def user_in_group(user):
    return user.groups.filter(name__in=["Admin", "Clerk"]).exists()

class Officer(TemplateView):
    """Class Officer"""
    template_name = "officer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['officers'] = OfficerModel.objects.all()
        if self.request.user.is_authenticated:
            context['myProfileOfficer'] = OfficerModel.objects.filter(user = self.request.user)[0]
            context['groupsUser'] = self.request.user.groups.all()[0]
        return context

class CitationListView(ListView):
    """Class Citation"""
    template_name = "citations.html"
    model = CitationModel

    def is_user_in_clerk_group(self, user):
        clerk_group = Group.objects.get(name='Clerk')
        return clerk_group in user.groups.all()

    def is_user_in_officer_group(self, user):
        officer_group = Group.objects.get(name='Officer')
        return officer_group in user.groups.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        name_passenger = self.request.GET.get('name_passenger')
        
        if name_passenger:
            queryset = queryset.filter(name_passenger__icontains=name_passenger)

        if self.request.user.is_authenticated:
            agency_profile = OfficerModel.objects.filter(user = self.request.user)[0].agency
            if self.is_user_in_clerk_group(self.request.user):
                queryset = queryset.filter(issued_by__agency=agency_profile)
            elif self.is_user_in_officer_group(self.request.user):
                queryset = queryset.filter(issued_by__agency=agency_profile)
        return queryset

class OfficerCreate(CreateView):
    form_class = OfficerCreationFormExtensible
    success_url = reverse_lazy('citation')
    template_name = "signup.html"

    def get_success_url(self):
        return reverse_lazy('citation') + '?register'

    def get_form(self, form_class=None):
        form = super(OfficerCreate, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'username'})
        form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Name'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Last Name'})
        form.fields['groups'].widget = forms.CheckboxSelectMultiple()
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Password'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repeat Password'})
        
        return form

class OfficerDelete(DeleteView):
    model = OfficerModel
    template_name = 'officer_confirm_delete.html'
    success_url = reverse_lazy('officer')
