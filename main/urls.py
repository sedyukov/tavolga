from django.urls import path

from .views import index_main, index_authors, index_author, index_about, index_news, index_new, index_numbers, \
    index_number, index_serch_result, index_search

urlpatterns = [
    path('', index_main, name='index_main'),
    path('numbers/', index_numbers, name='index_numbers'),
    path('number/<int:number_id>/', index_number, name='index_number'),
    path('authors/', index_authors, name='index_main'),
    path('author/<int:author_id>/', index_author, name='index_auth'),
    path('about/', index_about, name='index_about'),
    path('news/', index_news, name='index_news'),
    path('search/', index_search, name='index_search'),
    path('search/res/', index_serch_result, name='index_serch_result'),
    path('new/<int:new_id>/', index_new, name='index_new'),

]
