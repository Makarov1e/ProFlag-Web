from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('search.urls')),
    path('search/', include('search.urls')),
    path('login/', include('login.urls'))


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

