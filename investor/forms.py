from django import forms

from account import models as account_model


#recharge form
recharge_method_list = (
        ('bkash', 'BKASH'),
        ('dbbl_rocket', 'DBBL/ROCKET'),)

class CreditRechargeForm(forms.Form):
    method = forms.ChoiceField(choices=recharge_method_list, required=False, widget=forms.Select(attrs={'class': 'validate browser-default'}))
    sender_phone_number = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))
    transaction_id = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))
    credit = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))


    def clean(self):
        method = self.cleaned_data.get('method')
        sender_phone_number = self.cleaned_data.get('sender_phone_number')
        transaction_id = self.cleaned_data.get('transaction_id')
        credit = self.cleaned_data.get('credit')
        status = self.cleaned_data.get('status')

        if len(sender_phone_number) == 0:
            raise forms.ValidationError('Enter phone number from where you send money!')
        else:
            if len(transaction_id) == 0:
                raise forms.ValidationError('Enter Transaction ID! You found this in the confirmation message in DBBL or BKASH!')
            else:
                if credit == None:
                    raise forms.ValidationError('Enter recharge amount!')



    def deploy(self, request):
        method = self.cleaned_data.get('method')
        sender_phone_number = self.cleaned_data.get('sender_phone_number')
        transaction_id = self.cleaned_data.get('transaction_id')
        credit = self.cleaned_data.get('credit')
        status = self.cleaned_data.get('status')

        deploy = account_model.CreditRecharge(user=request.user, method=method, sender_phone_number=sender_phone_number, transaction_id=transaction_id, credit=credit)

        deploy.save()
