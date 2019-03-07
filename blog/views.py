from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Pictures
from django.utils import timezone
from django.core.paginator import Paginator
from .form import BlogPost


# Create your views here.
def list(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request, 'list.html', { 'blogs' : blogs, 'posts':posts })

def home(request):
    blog = Pictures.objects

    return render(request, 'home.html', {'blog': blog})
    
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blog': blog_detail})

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('detail', str(blog.id))

def write(request):
    return render(request, 'write.html')


def blogpost(request):
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            psot.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'write.html', {'form':form})