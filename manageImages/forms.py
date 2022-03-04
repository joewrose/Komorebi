from django import forms
from manageImages.models import Picture

class ImageForm(forms.ModelForm):
    image = forms.ImageField()
    name = forms.CharField(max_length=100,help_text="Enter image name")
    ID = forms.IntegerField(widget=forms.HiddenInput())
    url = forms.URLField(widget=forms.HiddenInput())
    likes = forms.IntegerField(widget=forms.HiddenInput())
    dislikes = forms.IntegerField(widget=forms.HiddenInput())
    time = forms.DateTimeField(widget=forms.HiddenInput())


    class Meta:
        model = Picture
        fields=('name','image')