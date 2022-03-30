from django import forms
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PostForm(forms.ModelForm):

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-group mt-3 mb-4', 'placeholder':'enter your username...'}),
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={'class': 'form-group mt-3 mb-4','type':'email', 'placeholder':'enter your email...'}),
    )

    profileImage = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={'class': 'form-group mt-3 mb-4','type':'file'}),
    )

    city = forms.CharField(
        label="City",
        widget=forms.TextInput(attrs={'class': 'form-group mt-3 mb-4', 'placeholder':'enter your username...'}),
    )

    description = forms.CharField(
        label="Description",
        widget=forms.TextInput(attrs={'class': 'form-group mt-3 mb-4', 'placeholder':'enter your username...'}),
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
        fields = ('username', 'email', 'profileImage', 'city', 'description','password')

class EditForm(forms.ModelForm):

    username = forms.CharField(
        label="Username",
        required=False,
        empty_value=None,
        widget=forms.HiddenInput(attrs={'class': 'form-group mt-3 mb-4', 'placeholder':'enter your username...'}),
    )

    email = forms.CharField(
        label="Email",
        required=False,
        empty_value=None,
        widget=forms.TextInput(attrs={'class': 'form-group mt-3 mb-4','type':'email', 'placeholder':'enter your email...'}),
    )

    profileImage = forms.ImageField(
        label="Image",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-group mt-3 mb-4','type':'file'}),
    )

    city = forms.CharField(
        label="City",
        required=False,
        empty_value=None,
        widget=forms.TextInput(attrs={'class': 'form-group mt-3 mb-4', 'placeholder':'enter your username...'}),
    )

    description = forms.CharField(
        label="Description",
        required=False,
        empty_value=None,
        widget=forms.TextInput(attrs={'class': 'form-group mt-3 mb-4', 'placeholder':'enter your username...'}),
    )

    password = forms.CharField(
        label="Password",
        required=False,
        empty_value=None,
        widget=forms.PasswordInput(attrs={'class': 'form-group mt-3 mb-4', 'type':'password','placeholder':'enter your password...'}),
    )


    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'

    class Meta:
        model = CustomUser
        fields = ('email', 'profileImage', 'city', 'description', 'password')



