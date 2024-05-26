# forms.py
from django import forms

class OrderSearchForm(forms.Form):
    order_number = forms.CharField(max_length=100, label='Order Number')

