from django import forms
from django.contrib.auth.hashers import make_password, check_password

from account import models as account_model
from . import models

#change user password from staff
class ChangeUserPasswordForm(forms.Form):
    new_password1 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))
    new_password2 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))

    def clean(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        if len(new_password1) < 8:
            raise forms.ValidationError("Password is too short!")
        else:
            if new_password1 != new_password2:
                raise forms.ValidationError("Password not matched!")


    def deploy(self, user_id):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        hash_pass = make_password(new_password1)

        deploy = account_model.UserProfile.objects.filter(id=user_id).update(password=hash_pass)



#product form
class ProductForm(forms.Form):
    name = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    contact_period = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    expected_return = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    harvest_period = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    description = forms.CharField(required=False, max_length=10000, widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}))
    extra = forms.CharField(required=False, max_length=5000, widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}))

    farm_size = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    price = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    farm_location = forms.CharField(required=False, max_length=5000, widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}))

    product_type = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    farm_email = forms.EmailField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    product_image = forms.ImageField(required=False)


    def clean(self):
        name = self.cleaned_data.get('name')
        contact_period = self.cleaned_data.get('contact_period')
        expected_return = self.cleaned_data.get('expected_return')
        harvest_period = self.cleaned_data.get('harvest_period')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        extra = self.cleaned_data.get('extra')
        farm_size = self.cleaned_data.get('farm_size')
        farm_location = self.cleaned_data.get('farm_location')
        product_type = self.cleaned_data.get('product_type')
        farm_email = self.cleaned_data.get('farm_email')
        product_image = self.cleaned_data.get('product_image')
        price = self.cleaned_data.get('price')


        if name == None:
            raise forms.ValidationError('Enter product name!')
        else:
            if contact_period == None:
                raise forms.ValidationError('Enter contact period!')
            else:
                if expected_return == None:
                    raise forms.ValidationError('Enter expected return in %!')
                else:
                    if harvest_period == None:
                        raise forms.ValidationError('Enter harvest period in month!')
                    else:
                        if title == None:
                            raise forms.ValidationError('Enter product title!')
                        else:
                            if description == None:
                                raise forms.ValidationError('Enter product description!')
                            else:
                                if product_image == None:
                                    raise forms.ValidationError('Select product image!')
                                else:
                                    if price == None:
                                        raise forms.ValidationError('Enter product price!')




    def deploy(self, request):
        name = self.cleaned_data.get('name')
        contact_period = self.cleaned_data.get('contact_period')
        expected_return = self.cleaned_data.get('expected_return')
        harvest_period = self.cleaned_data.get('harvest_period')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        extra = self.cleaned_data.get('extra')
        farm_size = self.cleaned_data.get('farm_size')
        farm_location = self.cleaned_data.get('farm_location')
        product_type = self.cleaned_data.get('product_type')
        farm_email = self.cleaned_data.get('farm_email')
        product_image = self.cleaned_data.get('product_image')
        price = self.cleaned_data.get('price')


        deploy = models.Product(user=request.user, name=name, contact_period=contact_period, expected_return=expected_return, harvest_period=harvest_period, price=price, title=title, description=description, extra=extra, farm_size=farm_size, farm_location=farm_location, product_type=product_type, farm_email=farm_email, product_image=product_image)
        deploy.save()


