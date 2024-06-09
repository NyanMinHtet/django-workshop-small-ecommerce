from django import forms
from .models import Receipt


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ("cus_name","email","phone_no","address","payment_method")