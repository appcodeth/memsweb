from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, re_path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

SITEMAPS = {}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include(('app.urls', 'app'), namespace='app')),
    re_path(r'^robots.txt$', lambda r: HttpResponse('User-agent: *\nDisallow: /', content_type='text/plain')),
    re_path(r'^sitemap.xml$', sitemap, {'sitemaps': SITEMAPS}, name='sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = 'MEMs'
admin.site.site_header = 'MEMs Administrator'
