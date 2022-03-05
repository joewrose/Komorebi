import uuid

from django import forms
from django.contrib.auth.forms import UserCreationForm

from manageImages.models import Picture
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ImageForm(forms.ModelForm):
    image = forms.ImageField()
    name = forms.CharField(max_length=100, help_text="Enter image name")
    ID = forms.UUIDField(widget=forms.HiddenInput(), required=False)
    url = forms.URLField(widget=forms.HiddenInput(), required=False)
    likes = forms.IntegerField(widget=forms.HiddenInput(), required=False, initial=0)
    dislikes = forms.IntegerField(widget=forms.HiddenInput(), required=False, initial=0)
    time = forms.DateTimeField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Picture
        fields = ('name', 'image')
