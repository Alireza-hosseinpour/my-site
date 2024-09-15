from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'
# setting a default router
router = DefaultRouter()
router.register('post', views.PostModelViewSet, basename='post')
router.register('category', views.CategoryModelViewSet, basename='category')

urlpatterns = router.urls

# urlpatterns = [
#     # path('posts/', views.postList, name='post-list'),
#     path('posts/', views.PostList.as_view(), name='post-list'),
#     path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
#     # path('posts/<int:id>/', views.postDetail, name='post-detail'),
#
# ]
