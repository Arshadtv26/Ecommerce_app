# payments/forms.py

from django import forms

class PaymentForm(forms.Form):
    amount = forms.DecimalField(label='Amount', max_digits=10, decimal_places=2)
    stripeToken = forms.CharField(widget=forms.HiddenInput)
