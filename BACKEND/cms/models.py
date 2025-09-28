from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import JSONField


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.title


class Job(models.Model):
    FULL_TIME = "Full-Time"
    PART_TIME = "Part-Time"
    REMOTE = "Remote"
    INTERN = "Intern"

    JOB_TYPE_CHOICES = [
        (FULL_TIME, "Full-Time"),
        (PART_TIME, "Part-Time"),
        (REMOTE, "Remote"),
        (INTERN, "Intern"),
    ]
    job_title = models.CharField(max_length=255, default="")
    company = models.CharField(max_length=255, null=True, blank=True, default="")
    location = models.CharField(max_length=255, null=True, blank=True, default="")
    description = models.TextField(default="")
    posted_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    jobType = models.CharField(
        choices=JOB_TYPE_CHOICES, max_length=50, default="Full-Time"
    )
    deadline = models.DateTimeField(default=timezone.now, null=True, blank=True)
    experience = models.IntegerField(default=0, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    email = models.EmailField(null=True, blank=True, default="")

    def __str__(self):
        return self.job_title


class Role(models.Model):
    role_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.role_name


class NewsFeed(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Event(models.Model):
    event_name = models.CharField(max_length=255)
    date = models.DateTimeField()
    event_type = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)

    def __str__(self):
        return self.event_name


class Post(models.Model):
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="owner")

    def __str__(self):
        return self.post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"


class RegistrationRequest(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(unique=False)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    avatar = models.ImageField(upload_to='profiles/', blank=True, null=True)
    graduationYear = models.IntegerField()
    batch = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    studentId = models.CharField(max_length=255)
    currentCompany = models.CharField(max_length=255, blank=True, null=True)
    currentPosition = models.CharField(max_length=255, blank=True, null=True)
    experience = models.IntegerField()
    skills = JSONField(null=True, blank=True, default=list)
    interests = JSONField(null=True, blank=True, default=list)
    achievements = models.TextField(null=True, blank=True, default="")
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    cv = models.ImageField(upload_to='documents/', blank=True, null=True)
    proofDocument = models.ImageField(upload_to='documents/', blank=True, null=True)
    isApproved = models.BooleanField(default=False)
    rejectionReason = models.TextField(blank=True, null=True, default="")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName} - {self.email}"


class AlumniVerificationScore(models.Model):
    """Model to track alumni verification scoring"""
    email = models.EmailField()
    student_id = models.CharField(max_length=50)
    graduation_year = models.IntegerField()
    department = models.CharField(max_length=100)
    linkedin_profile = models.URLField(blank=True, null=True)
    
    # Scoring fields
    student_id_score = models.IntegerField(default=0)  # 0-2 points
    graduation_year_score = models.IntegerField(default=0)  # 0-2 points
    linkedin_score = models.IntegerField(default=0)  # 0-2 points
    document_score = models.IntegerField(default=0)  # 0-2 points
    total_score = models.IntegerField(default=0)  # Total out of 8
    
    # Status tracking
    verification_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending Verification'),
        ('auto_approved', 'Auto Approved'),
        ('manual_review', 'Manual Review Required'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='pending')
    
    auto_approval_threshold = models.IntegerField(default=5)  # Score needed for auto-approval
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def calculate_total_score(self):
        """Calculate total verification score"""
        self.total_score = (
            self.student_id_score + 
            self.graduation_year_score + 
            self.linkedin_score + 
            self.document_score
        )
        return self.total_score
    
    def is_auto_approvable(self):
        """Check if alumni meets auto-approval criteria"""
        return self.calculate_total_score() >= self.auto_approval_threshold
    
    def __str__(self):
        return f"{self.email} - Score: {self.total_score}/8"


# Import mentorship models
from .mentorship_models import MentorProfile, MentorshipRequest, MentorshipSession