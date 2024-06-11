from django import forms
from .models import Receipt


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ("cus_name","email","phone_no","address","payment_method")
        widgets = {
            'cus_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'example@gmail.com'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control','placeholder':'09xxxxxxxxx'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
        }