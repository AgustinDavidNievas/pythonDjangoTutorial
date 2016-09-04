"""pruebaDj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include
#from django.conf.urls import patterns
from django.contrib import admin

from polls import views
#from pruebaDj.polls import views#me parece que pasa lo mismo que con los paths del admin u_u

admin.autodiscover()#En el tutorial le agrega esto...

urlpatterns = [
    url(r'^admin/', admin.site.urls),#Por defecto estaba esto solo
    #url(r'^polls/', include('pruebaDj.pruebaDj.urls')),#Esta linea rompe por el path, recursividad infinita o no encuentra el modulo
    url(r'^polls', views.index, name='index'),
    
    # ex: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
]
