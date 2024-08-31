from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/<str:username>/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('new/post/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<str:username>/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-edit'),
    path('post/<str:username>/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    # path('post/<str:username>/', views.UserPostListView.as_view(), name='user-posts'),
]
