from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet
from rest_framework.authtoken.views import ObtainAuthToken

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>.+)/comments', CommentViewSet,
                basename='comments')
router.register(r'follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/api-token-auth/', ObtainAuthToken.as_view()),
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
