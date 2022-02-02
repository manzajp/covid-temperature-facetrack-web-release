import ipaddress
from .models import Camera, Image
from login.models import User
from .serializers import CameraSerializer, ImageSerializer
from rest_framework import generics, views
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, request
from rest_framework.response import Response
from django.core.files.base import ContentFile
import base64

class CameraList(generics.ListCreateAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def post(self, request):
        try:
            imageName = request.POST['imageName'][len("uploads/"):]
            image64 = request.POST['image']
            ipAddress = request.POST['ipAddress']
            temp = request.POST['temp']
            camera = Camera.objects.get(ipAddress=ipAddress)
            
        except(Camera.DoesNotExist):
            print(request.META.get('REMOTE_ADDR'))
            return Response(data="Camera not registered to the system!", status=400)
        else:
            data = {
                'imageName':imageName, 
                'image':ContentFile(base64.b64decode(image64), name=imageName),
                'temp': temp,
                'camera':camera.id,
                }
            serializer = ImageSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=200)
            else:
                return Response(data=serializer.errors, status=400)

class CameraForm(TemplateView):
    template_name = "camera/cameraform.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(username=self.request.session['username'])
        return context

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

        camID = request.POST['id']
        cam = Camera.objects.get(id=camID)

    except(Camera.DoesNotExist):
        response = "Camera not found for deletion!<a href=\"{% url 'login:dashboard' %}\"><button>Return to Dashboard</button></a>"
        return HttpResponse(response)

    else:
        cam.delete()
        return redirect('login:dashboard')
