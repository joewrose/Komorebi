import uuid

from django import forms
from manageImages.models import Picture


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
