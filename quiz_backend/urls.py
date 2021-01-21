from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf.urls.static import static
from django.conf import settings
import rest_framework

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('', include('quiz.urls')),
]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
