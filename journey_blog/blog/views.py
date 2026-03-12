from django.shortcuts import render, get_object_or_404
from .models import JourneyPost

def home(request):
    posts = JourneyPost.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(JourneyPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'pos': post})



# Create your views here.
