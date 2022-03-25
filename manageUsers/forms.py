from django import forms
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PostForm(forms.ModelForm):

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-group mt-3 mb-4', 'placeholder':'enter your username...'}),
    )

    email = forms.CharField(
        label="Email",
        widget=forms.TextInput(attrs={'class': 'form-group mt-3 mb-4','type':'email', 'placeholder':'enter your email...'}),
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-group mt-3 mb-4', 'type':'password','placeholder':'enter your password...'}),
    )


    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'

    class Meta:
        model = CustomUser
        fields = ('username','email','password')


