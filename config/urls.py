"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from accounts import account_views
from dof import dof_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', account_views.login_view, name='account_login'),
    path('logout/', account_views.logout_view, name='account_logout'),
    path('signup/', account_views.signup_view, name='account_signup'),
    path(
        'password/reset/',
        account_views.password_reset_view,
        name='account_reset_password'
    ),
    path(
        'password/reset/done/',
        account_views.password_reset_done_view,
        name='account_reset_password_done'
    ),
    re_path(
        r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        account_views.password_reset_from_key_view,
        name="account_reset_password_from_key"
    ),
    path('password/reset/key/done/', account_views.password_reset_from_key_done_view, name='account_reset_password_from_key_done'),
    path('mypage/', dof_views.mypage_view, name='mypage'),
    path('diagnosis/', dof_views.diagnosis_view, name='diagnosis'),
]
