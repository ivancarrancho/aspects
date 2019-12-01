from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        '',
        TemplateView.as_view(template_name='home.html'),
        name='home',
    ),

    path(
        'app/',
        include('app.urls', namespace='app')
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
