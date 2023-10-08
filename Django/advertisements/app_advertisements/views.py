from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .models import Advertisement
from .forms import AdvertisementForms
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    advertisements=Advertisement.objects.all()
    context={'advertisements':advertisements}
    return render(request, 'app_advertisements/index.html', context)

def top_sellers(request):
    return render(request, 'app_advertisements/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
def adv_post(request):
    if request.method=="POST":
        form=AdvertisementForms(request.POST, request.FILES)
        if form.is_valid():
            advertisement=Advertisement(**form.cleaned_data)
            advertisement.user=request.user
            advertisement.save()
            url=reverse('main_page')
            return redirect (url)
    else:
        form=AdvertisementForms()
    context={'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)
