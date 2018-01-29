from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^userlist/$', views.userlist, name='userlist'),
    url(r'^userlist/edit_permission/$',
        views.edit_permission, name='edit_permission'),
    url(r'^booksearch/$', views.booksearch, name='booksearch'),
    url(r'^booklist/$', views.booklist, name='booklist'),
    url(r'^bookadmin/$', views.book_admin, name='book_admin'),
    url(r'^searchjson/$', views.searchjson, name="searchjson"),
    url(r'^searchperid/$', views.search_per_id, name="search_per_id"),
    url(r'^add_book/$', views.add_book, name='add_book'),
    url(r'^edit_book/$', views.edit_book, name='edit_book'),
    url(r'^delete_book/$', views.delete_book, name='delete_book'),
    url(r'author/(?P<author_pk>\d+)/$', views.author_detail, name='author_detail'),
]
