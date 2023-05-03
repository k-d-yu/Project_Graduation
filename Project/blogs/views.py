from django.shortcuts import render, get_object_or_404
from .models import Blogs


def blogs(request):
    blogs = Blogs.objects.order_by("-date")
    context = {"blogs": blogs}
    return render(request, "blog/blogs.html", context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    context = {"blog": blog}
    return render(request, "blog/blog_detail.html", context)
