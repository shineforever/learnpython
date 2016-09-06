"""jsonp_demo_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from jsonp_demo_django_server import views as server_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # check查询的url,db_name:要查找的库，user_name:用户名，check_what:你要查询什么？ 统统交给demo3来处理
    url(
        r'^check/(?P<db_name>\w+)/(?P<user_name>\w+)/(?P<check_what>\w+)/callback=(?P<callback_name>\w+)',
        server_views.demo3
    ),
]
