
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from .views import email_template




urlpatterns = [
    path("email/", email_template, name="email_template"),
    path('admin/', admin.site.urls),
    path('archimatch_app/', include("archimatch_app.urls")),
    path('schema/', SpectacularAPIView.as_view(),name="schema"),
    path('',SpectacularSwaggerView.as_view(url_name="schema"))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
