from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from .models import Image

from .forms import *

class ImageView(generic.ListView):
    template_name = 'camera_management/imageView.html'

    def get_queryset(self):
        return Image.objects.all()

def upload(request):

	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('camera:success')
	else:
		form = ImageForm()
	return render(request, 'camera_management/importForm.html', {'form' : form})


def success(request):
	return HttpResponse('successfully uploaded')

