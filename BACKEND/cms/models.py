from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import JSONField


# Create your models here.


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


# TABH-Specific Models for Hostel Management

class HostelRoom(models.Model):
    """Model for managing hostel rooms"""
    ROOM_TYPES = [
        ('single', 'Single Room'),
        ('double', 'Double Room (2 students)'),
        ('dormitory', 'Dormitory (4 students)'),
    ]
    
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES, default='double')
    capacity = models.IntegerField(default=2)
    current_occupancy = models.IntegerField(default=0)
    floor = models.IntegerField(default=1)
    has_attached_bathroom = models.BooleanField(default=True)
    has_balcony = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Room {self.room_number} - {self.get_room_type_display()}"
    
    @property
    def is_full(self):
        return self.current_occupancy >= self.capacity


class HostelResident(models.Model):
    """Model for current hostel residents (hostelers)"""
    PRIORITY_CHOICES = [
        ('priority_1', 'Priority I - Battle Casualties/Gallantry Awardees'),
        ('priority_2', 'Priority II - NCR Posted/Coaching'),
        ('priority_3', 'Priority III - Ex-Servicemen Sons'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active Resident'),
        ('on_leave', 'On Leave'),
        ('suspended', 'Suspended'),
        ('graduated', 'Graduated/Left'),
    ]
    
    # Personal Information
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    avatar = models.ImageField(upload_to='residents/', blank=True, null=True)
    
    # Army Connection
    father_name = models.CharField(max_length=255)
    father_rank = models.CharField(max_length=100)
    father_unit = models.CharField(max_length=255)
    service_number = models.CharField(max_length=50, blank=True, null=True)
    priority_category = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    
    # Academic Information
    college_name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    year_of_study = models.IntegerField()
    expected_graduation = models.DateField()
    
    # Hostel Information
    room = models.ForeignKey(HostelRoom, on_delete=models.SET_NULL, null=True, blank=True)
    admission_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    
    # Local Guardian
    lg_name = models.CharField(max_length=255, verbose_name="Local Guardian Name")
    lg_phone = models.CharField(max_length=20, verbose_name="Local Guardian Phone")
    lg_address = models.TextField(verbose_name="Local Guardian Address")
    lg_relation = models.CharField(max_length=100, verbose_name="Relation with Local Guardian")
    
    # Documents
    admission_form = models.FileField(upload_to='documents/admission/', blank=True, null=True)
    id_proof = models.FileField(upload_to='documents/id_proof/', blank=True, null=True)
    medical_certificate = models.FileField(upload_to='documents/medical/', blank=True, null=True)
    
    # Fees and Payments
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    monthly_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.firstName} {self.lastName} - Room {self.room.room_number if self.room else 'Unassigned'}"
    
    @property
    def full_name(self):
        return f"{self.firstName} {self.lastName}"


class HostelAnnouncement(models.Model):
    """Model for hostel announcements and notices"""
    PRIORITY_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_LEVELS, default='medium')
    target_audience = models.CharField(max_length=50, choices=[
        ('all', 'All Residents'),
        ('current', 'Current Residents Only'),
        ('alumni', 'Alumni Only'),
        ('specific', 'Specific Group'),
    ], default='all')
    
    is_active = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField(blank=True, null=True)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-priority', '-publish_date']
    
    def __str__(self):
        return f"{self.title} ({self.get_priority_display()})"


# Gallery Models for TABH Photo Management

class GalleryCategory(models.Model):
    """Categories for organizing gallery images"""
    CATEGORY_TYPES = [
        ('festivals', 'Festivals & Celebrations'),
        ('officers', 'Special Officers & Visitors'),
        ('events', 'Hostel Events'),
        ('daily_life', 'Daily Life'),
        ('sports', 'Sports & Recreation'),
        ('academic', 'Academic Activities'),
        ('infrastructure', 'Infrastructure & Facilities'),
        ('alumni', 'Alumni Visits'),
    ]
    
    name = models.CharField(max_length=100)
    category_type = models.CharField(max_length=20, choices=CATEGORY_TYPES)
    description = models.TextField(blank=True, null=True)
    color_code = models.CharField(max_length=7, default='#dc2626', help_text="Hex color code for category")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text="Display order")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Gallery Categories"
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_type_display()})"


class GalleryTag(models.Model):
    """Tags for gallery images (festivals, people, events, etc.)"""
    TAG_TYPES = [
        ('festival', 'Festival'),
        ('person', 'Person'),
        ('event', 'Event'),
        ('location', 'Location'),
        ('activity', 'Activity'),
        ('general', 'General'),
    ]
    
    name = models.CharField(max_length=50)
    tag_type = models.CharField(max_length=20, choices=TAG_TYPES, default='general')
    description = models.TextField(blank=True, null=True)
    is_featured = models.BooleanField(default=False, help_text="Show in featured tags")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['tag_type', 'name']
        unique_together = ['name', 'tag_type']
    
    def __str__(self):
        return f"{self.name} ({self.get_tag_type_display()})"


class GalleryAlbum(models.Model):
    """Albums to group related gallery images"""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='gallery/albums/covers/', blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-event_date', '-created_at']
    
    def __str__(self):
        return self.title
    
    @property
    def image_count(self):
        return self.images.count()


class GalleryImage(models.Model):
    """Main model for gallery images"""
    PRIORITY_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('featured', 'Featured'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='gallery/images/')
    thumbnail = models.ImageField(upload_to='gallery/thumbnails/', blank=True, null=True)
    
    # Organization
    album = models.ForeignKey(GalleryAlbum, on_delete=models.CASCADE, related_name='images', blank=True, null=True)
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(GalleryTag, blank=True)
    
    # Event details
    event_date = models.DateField(help_text="Date when the photo was taken")
    event_location = models.CharField(max_length=200, blank=True, null=True)
    
    # People in photo
    people_tagged = models.TextField(blank=True, null=True, help_text="Names of people in the photo (comma separated)")
    special_guests = models.TextField(blank=True, null=True, help_text="Special officers/visitors in the photo")
    
    # Display settings
    priority = models.CharField(max_length=10, choices=PRIORITY_LEVELS, default='medium')
    is_public = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    show_on_homepage = models.BooleanField(default=False)
    
    # Metadata
    photographer = models.CharField(max_length=100, blank=True, null=True)
    camera_details = models.CharField(max_length=200, blank=True, null=True)
    view_count = models.IntegerField(default=0)
    
    # Management
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-priority', '-event_date', '-created_at']
    
    def __str__(self):
        return self.title
    
    def increment_view_count(self):
        """Increment view count when image is viewed"""
        self.view_count += 1
        self.save(update_fields=['view_count'])
    
    @property
    def tag_list(self):
        """Return comma-separated list of tag names"""
        return ", ".join([tag.name for tag in self.tags.all()])


class GalleryComment(models.Model):
    """Comments on gallery images"""
    image = models.ForeignKey(GalleryImage, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    is_approved = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.image.title}"


class GalleryLike(models.Model):
    """Likes for gallery images"""
    image = models.ForeignKey(GalleryImage, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['image', 'user']
    
    def __str__(self):
        return f"{self.user.username} likes {self.image.title}"


# Import mentorship models
from .mentorship_models import MentorProfile, MentorshipRequest, MentorshipSession