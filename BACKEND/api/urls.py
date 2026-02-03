from django.urls import path, include
from rest_framework import routers  # type: ignore
from .views import JobViewSet, EventViewSet, NewsFeedViewSet,PostViewSet, CommentListGetCreateView, RegistrationRequestView, gallery_images, gallery_categories, gallery_tags

router = routers.DefaultRouter()

router.register(r"jobs", JobViewSet, "jobs")
router.register(r"events", EventViewSet, basename="events")
router.register(r"newsfeeds", NewsFeedViewSet, basename="newsfeeds")
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"registration-requests", RegistrationRequestView, "RegistrationRequests")
# router.register(r"approve", RegistrationRequestView.approve(), "approve")
# router.register(r"user", UserViewSet, "user")


urlpatterns = [
    # path('', views.blog_list, name='blog_list'),
    path("", include(router.urls)),
    path('posts/<int:post_id>/comments/', CommentListGetCreateView.as_view(), name='comment-list-create'),
    
    # Gallery API URLs
    path('gallery/images/', gallery_images, name='gallery-images'),
    path('gallery/categories/', gallery_categories, name='gallery-categories'),
    path('gallery/tags/', gallery_tags, name='gallery-tags'),
    
    # Mentorship System URLs
    path('mentorship/', include('api.mentorship_urls')),
]
