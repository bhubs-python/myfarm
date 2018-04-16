from django.shortcuts import render, redirect
from django.views import View

from account import models as account_model


#permission mixin
class InvestorPermissionMixin(object):
    def has_permissions(self, request):
        return request.user.investor == True

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not self.has_permissions(request):
                return redirect('account:sign-in')
            return super(InvestorPermissionMixin, self).dispatch(
                request, *args, **kwargs)
        else:
            return redirect('account:sign-in')




#investor home
class Home(InvestorPermissionMixin, View):
    template_name = 'investor/index.html'

    def get(self, request):
        change_status_sidebar = 'dashboard'

        variables = {
            'change_status_sidebar': change_status_sidebar,
        }

        return render(request, self.template_name, variables)
