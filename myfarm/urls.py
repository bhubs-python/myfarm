from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^', include('home.urls', namespace='home')),

    #staff
    url(r'^staff/', include('staff.urls', namespace='staff')),

    #password reset
    url(r'^account/recover-password/$', auth_views.password_reset, {'template_name': 'account/password_reset.html', 'email_template_name': 'account/password_reset_email.html'}, name='password_reset'),
    url(r'^account/recover-password/done/$', auth_views.password_reset_done, {'template_name': 'account/password_reset_done.html'}, name='password_reset_done'),
    url(r'^account/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'template_name': 'account/password_reset_confirm.html'},name='password_reset_confirm'),
    url(r'^account/reset/done/$', auth_views.password_reset_complete, {'template_name': 'account/password_reset_complete.html'}, name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
