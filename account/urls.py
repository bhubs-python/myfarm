from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sign-out/$', views.signout_request, name='sign-out'),
    url(r'^sign-up/$', views.SignUp.as_view(), name='sign-up'),
    url(r'^sign-in/$', views.SignIn.as_view(), name='sign-in'),

    url(r'^profile/$', views.Profile.as_view(), name='profile'),
    url(r'^profile/edit/$', views.ProfileEdit.as_view(), name='profile-edit'),
    url(r'^change-password/$', views.ChangePassword.as_view(), name='change-password'),

    #api
    url(r'^api/user-profile/$', views.UserProfileAPI.as_view(), name='user-profile-api'),
]
