from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Crop
from .forms import CropForm

from blogit.models import Post


def login(request):
    return render(request, 'login.html')

def index(request):
    posts = Post.published.all().order_by('-created_at')[:5]
    return render(request, 'index.html', locals())


@login_required
def user_home(request):
    """ homepage for a user after they've logged in """
    # crop = Crop.objects.get(user=request.user)
    return render(request, 'user_home.html', locals())

@login_required
def crop_form(request):
    crop, created = Crop.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        crop_data = request.POST.copy()
        crop_data['user'] = request.user
        form = CropForm(crop_data)
    else:
        form = CropForm(instance=crop)

    return render(request, 'crop_form.html', locals())

@login_required
def glean_list(request):
    return render(request, 'glean_list.html')
