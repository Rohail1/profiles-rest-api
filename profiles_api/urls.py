from django.urls import path, include
from profiles_api.views import HelloApiView, HelloViewSet, UserProfileViewSet, \
    UserLoginApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello')
router.register('profile', UserProfileViewSet)

urlpatterns = [
    path('hello/', HelloApiView.as_view()),
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls)),
]