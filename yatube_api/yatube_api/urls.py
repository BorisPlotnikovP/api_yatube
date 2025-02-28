from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from api.views import PostViewSet, GroupViewSet, CommentViewSet


router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
# 5a7c570f8fd0ad64bea757b33f7061379feb028d

post_router = routers.NestedSimpleRouter(router, 'posts', lookup='post')
post_router.register('comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/api-token-auth/', obtain_auth_token, name='get_token'),
    path('api/v1/', include(router.urls + post_router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
