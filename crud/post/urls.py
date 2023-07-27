from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('list_post/', views.ListPostView.as_view(), name='list_post_view'),
    path('create_post/', views.CreatePostView.as_view(), name='create_post_view'),
    path('update_post/<int:pk>/', views.UpdatePostView.as_view(), name='update_post_view'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post_view')
]
