from django.shortcuts import render, get_object_or_404
from .models import service_model, blog_model

# Create your views here.
def detail_service(request):
    return render(request, 'detail-service.html')

def home_page(req): 
    services = service_model.objects.all()[:3]
    blogs = blog_model.objects.all()[:3]
    context = {
        'services': services,
        'blogs': blogs
    }
    return render(req, 'index.html', context)

def our_service(req):
    services = service_model.objects.all()
    context = {
        'services': services
    }
    return render(req, 'our-service.html', context)

def our_blog(req):
    blogs = blog_model.objects.all()
    context = {
        'blogs': blogs
    }
    return render(req, 'our-blog.html', context)

def faq(req):
    return render(req, 'faq.html')

def ourteam(req):
    return render(req, 'ourteam.html')

def tac(req):
    return render(req, 'tac.html')

def detail_blog(req, id):
    blog = get_object_or_404(blog_model, id=id)
    blogs = blog_model.objects.all()[:3]
    context = {
        'blog': blog,
        'blogs': blogs
    }
    return render(req, 'detailblog.html', context)

def about_us(req):
    return render(req, 'about.html')

def contact_us(req):
    return render(req, 'contact.html')