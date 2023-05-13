from .models import Blogs
from django.db.models import Q
from django.core.paginator import Paginator


def search_blog(request):
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')

    blogs = Blogs.objects.filter(Q(title__iregex=search) | Q(description__iregex=search))

    return blogs, search


def paginate_blogs(request, blogs, results):
    page = request.GET.get('page', 1)
    paginator = Paginator(blogs, results)
    blogs = paginator.get_page(page)

    left_index = int(page) - 4

    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, blogs