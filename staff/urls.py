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

]
