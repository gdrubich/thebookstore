from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from books import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^booklist/', views.booklist, name='booklist'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
