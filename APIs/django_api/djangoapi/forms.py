from django import forms
from django.forms.fields import EmailField
from .models import Person

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.EmailField()
    age = forms.IntegerField()

    class Meta:
        model = Person
        fields = '__all__'
    
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        # let's say we wanted to make our data all caps, we could do that here!
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.age = self.cleaned_data['age']
        if commit:
            user.save()
        return user