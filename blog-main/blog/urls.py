from rest_framework import routers

from blog.views import BlogViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'blog', BlogViewSet, basename='blog-list')
router.register(r'post', PostViewSet, basename='post-list')
