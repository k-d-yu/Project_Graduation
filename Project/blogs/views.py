from django.shortcuts import render, get_object_or_404
from .models import Blogs


def blogs(request):
    blogs = Blogs.objects.order_by("-date")
    return render(request, "blog/blogs.html", {"blogs": blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, "blog/blog_detail.html", {"blog": blog})
