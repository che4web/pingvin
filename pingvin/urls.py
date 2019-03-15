"""pingvin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
#from raccoonapp.views import RacconList,crt_view
from raccoonapp.views import home_view, RaccoonListView,RaccoonDetailView,RaccoonUpdateView
urlpatterns = [
 #   url(r'^',crt_view),
#    url(r'^admin/r',RacconList.as_view()),
    url(r'^admin/', admin.site.urls),
    #url(r'^$',home_view),
    url(r'^raccoon/(?P<pk>\d+)/$',RaccoonDetailView.as_view(),name="raccoon-detail"),
    url(r'^raccoon/(?P<pk>\d+)/edit/$',RaccoonUpdateView.as_view(),name="raccoon-update"),
    url(r'^$',RaccoonListView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
