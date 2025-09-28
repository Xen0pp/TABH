from django.urls import path
from . import mentorship_views

urlpatterns = [
    # Mentor Profile endpoints
    path('mentors/', mentorship_views.mentor_profiles, name='mentor-profiles'),
    path('mentors/<int:pk>/', mentorship_views.mentor_profile_detail, name='mentor-profile-detail'),
    
    # Mentorship Request endpoints
    path('mentorship-requests/', mentorship_views.mentorship_requests, name='mentorship-requests'),
    path('mentorship-requests/<int:pk>/', mentorship_views.mentorship_request_detail, name='mentorship-request-detail'),
]
