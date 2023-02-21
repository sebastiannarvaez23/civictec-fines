from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.db.models import Q

class OfficerCreationFormExtensible(UserCreationForm):
    
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.filter(Q(name='Clerk')| Q(name='Officer')), widget=forms.CheckboxSelectMultiple(), required=True, )
    first_name = forms.TextInput()
    last_name = forms.TextInput()

    class Meta(UserCreationForm.Meta):
        model = User 
        fields = ('username', 'first_name', 'last_name', 'groups', 'password1', 'password2',)