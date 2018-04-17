from django import forms
from django.contrib.auth import authenticate
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm
import re

from . import models



# user registration form
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    email = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'email'}))
    phone = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    job_title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    company = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    address = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )
    suit_floor_apt = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    city = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    state = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    zip_postal_code = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    password1 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))
    password2 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate', 'id': 'password'}))


    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')

        job_title = self.cleaned_data.get('job_title')
        company = self.cleaned_data.get('company')
        address = self.cleaned_data.get('address')
        suit_floor_apt = self.cleaned_data.get('suit_floor_apt')

        city = self.cleaned_data.get('city')
        state = self.cleaned_data.get('state')
        zip_postal_code = self.cleaned_data.get('zip_postal_code')

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')


        if len(username) < 1:
            raise forms.ValidationError("Enter username!")
        else:
            user_exist = models.UserProfile.objects.filter(username__iexact=username).exists()
            if user_exist:
                raise forms.ValidationError("Username already taken!")
            else:
                if len(email) < 1:
                    raise forms.ValidationError("Enter email address!")
                else:
                    email_correction = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
                    if email_correction == None:
                        raise forms.ValidationError("Email not correct!")
                    else:
                        email_exist = models.UserProfile.objects.filter(email__iexact=email).exists()
                        if email_exist:
                            raise forms.ValidationError("Email already exist!")
                        else:
                            if len(password1) < 8:
                                raise forms.ValidationError("Password is too short!")
                            else:
                                if password1 != password2:
                                    raise forms.ValidationError("Password not matched!")



    def registration(self, request):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')

        job_title = self.cleaned_data.get('job_title')
        company = self.cleaned_data.get('company')

        address = self.cleaned_data.get('address')
        suit_floor_apt = self.cleaned_data.get('suit_floor_apt')

        city = self.cleaned_data.get('city')
        state = self.cleaned_data.get('state')
        zip_postal_code = self.cleaned_data.get('zip_postal_code')

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        member_type = request.POST.get('member_type')

        user = models.UserProfile.objects.create_user(username=username, email=email, phone=phone, job_title=job_title, company=company, address=address, suit_floor_apt=suit_floor_apt, city=city, state=state, zip_postal_code=zip_postal_code)
        user.set_password(password1)

        if member_type == 'investor':
            user.investor = True
        elif member_type == 'farmer':
            user.farmer = True

        user.save()



# login form
class SignInForm(forms.Form):
    username = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))
    password = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate', 'id': 'password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if len(username) < 1:
            raise forms.ValidationError("Enter Username!")
        else:
            if len(password) < 8:
                raise forms.ValidationError("Password is too short!")
            else:
                user = authenticate(username=username, password=password)
                if not user or not user.is_active:
                    raise forms.ValidationError("Username or Password not matched!")


    def signin(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user



#user profile edit form
class ProfileEditForm(forms.ModelForm):
    address = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )

    class Meta:
        model = models.UserProfile
        fields = ('phone', 'photo', 'job_title', 'company', 'address', 'suit_floor_apt', 'city', 'state', 'zip_postal_code')



#change password form
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))
    new_password1 = forms.CharField(label='New Password', max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))
    new_password2 = forms.CharField(label='Confirm Password', max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))

    def clean(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        if len(new_password1) < 8:
            raise forms.ValidationError("Password is too short!")
        else:
            if new_password1 != new_password2:
                raise forms.ValidationError("Password not matched!")

