from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'camera'
urlpatterns = [
	path('upload', upload, name = 'upload'),
	path('views', ImageView.as_view(), name = 'views'),
	path('success', success, name = 'success'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
