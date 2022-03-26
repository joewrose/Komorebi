import uuid
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm

from manageImages.models import Picture
from django.contrib.auth.models import User


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

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'


class ImageForm(forms.ModelForm):

    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={'class': 'form-group mt-3 mb-4', 'placeholder':'Enter name of image...'}),
    )

    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={'class': 'form-group mt-3 mb-4','type':'file'}),
    )

    ID = forms.UUIDField(
        required=False,
        widget=forms.HiddenInput(attrs={'class': 'form-group mt-3 mb-4'}),
    )

    url = forms.URLField(
        required=False,
        widget=forms.HiddenInput(attrs={'class': 'form-group mt-3 mb-4'}),
    )

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'

    class Meta:
        model = Picture
        fields = ('name', 'image', 'ID', 'url',)



