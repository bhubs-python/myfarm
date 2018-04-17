from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),

    #user management url
    url(r'^user/home/$', views.UserHome.as_view(), name='user-home'),
    url(r'^user/all/$', views.AllUser.as_view(), name='all-user'),
    url(r'^user/detail/(?P<user_id>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),

    url(r'^user/(?P<profile_status>[a-zA-z]+)/(?P<user_id>[0-9]+)/$', views.ActiveDeactiveUser.as_view(), name='active-deactive-user'),
    url(r'^user/(?P<user_id>[0-9]+)/delete/$', views.DeleteUser.as_view(), name='delete-user'),
    url(r'^user/(?P<user_id>[0-9]+)/change-password/$', views.ChangeUserPassword.as_view(), name='change-user-password'),

    url(r'^user/(?P<user_id>[0-9]+)/edit/$', views.EditUser.as_view(), name='edit-user'),


    #product block start
    url(r'^product/home/$', views.ProductHome.as_view(), name='product-home'),
    url(r'^product/add/$', views.ProductAdd.as_view(), name='product-add'),

    #product block end

    #payment block start
    url(r'^payment/home/$', views.PaymentHome.as_view(), name='payment-home'),
    url(r'^payment/pending/recharge/$', views.PaymentPendingRecharge.as_view(), name='payment-pending-recharge'),
    url(r'^payment/pending/recharge//$', views.PaymentPendingRecharge.as_view(), name='payment-pending-recharge'),
    url(r'^payment/recharge/pending/(?P<credit_recharge_id>[0-9]+)/$', views.PendingRechargeDetail.as_view(), name='payment-pending-recharge-detail'),
    #url(r'^product/add/$', views.ProductAdd.as_view(), name='product-add'),

    #payment block end

]
