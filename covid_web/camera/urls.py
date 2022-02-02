from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'cameras', views.CameraViewSet)
# router.register(r'images', views.ImageViewSet)

# app_name = 'camera'
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

app_name = 'camera'
urlpatterns = [
    path('cameras/', views.CameraList.as_view()),
    path('images/', views.ImageList.as_view()),
    path('cameraForm/', views.CameraForm.as_view(), name='cameraForm'),
    path('cameraForm/response', views.cameraAdd, name='cameraAdd'),
    path('cameraForm/response/delete', views.cameraDel, name='cameraDel'),
    # path('api/image/add', views.ImageAPIadd.as_view(), name='imageAdd'),
]