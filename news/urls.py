"""news URL Configuration

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

# from django.urls import path
# from . import views

# #url conf
# urlpatterns=[
#     path('',views.welcome,name = 'welcome'),
#     path('today/',views.news_of_day,name='newsToday'),
#     path('archives/(\d{4}-\d{2}-\d{2})/',views.past_days_news,name = 'pastNews') #create new regex pattern to match the dates y-m-day  valid url 127.0.0.1:8000/news/archives/2017-02-04/ ...connect it to the past days news..will capture 2017-02-04 and send it to our view function. 
# ]
#    # /news/welcome/..use path fn to create url patter obj


from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path,path
from . import views

urlpatterns=[   
    path('',views.news_today,name='newsToday'), #ite root route.
    re_path('^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),  #create new regex pattern to match the dates y-m-day  valid url 127.0.0.1:8000/news/archives/2017-02-04/ ...connect it to the past days news..will capture 2017-02-04 and send it to our view function.
    path('search/', views.search_results, name='search_results'),
    path('article/(\d+)',views.article,name ='article'), # capture an integer which will be the id 
    path('new/article', views.new_article, name='new-article'),
    path('ajax/newsletter/', views.newsletter, name='newsletter'),
    path('api/merch/', views.MerchList.as_view()),
    re_path('api/merch/merch-id/(?P<pk>[0-9]+)/$',
        views.MerchDescription.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
