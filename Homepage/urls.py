from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.home,name="index"),
    url(r'^Investor/$', views.investor,name="investor"),
    url(r'^Startup/$', views.startup,name="startup"),
    url(r'^Investor/logout', views.inv_logout,name="investor logout")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT);
