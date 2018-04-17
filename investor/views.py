from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Q

from account import models as account_model

from . import forms


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




#==================================================================================
#==================================================================================
#                                credit
#==================================================================================
#==================================================================================



#credit home
class CreditHome(InvestorPermissionMixin, View):
    template_name = 'investor/credit-home.html'

    def get(self, request):
        change_status_sidebar = 'credit'

        my_wallet = account_model.Credit.objects.get(user=request.user)

        variables = {
            'change_status_sidebar': change_status_sidebar,

            'my_wallet': my_wallet,
        }

        return render(request, self.template_name, variables)



#credit home
class CreditRecharge(InvestorPermissionMixin, View):
    template_name = 'investor/credit-recharge.html'

    def get(self, request):
        change_status_sidebar = 'credit'
        
        recharge_form = forms.CreditRechargeForm()

        variables = {
            'change_status_sidebar': change_status_sidebar,

            'recharge_form': recharge_form,
        }

        return render(request, self.template_name, variables)


    def post(self, request):
        change_status_sidebar = 'credit'

        recharge_form = forms.CreditRechargeForm(request.POST or None)

        if recharge_form.is_valid():
            recharge_form.deploy(request)

        variables = {
            'change_status_sidebar': change_status_sidebar,

            'recharge_form': recharge_form,
        }

        return render(request, self.template_name, variables)




#pending recharge
class PendingRecharge(InvestorPermissionMixin, View):
    template_name = 'investor/pending-recharge.html'

    def get(self, request):
        change_status_sidebar = 'credit'

        pending_recharges = account_model.CreditRecharge.objects.filter(Q(user=request.user) & Q(status='pending'))

        variables = {
            'change_status_sidebar': change_status_sidebar,

            'pending_recharges': pending_recharges,
        }

        return render(request, self.template_name, variables)



#pending recharge
class PendingRechargeDetail(InvestorPermissionMixin, View):
    template_name = 'investor/pending-recharge-detail.html'

    def get(self, request, credit_recharge_id):
        pending_recharge = get_object_or_404(account_model.CreditRecharge, id=credit_recharge_id)

        change_status_sidebar = 'credit'

        variables = {
            'change_status_sidebar': change_status_sidebar,

            'pending_recharge': pending_recharge,
        }

        return render(request, self.template_name, variables)



#==================================================================================
#==================================================================================
#                                credit
#==================================================================================
#==================================================================================
