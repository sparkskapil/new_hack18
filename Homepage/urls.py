from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.home,name="index"),
    url(r'^Investor/$', views.investor,name="investor"),
    url(r'^Startup/$', views.startup,name="startup"),
    url(r'^Investor/Edit/',views.inv_edit,name="Edit Profile"),

    url(r'^Investor/logout/', views.inv_logout,name="investor logout"),
    url(r'^Startup/logout/', views.Startup_logout,name="startup logout"),
    url(r'^Startup/chat/', views.chatbot,name="Chat Ajax"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT);
