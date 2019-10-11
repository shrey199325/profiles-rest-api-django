from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(prefix="hello-viewset", viewset=views.HelloViewSet,
                basename="hello-viewset")
router.register("profile", views.UserProfileViewSet)
router.register("feed", views.UserProfileFeedViewSet)


urlpatterns = [
    path("Hello-view/", views.HelloAPIView.as_view()),
    path("", include(router.urls)),
    path("login/", views.UserLoginAPIView.as_view()),
]
