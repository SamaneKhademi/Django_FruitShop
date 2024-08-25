from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label='اسم و فامیل',
                                         widget=forms.TextInput(attrs={'class': 'form-control'}),
                                         required=True)
    shipping_email = forms.CharField(label='ایمیل',
                                     widget=forms.TextInput(attrs={'class': 'form-control'}),
                                     required=True)
    shipping_state = forms.CharField(label='استان',
                                     widget=forms.TextInput(attrs={'class': 'form-control'}),
                                     required=False)
    shipping_city = forms.CharField(label='شهر',
                                    widget=forms.TextInput(attrs={'class': 'form-control'}),
                                    required=True)
    shipping_address = forms.CharField(label='آدرس کامل',
                                       widget=forms.TextInput(attrs={'class': 'form-control'}),
                                       required=True)
    shipping_zipcode = forms.CharField(label='کدپستی',
                                       widget=forms.TextInput(attrs={'class': 'form-control'}),
                                       required=False)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_state', 'shipping_city', 'shipping_address', 'shipping_zipcode']
        exclude = ['user']