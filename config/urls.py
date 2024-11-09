from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.catalog.urls', namespace='catalog')),
    path('security/', include('core.security.urls', namespace='security')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
