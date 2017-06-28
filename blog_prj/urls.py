from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from .settings import MEDIA_ROOT


urlpatterns = [
    # Examples:
    # url(r'^$', 'blog_prj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),






]
