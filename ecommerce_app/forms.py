from django import forms
from .models import Order


class CartForm(forms.Form):
    quantity = forms.IntegerField(initial='1')
    product_id = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(CartForm, self).__init__(*args, **kwargs)


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('paid',)

        widgets = {
            'address': forms.Textarea(attrs={'row': 5, 'col': 8}),
        }

subscription_options = [
    ('1-month', '1-Month subscription ($15 USD/Mon)'),
    ('1-year', '1-Year subscription ($35 USD/Mon)'),
]
 
 
class SubscriptionForm(forms.Form):
    plans = forms.ChoiceField(choices=subscription_options)
