from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField


class MentorProfile(models.Model):
    """Model for alumni who want to become mentors"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mentor_profile')
    expertise_areas = models.JSONField(default=list, help_text="List of expertise areas like ['Web Development', 'Data Science']")
    years_experience = models.IntegerField(help_text="Total years of professional experience")
    current_company = models.CharField(max_length=255)
    current_position = models.CharField(max_length=255)
    mentoring_capacity = models.IntegerField(default=3, help_text="Maximum number of mentees at one time")
    availability = models.JSONField(default=dict, help_text="Available time slots for mentoring")
    bio = models.TextField(help_text="Detailed bio and mentoring philosophy")
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    
    # Approval and status
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    approval_date = models.DateTimeField(null=True, blank=True)
    rejection_reason = models.TextField(blank=True, null=True)
    
    # Ratings and feedback
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    total_mentorships = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Mentor Profile"
        verbose_name_plural = "Mentor Profiles"
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.current_position}"
    
    def get_current_mentees_count(self):
        """Get current number of active mentees"""
        from cms.mentorship_models import MentorshipRequest
        return MentorshipRequest.objects.filter(mentor=self.user, status='accepted').count()

    def can_accept_more_mentees(self):
        """Check if mentor can accept more mentees"""
        return self.get_current_mentees_count() < self.mentoring_capacity


class MentorshipRequest(models.Model):
    """Model for mentorship requests from students to mentors"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]
    
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentorship_requests')
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentor_requests')
    
    # Request details
    goals = models.TextField(help_text="What the mentee wants to achieve")
    duration_months = models.IntegerField(default=3, help_text="Preferred mentorship duration in months")
    preferred_communication = models.CharField(max_length=50, choices=[
        ('video_calls', 'Video Calls'),
        ('messaging', 'Messaging'),
        ('in_person', 'In Person'),
        ('mixed', 'Mixed')
    ], default='mixed')
    
    # Status and timeline
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    requested_at = models.DateTimeField(auto_now_add=True)
    responded_at = models.DateTimeField(null=True, blank=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    # Response from mentor
    mentor_response = models.TextField(blank=True, null=True)
    rejection_reason = models.TextField(blank=True, null=True)
    
    # Progress tracking
    progress_percentage = models.IntegerField(default=0)
    mentee_rating = models.IntegerField(null=True, blank=True, choices=[(i, i) for i in range(1, 6)])
    mentor_rating = models.IntegerField(null=True, blank=True, choices=[(i, i) for i in range(1, 6)])
    mentee_feedback = models.TextField(blank=True, null=True)
    mentor_feedback = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Mentorship Request"
        verbose_name_plural = "Mentorship Requests"
    
    def __str__(self):
        return f"{self.mentee.first_name} → {self.mentor.first_name} ({self.status})"


class MentorshipSession(models.Model):
    """Model for individual mentorship sessions"""
    SESSION_TYPE_CHOICES = [
        ('video_call', 'Video Call'),
        ('phone_call', 'Phone Call'),
        ('in_person', 'In Person'),
        ('messaging', 'Messaging'),
        ('email', 'Email')
    ]
    
    mentorship = models.ForeignKey(MentorshipRequest, on_delete=models.CASCADE, related_name='sessions')
    session_date = models.DateTimeField()
    duration_minutes = models.IntegerField(default=60)
    session_type = models.CharField(max_length=20, choices=SESSION_TYPE_CHOICES, default='video_call')
    
    # Session content
    agenda = models.TextField(blank=True, null=True, help_text="Planned agenda for the session")
    notes = models.TextField(blank=True, null=True, help_text="Session notes and key points discussed")
    action_items = models.JSONField(default=list, help_text="List of action items for mentee")
    
    # Status
    completed = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    cancellation_reason = models.TextField(blank=True, null=True)
    
    # Meeting details
    meeting_link = models.URLField(blank=True, null=True, help_text="Video call link if applicable")
    location = models.CharField(max_length=255, blank=True, null=True, help_text="Physical location if in-person")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Mentorship Session"
        verbose_name_plural = "Mentorship Sessions"
        ordering = ['-session_date']
    
    def __str__(self):
        return f"Session: {self.mentorship.mentee.first_name} & {self.mentorship.mentor.first_name} - {self.session_date.strftime('%Y-%m-%d')}"
