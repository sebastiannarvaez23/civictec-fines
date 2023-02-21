from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import (
    Agency,
    Citation,
    Officer
)

# Register your models here.

@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',)

@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    list_display = ('agency', 'user',)

@admin.register(Citation)
class CitationsAdmin(admin.ModelAdmin):

    list_display = ('no_citation', 'city', 'name_passenger', 'phone_passenger', 'model_car', 'issued_by', 'issued_date', 'name_passenger',)
    ordering = ('issued_date',)
    search_fields = ('no_citation', 'issued_by')
    
    def is_user_in_clerk_group(self, user):
        clerk_group = Group.objects.get(name='Clerk')
        return clerk_group in user.groups.all()

    def is_user_in_officer_group(self, user):
        officer_group = Group.objects.get(name='Officer')
        return officer_group in user.groups.all()
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        agency_profile = Officer.objects.filter(user = request.user)[0].agency
        if self.is_user_in_clerk_group(request.user):
            return Citation.objects.filter(issued_by__agency=agency_profile)
        elif self.is_user_in_officer_group(request.user):
            return Citation.objects.filter(issued_by__agency=agency_profile)
        else:
            return qs

class OfficerAdmin(UserAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(username=request.user.username)

admin.site.unregister(User)
admin.site.register(User, OfficerAdmin)