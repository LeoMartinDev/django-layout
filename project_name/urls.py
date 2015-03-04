from django.conf.urls import url, include, static
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # (r'', include('{{ project_name }}.apps.')),

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static.static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
