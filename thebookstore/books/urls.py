from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^userlist/$', views.userlist, name='userlist'),
    url(r'^userlis/edit_permission/$',
        views.edit_permission, name='edit_permission'),
    url(r'^booklist/', views.booklist, name='booklist'),
    url(r'author/(?P<author_pk>\d+)/$', views.author_detail, name='author_detail'),
]
