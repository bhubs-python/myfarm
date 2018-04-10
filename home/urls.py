from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),

    url(r'^product/(?P<product_id>[0-9]+)/detail/$', views.ProductDetail.as_view(), name='product-detail'),


    url(r'^search/$', views.Search.as_view(), name='search'),
]
