"""src URL Configuration

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
from django.contrib.auth import views as auth_views
from django.urls import path, re_path, include
from . import views, forms

urlpatterns = [
    path('', include('FoodOrder.urls')),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('profile/', views.edit_profile, name='profile'),
    path('profile/password/', views.change_password, name="password"),

    re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name='profile/password_reset_form.html',
                                                                       subject_template_name=
                                                                       'profile/password_reset_subject.txt',
                                                                       email_template_name=
                                                                       'profile/password_reset_email.html',
                                                                       form_class=forms.PasswordReset),
            name='password_reset'),
    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='profile/password_reset_done.html'), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(template_name='profile/password_reset_confirm.html', form_class= forms.PasswordNew),
            name='password_reset_confirm'),
    re_path(r'^reset/done/$',
            auth_views.PasswordResetCompleteView.as_view(template_name='profile/password_reset_complete.html'),
            name='password_reset_complete'),

]
