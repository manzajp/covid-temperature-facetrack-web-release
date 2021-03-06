from dataclasses import field
from statistics import mode
from rest_framework import serializers
from .views import Camera, Image

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ['cameraName', 'ipAddress']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['imageName', 'image', 'temp', 'camera']
