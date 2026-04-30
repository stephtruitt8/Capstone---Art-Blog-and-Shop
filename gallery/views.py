from django.shortcuts import render

# Create your views here.
def gallery_view(request):
    return render(request, 'gallery/gallery.html')


def illustrations_view(request):
    return render(request, 'gallery/illustrations.html')

def sketches_view(request):
    return render(request, 'gallery/sketches.html')

def story_art_view(request):
    return render(request, 'gallery/story_art.html')