from django.urls import path
from .views import HomePageView
from . import views


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    
    path('categories/', views.category_list,name='category_list'),

    path('categories/new', views.new_category, name='new_category'),

    path('categories/<int:category_id>', views.category_detail, name='category_detail'),
  
    path('categories/<int:category_id>/edit', views.category_detail, name='edit_category'),

    path('categories/<int:category_id>/delete', views.delete_category, name='delete_category'),
    path('categories/<int:category_id>/posts/<int:post_id>', views.post_detail, name='post_detail'),
]