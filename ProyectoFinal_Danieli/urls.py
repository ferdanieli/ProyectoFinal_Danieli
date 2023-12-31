from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from blog.views import show_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_html),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('mensajes/', include('mensajes.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)