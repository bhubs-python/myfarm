from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),


    url(r'^credit/home/$', views.CreditHome.as_view(), name='credit-home'),
    url(r'^credit/recharge/$', views.CreditRecharge.as_view(), name='credit-recharge'),
    url(r'^credit/recharge/pending/$', views.PendingRecharge.as_view(), name='pending-recharge'),
    url(r'^credit/recharge/pending/(?P<credit_recharge_id>[0-9]+)/$', views.PendingRechargeDetail.as_view(), name='pending-recharge-detail'),
]
