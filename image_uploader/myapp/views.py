from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import ImageUpload

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')  # Reload the same page to show the updated image grid
    else:
        form = ImageUploadForm()

    # Get all the images to display in the grid
    images = ImageUpload.objects.all()

    return render(request, 'upload_image.html', {'form': form, 'images': images})
