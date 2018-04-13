from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import login, logout
from django.contrib.auth import update_session_auth_hash
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Q

from . import serializers

from . import models
from . import forms

from home import forms as home_form



# sign out
def signout_request(request):
    logout(request)
    return redirect('account:sign-in')

#sign up
class SignUp(View):
    template_name = 'account/sign-up.html'

    def get(self, request):

        sign_up_form = forms.RegistrationForm()

        variables = {
            'sign_up_form': sign_up_form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        sign_up_form = forms.RegistrationForm(request.POST or None)

        if sign_up_form.is_valid():
            sign_up_form.registration()
            return redirect('account:sign-in')

        variables = {
            'sign_up_form': sign_up_form,
        }

        return render(request, self.template_name, variables)



#sign in
class SignIn(View):
    template_name = 'account/sign-in.html'

    def get(self, request):
        signinForm = forms.SignInForm()

        variables = {
            'signinForm': signinForm,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        signinForm = forms.SignInForm(request.POST or None)

        if signinForm.is_valid():
            user = signinForm.signin()
            if user:
                login(request, user)
                return redirect('home:home')

        variables = {
            'signinForm': signinForm,
        }

        return render(request, self.template_name, variables)


#user profile
class Profile(View):
    template_name = 'account/profile.html'

    def get(self, request):

        variables = {

        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass



#user profile edit
class ProfileEdit(View):
    template_name = 'account/profile-edit.html'

    def get(self, request):

        profile_edit_form = forms.ProfileEditForm(instance=models.UserProfile.objects.get(username=request.user.username))

        variables = {
            'profile_edit_form': profile_edit_form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        profile_edit_form = forms.ProfileEditForm(request.POST or None, request.FILES, instance=models.UserProfile.objects.get(username=request.user.username))

        if profile_edit_form.is_valid():
            profile_edit_form.save()
            return redirect('account:profile')

        variables = {
            'profile_edit_form': profile_edit_form,
        }

        return render(request, self.template_name, variables)



#change password
class ChangePassword(View):
    template_name = 'account/change-password.html'

    def get(self, request):
        change_password_form = forms.ChangePasswordForm(request.user)

        variables = {
            'change_password_form': change_password_form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        change_password_form = forms.ChangePasswordForm(data=request.POST or None, user=request.user)

        if change_password_form.is_valid():
            change_password_form.save()
            update_session_auth_hash(request, change_password_form.user)

            return redirect('account:profile')

        variables = {
            'change_password_form': change_password_form,
        }

        return render(request, self.template_name, variables)





#=====================================================================================================
#=====================================================================================================
#                                     api
#=====================================================================================================
#=====================================================================================================


#api view
class UserProfileAPI(APIView):
    def get(self, request):
        if request.GET.get("username"):
            username = request.GET.get("username")

            userObj = models.UserProfile.objects.filter(username=username)

            serializer = None
            x = 'User authorized'

            if request.user.is_authenticated() and request.user.username == username:
                serializer = serializers.UserProfileSerializer(userObj, many=True).data
            else:
                x = 'Error authentication'

            return Response({
                'data': serializer,
                'x': x,
            })

