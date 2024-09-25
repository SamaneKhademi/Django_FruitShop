from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile


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


class UpdateUserForm(UserChangeForm):
    password = None
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}), required=False)
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email')


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='رمز عبور قبلی', widget=forms.PasswordInput(attrs={'autofocus': True, 'class': 'form-control'}))
    new_password1 = forms.CharField(label='رمز عبور جدید', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='تکرار رمز عبور جدید', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserInfoForm(forms.ModelForm):
    full_name = forms.CharField(label='اسم و فامیل', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    phone = forms.CharField(label='تلفن', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    state = forms.CharField(label='استان', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    city = forms.CharField(label='شهر', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    address = forms.CharField(label='آدرس', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    zipcode = forms.CharField(label='کدپستی', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Profile
        fields = ('full_name', 'phone', 'state', 'city', 'address', 'zipcode')
