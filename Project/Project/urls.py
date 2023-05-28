from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from main import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('session/', views.session, name="session"),
    path('contacts/', views.contacts, name="contacts"),
    path('blog/', include("blogs.urls")),
    path('personal_account/', include("personal_account.urls")),
    path('reviews/', views.reviews, name="reviews"),
    path('reviews-delete/', views.reviews_delete, name="reviews_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
