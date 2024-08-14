from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = UsernameField(label='نام کاربری', widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(attrs={'class':'form-control'}))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='نام کاربری',
        help_text='<ul class="form-text text-muted"><li>نام کاربری میتواند شامل عدد ، حروف و @/./+/-/_ باشد.</li></ul>',
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    email = forms.CharField(label='ایمیل', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label='رمز عبور',
        help_text='<ul class="form-text text-muted small"><li>رمز عبور باید حداقل 8 کاراکتر باشد.</li><li>رمز عبور نمی تواند فقط عدد باشد.</li><li>رمز عبور نمی تواند یک رمز عبور معمولی باشد.</li><li>رمز عبور نمی تواند مشابه دیگر اطلاعات شخصی شما باشد.</li></ul>',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

