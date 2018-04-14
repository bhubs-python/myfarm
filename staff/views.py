from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from account import models as account_model
from account import forms as account_form

from . import forms
from . import models


#permission mixin
class StaffPermissionMixin(object):
    def has_permissions(self, request):
        return request.user.is_staff == True or request.user.is_superuser == True

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not self.has_permissions(request):
                return redirect('account:sign-in')
            return super(StaffPermissionMixin, self).dispatch(
                request, *args, **kwargs)
        else:
            return redirect('account:sign-in')



#staff home
class Home(StaffPermissionMixin, View):
    template_name = 'staff/index.html'

    def get(self, request):

        variables = {

        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#staff home
class UserHome(StaffPermissionMixin, View):
    template_name = 'staff/user-home.html'

    def get(self, request):
        change_status_sidebar = 'user-management'

        variables = {
            'change_status_sidebar': change_status_sidebar,
        }

        return render(request, self.template_name, variables)


#all user
class AllUser(StaffPermissionMixin, View):
    template_name = 'staff/all-user.html'

    def get(self, request):

        all_users = account_model.UserProfile.objects.all()
        all_users_count = account_model.UserProfile.objects.all().count()

        change_status_sidebar = 'user-management'

        variables = {
            'all_users': all_users,
            'all_users_count': all_users_count,
            'change_status_sidebar': change_status_sidebar,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass



#user detail
class UserDetail(StaffPermissionMixin, View):
    template_name = 'staff/user-detail.html'

    def get(self, request, user_id):

        get_object_or_404(account_model.UserProfile, pk=user_id)
        users = account_model.UserProfile.objects.filter(id=user_id)
        change_status_sidebar = 'user-management'

        variables = {
            'users': users,
            'change_status_sidebar': change_status_sidebar,
        }

        return render(request, self.template_name, variables)

    def post(self, request, user_id):
        pass


#active or deactive user
class ActiveDeactiveUser(StaffPermissionMixin, View):
    template_name = 'staff/active-deactive-user.html'

    def get(self, request, profile_status, user_id):

        get_object_or_404(account_model.UserProfile, pk=user_id)
        users = account_model.UserProfile.objects.filter(id=user_id)
        change_status_sidebar = 'user-management'

        variables = {
            'users': users,
            'profile_status': profile_status,
            'change_status_sidebar': change_status_sidebar,
        }

        return render(request, self.template_name, variables)

    def post(self, request, profile_status, user_id):
        get_object_or_404(account_model.UserProfile, pk=user_id)
        users = account_model.UserProfile.objects.filter(id=user_id)
        change_status_sidebar = 'user-management'

        if request.POST.get('yes') == 'yes':
            for user in users:
                if profile_status == 'activate':
                    user.is_active = True
                    user.save()
                elif profile_status == 'deactivate':
                    user.is_active = False
                    user.save()
            return redirect('staff:user-detail', user_id=user_id)

        elif request.POST.get('no') == 'no':
            return redirect('staff:user-detail', user_id=user_id)


        variables = {
            'users': users,
            'profile_status': profile_status,
            'change_status_sidebar': change_status_sidebar,
        }

        return render(request, self.template_name, variables)




#delete user
class DeleteUser(StaffPermissionMixin, View):
    template_name = 'staff/delete-user.html'

    def get(self, request, user_id):

        get_object_or_404(account_model.UserProfile, pk=user_id)
        users = account_model.UserProfile.objects.filter(id=user_id)
        change_status_sidebar = 'user-management'

        variables = {
            'users': users,
            'change_status_sidebar': change_status_sidebar,
        }

        return render(request, self.template_name, variables)

    def post(self, request, user_id):
        get_object_or_404(account_model.UserProfile, pk=user_id)
        users = account_model.UserProfile.objects.filter(id=user_id)
        change_status_sidebar = 'user-management'

        if request.POST.get('yes') == 'yes':
            users.delete()
            return redirect('staff:all-user')

        elif request.POST.get('no') == 'no':
            return redirect('staff:all-user')

        variables = {
            'users': users,
            'change_status_sidebar': change_status_sidebar,
        }

        return render(request, self.template_name, variables)



#edit user
class EditUser(StaffPermissionMixin, View):
    template_name = 'staff/user-edit.html'

    def get(self, request, user_id):

        get_object_or_404(account_model.UserProfile, pk=user_id)
        users = account_model.UserProfile.objects.filter(id=user_id)
        change_status_sidebar = 'user-management'

        profile_edit_form = account_form.ProfileEditForm(instance=account_model.UserProfile.objects.get(id=user_id))

        variables = {
            'users': users,
            'profile_edit_form': profile_edit_form,
            'change_status_sidebar': change_status_sidebar,
        }

        return render(request, self.template_name, variables)

    def post(self, request, user_id):
        get_object_or_404(account_model.UserProfile, pk=user_id)
        users = account_model.UserProfile.objects.filter(id=user_id)
        change_status_sidebar = 'user-management'

        profile_edit_form = account_form.ProfileEditForm(request.POST or None, instance=account_model.UserProfile.objects.get(id=user_id))

        if profile_edit_form.is_valid():
            profile_edit_form.save()

        variables = {
            'users': users,
            'profile_edit_form': profile_edit_form,
            'change_status_sidebar': change_status_sidebar,
        }

        return render(request, self.template_name, variables)



#change user password
class ChangeUserPassword(View):
    template_name = 'staff/change-user-password.html'

    def get(self, request, user_id):

        get_object_or_404(account_model.UserProfile, pk=user_id)
        users = account_model.UserProfile.objects.filter(id=user_id)
        change_status_sidebar = 'user-management'

        change_user_password = forms.ChangeUserPasswordForm()

        variables = {
            'users': users,
            'change_user_password': change_user_password,
            'change_status_sidebar': change_status_sidebar,
        }

        return render(request, self.template_name, variables)

    def post(self, request, user_id):
        get_object_or_404(account_model.UserProfile, pk=user_id)
        users = account_model.UserProfile.objects.filter(id=user_id)
        change_status_sidebar = 'user-management'

        change_user_password = forms.ChangeUserPasswordForm(request.POST or None)

        if change_user_password.is_valid():
            change_user_password.deploy(user_id)

        variables = {
            'users': users,
            'change_user_password': change_user_password,
            'change_status_sidebar': change_status_sidebar,
        }

        return render(request, self.template_name, variables)



#staff home
class ProductHome(StaffPermissionMixin, View):
    template_name = 'staff/product-home.html'

    def get(self, request):
        change_status_sidebar = 'product-management'

        variables = {
            'change_status_sidebar': change_status_sidebar,
        }

        return render(request, self.template_name, variables)




#staff home
class ProductAdd(StaffPermissionMixin, View):
    template_name = 'staff/product-add.html'

    def get(self, request):

        add_product_form = forms.ProductForm()
        change_status_sidebar = 'product-management'

        variables = {
            'add_product_form': add_product_form,
            'change_status_sidebar': change_status_sidebar,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        add_product_form = forms.ProductForm(request.POST or None, request.FILES)
        change_status_sidebar = 'product-management'

        if add_product_form.is_valid():
            add_product_form.deploy(request)

        variables = {
            'add_product_form': add_product_form,
            'change_status_sidebar': change_status_sidebar,
        }

        return render(request, self.template_name, variables)
