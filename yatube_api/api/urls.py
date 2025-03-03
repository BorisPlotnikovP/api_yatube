from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_nested import routers
from rest_framework.routers import SimpleRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet


router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

post_router = routers.NestedSimpleRouter(router, 'posts', lookup='post')
post_router.register('comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='get_token'),
    path('v1/', include(router.urls + post_router.urls)),
]
