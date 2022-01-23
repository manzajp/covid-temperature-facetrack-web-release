from .models import Camera, Image
from login.models import User
from .serializers import CameraSerializer, ImageSerializer
from rest_framework import generics
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.files import ContentFile

import base64
def base64_to_image(base64_string):
    format, imgstr = base64_string.split(';base64,')
    ext = format.split('/')[-1]
    return ContentFile(base64.b64decode(imgstr), name=uuid4().hex + "." + ext)

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

# def cameraDel(request):
#     try:
#         username = request.session['username']
#         user = User.objects.get(userName=username)

#         cameraName = request.POST['cameraName']
#         ipAddress = request.POST['ipAddress']
#         oldCam = Camera.objects.get(ipAddress=ipAddress)

#     except(Camera.DoesNotExist):
#         newCamera = Camera(cameraName=cameraName, ipAddress=ipAddress, owner=user)
#         newCamera.save()
#         # should be success page
#         return redirect('login:dashboard')

#     else:
#         response = "Camera IP already assigned."
#         return HttpResponse(response)    

def imageAdd(request):
    try:
        username = request.session['username']
        user = User.objects.get(userName=username)

        ipAddress = request.POST['ipAddress']
        curCam = Camera.objects.get(ipAddress=ipAddress)

    except(Camera.DoesNotExist):
        response = "Camera IP is not registered.<a href=\"{% url 'login:dashboard' %}\"><button>Return to Dashboard</button></a>"
        return HttpResponse(response)

    else:
        newImage = Image(image=base64_to_image(request.POST['image64']), camera = curCam)
        newImage.save()
        return redirect('login:dashboard')
        