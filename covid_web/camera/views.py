from .models import Camera, Image
from login.models import User
from .serializers import CameraSerializer, ImageSerializer
from rest_framework import generics
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.http import HttpResponse

class CameraList(generics.ListCreateAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class CameraForm(TemplateView):
    template_name = "camera/cameraform.html"

def cameraAdd(request):
    try:
        username = request.session['username']
        user = User.objects.get(userName=username)

        cameraName = request.POST['cameraName']
        ipAddress = request.POST['ipAddress']
        oldCam = Camera.objects.get(cameraName=cameraName)
        oldCam = Camera.objects.get(ipAddress=ipAddress)

    except(Camera.DoesNotExist):
        newCamera = Camera(cameraName=cameraName, ipAddress=ipAddress, owner=user)
        newCamera.save()
        # should be success page
        return redirect('login:dashboard')

    else:
        response = "Camera IP already assigned.<a href=\"{% url 'login:dashboard' %}\"><button>Return to Dashboard</button></a>"
        return HttpResponse(response)

def cameraDel(request):
    try:
        username = request.session['username']
        user = User.objects.get(userName=username)

        cameraName = request.POST['cameraName']
        ipAddress = request.POST['ipAddress']
        oldCam = Camera.objects.get(ipAddress=ipAddress)

    except(Camera.DoesNotExist):
        newCamera = Camera(cameraName=cameraName, ipAddress=ipAddress, owner=user)
        newCamera.save()
        # should be success page
        return redirect('login:dashboard')

    else:
        response = "Camera IP already assigned."
        return HttpResponse(response)    
    

