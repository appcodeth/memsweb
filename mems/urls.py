from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.http import HttpResponse

SITEMAPS = {}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', include('app.urls', namespace='app')),
    url(r'^robots.txt$', lambda r: HttpResponse('User-agent: *\nDisallow: /', content_type='text/plain')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = 'MEMs'
admin.site.site_header = 'MEMs Administrator'
