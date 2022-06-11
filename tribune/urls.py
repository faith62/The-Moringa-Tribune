"""tribune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('news/',include('news.urls')) # create a new regex and call the include function and pass in the news application URLconf. any url that start with news followed by /..include this routes..reference
# ]


from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('news.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/login.html')),
    path('tinymce/', include('tinymce.urls')),
    path('api-token-auth/', obtain_auth_token)
]


# urlpatterns = [
#     path('accounts/', include('django_registration.backends.one_step.urls')),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('accounts/profile/', auth_views.LoginView.as_view(template_name='user/profile.html')),
#     path('logout/', auth_views.LogoutView.as_view(template_name='registration/login.html')),
# ]
