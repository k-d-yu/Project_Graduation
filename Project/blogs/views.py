from django.shortcuts import render, get_object_or_404
from .models import Blogs
from .utils import search_blog, paginate_blogs


def blogs(request):
    blogs, search = search_blog(request)
    custom_range, blogs = paginate_blogs(request, blogs, 3)

    context = {"blogs": blogs,
               'search': search,
               'custom_range': custom_range}

    return render(request, "blog/blogs.html", context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    context = {"blog": blog}
    return render(request, "blog/blog_detail.html", context)
