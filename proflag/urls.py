from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('search.urls')),
    path('search/', include('search.urls')),
    path('login/', include('login.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', views.register_request, name="register"),
    path('accounts/profile/', views.profile_request, name="profile"),
    path('accounts/change_password/', views.change_password, name="change-password")
]