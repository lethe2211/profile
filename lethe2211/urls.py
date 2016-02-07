from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'lethe2211.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('introduction.urls', namespace='introduction')),    
    url(r'^introduction/', include('introduction.urls', namespace='introduction')),
]

