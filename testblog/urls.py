from django.urls import path
from .views import *

urlpatterns = [
    #path('',post_list,name='post-list'),
    path('list', post_list, name='post-list'),
    path('details/<int:post_id>', post_details, name='post-details'),
    path('category', category_list, name='category-list'),
    path('catdetail/<cat_name>', category_detail, name='cat-detail'),
    path('add', add_category, name='add-category'),
    path('author/add', author_add, name='author-add'),
    path('addpost', blog_add, name='blog-add'),
    path('search', blog_search, name='blog-search'),
    path('delete/<int:post_id>',delete_post,name='post-delete')
]