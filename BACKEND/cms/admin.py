from django.contrib import admin
from cms.models import (
    Job,
    Role,
    NewsFeed,
    Event,
    Post,
    Comment,
    RegistrationRequest,
    AlumniVerificationScore,
    HostelRoom,
    HostelResident,
    HostelAnnouncement,
    GalleryCategory,
    GalleryTag,
    GalleryAlbum,
    GalleryImage,
    GalleryComment,
    GalleryLike
)
from cms.mentorship_models import MentorProfile, MentorshipRequest, MentorshipSession

# Register your models here.
admin.site.register(Job)
admin.site.register(Role)
admin.site.register(NewsFeed)
admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(RegistrationRequest)

# TABH-Specific Admin Configurations

@admin.register(HostelRoom)
class HostelRoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'room_type', 'capacity', 'current_occupancy', 'floor', 'is_available', 'monthly_rent']
    list_filter = ['room_type', 'floor', 'is_available', 'has_attached_bathroom']
    search_fields = ['room_number']
    ordering = ['floor', 'room_number']
    
    fieldsets = (
        ('Room Details', {
            'fields': ('room_number', 'room_type', 'capacity', 'floor')
        }),
        ('Amenities', {
            'fields': ('has_attached_bathroom', 'has_balcony')
        }),
        ('Availability & Pricing', {
            'fields': ('is_available', 'current_occupancy', 'monthly_rent')
        }),
    )

@admin.register(HostelResident)
class HostelResidentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'room', 'priority_category', 'status', 'admission_date']
    list_filter = ['priority_category', 'status', 'year_of_study', 'admission_date']
    search_fields = ['firstName', 'lastName', 'email', 'father_name', 'college_name']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('firstName', 'lastName', 'email', 'phone', 'address', 'avatar')
        }),
        ('Army Connection', {
            'fields': ('father_name', 'father_rank', 'father_unit', 'service_number', 'priority_category')
        }),
        ('Academic Information', {
            'fields': ('college_name', 'course', 'year_of_study', 'expected_graduation')
        }),
        ('Hostel Information', {
            'fields': ('room', 'admission_date', 'status')
        }),
        ('Local Guardian', {
            'fields': ('lg_name', 'lg_phone', 'lg_address', 'lg_relation')
        }),
        ('Documents', {
            'fields': ('admission_form', 'id_proof', 'medical_certificate')
        }),
        ('Financial', {
            'fields': ('security_deposit', 'monthly_charges')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(HostelAnnouncement)
class HostelAnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority', 'target_audience', 'is_active', 'publish_date', 'created_by']
    list_filter = ['priority', 'target_audience', 'is_active', 'publish_date']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Announcement Details', {
            'fields': ('title', 'content', 'priority', 'target_audience')
        }),
        ('Publishing', {
            'fields': ('is_active', 'publish_date', 'expiry_date')
        }),
        ('Metadata', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:  # If creating new announcement
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(AlumniVerificationScore)
class AlumniVerificationScoreAdmin(admin.ModelAdmin):
    list_display = [
        'email', 'total_score', 'verification_status', 
        'student_id_score', 'graduation_year_score', 
        'linkedin_score', 'document_score', 'created_at'
    ]
    list_filter = ['verification_status', 'total_score', 'graduation_year_score']
    search_fields = ['email', 'student_id', 'department']
    readonly_fields = ['total_score', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Alumni Information', {
            'fields': ('email', 'student_id', 'graduation_year', 'department', 'linkedin_profile')
        }),
        ('Verification Scores', {
            'fields': ('student_id_score', 'graduation_year_score', 'linkedin_score', 'document_score', 'total_score')
        }),
        ('Status', {
            'fields': ('verification_status', 'auto_approval_threshold')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        obj.calculate_total_score()
        super().save_model(request, obj, form, change)


@admin.register(MentorProfile)
class MentorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'current_position', 'current_company', 'is_approved', 'is_active', 'created_at']
    list_filter = ['is_approved', 'is_active', 'created_at']
    search_fields = ['user__first_name', 'user__last_name', 'user__email', 'current_company', 'current_position']
    readonly_fields = ['created_at', 'updated_at', 'total_mentorships', 'average_rating']
    
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'current_company', 'current_position', 'years_experience')
        }),
        ('Mentorship Details', {
            'fields': ('expertise_areas', 'mentoring_capacity', 'bio', 'availability')
        }),
        ('Social Links', {
            'fields': ('linkedin_url', 'github_url', 'portfolio_url')
        }),
        ('Approval Status', {
            'fields': ('is_approved', 'is_active', 'approval_date', 'rejection_reason')
        }),
        ('Statistics', {
            'fields': ('average_rating', 'total_mentorships', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['approve_mentors', 'reject_mentors']
    
    def approve_mentors(self, request, queryset):
        from django.utils import timezone
        queryset.update(is_approved=True, approval_date=timezone.now())
        self.message_user(request, f"Approved {queryset.count()} mentors.")
    approve_mentors.short_description = "Approve selected mentors"
    
    def reject_mentors(self, request, queryset):
        queryset.update(is_approved=False, approval_date=None)
        self.message_user(request, f"Rejected {queryset.count()} mentors.")
    reject_mentors.short_description = "Reject selected mentors"


@admin.register(MentorshipRequest)
class MentorshipRequestAdmin(admin.ModelAdmin):
    list_display = ['mentee', 'mentor', 'status', 'duration_months', 'requested_at', 'progress_percentage']
    list_filter = ['status', 'preferred_communication', 'duration_months', 'requested_at']
    search_fields = ['mentee__first_name', 'mentee__last_name', 'mentor__first_name', 'mentor__last_name']
    readonly_fields = ['requested_at', 'responded_at', 'started_at', 'completed_at']
    
    fieldsets = (
        ('Participants', {
            'fields': ('mentee', 'mentor')
        }),
        ('Request Details', {
            'fields': ('goals', 'duration_months', 'preferred_communication')
        }),
        ('Status & Timeline', {
            'fields': ('status', 'requested_at', 'responded_at', 'started_at', 'completed_at')
        }),
        ('Mentor Response', {
            'fields': ('mentor_response', 'rejection_reason')
        }),
        ('Progress & Feedback', {
            'fields': ('progress_percentage', 'mentee_rating', 'mentor_rating', 'mentee_feedback', 'mentor_feedback')
        }),
    )


@admin.register(MentorshipSession)
class MentorshipSessionAdmin(admin.ModelAdmin):
    list_display = ['mentorship', 'session_date', 'duration_minutes', 'session_type', 'completed', 'cancelled']
    list_filter = ['session_type', 'completed', 'cancelled', 'session_date']
    search_fields = ['mentorship__mentee__first_name', 'mentorship__mentor__first_name']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Session Info', {
            'fields': ('mentorship', 'session_date', 'duration_minutes', 'session_type')
        }),
        ('Content', {
            'fields': ('agenda', 'notes', 'action_items')
        }),
        ('Meeting Details', {
            'fields': ('meeting_link', 'location')
        }),
        ('Status', {
            'fields': ('completed', 'cancelled', 'cancellation_reason')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# Gallery Admin Configurations

@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_type', 'color_code', 'is_active', 'order', 'created_at']
    list_filter = ['category_type', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['order', 'name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(GalleryTag)
class GalleryTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'tag_type', 'is_featured', 'created_at']
    list_filter = ['tag_type', 'is_featured', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['tag_type', 'name']
    readonly_fields = ['created_at']


@admin.register(GalleryAlbum)
class GalleryAlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'is_featured', 'is_public', 'image_count', 'created_by', 'created_at']
    list_filter = ['is_featured', 'is_public', 'event_date', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['image_count', 'created_at', 'updated_at']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'album', 'category', 'event_date', 'priority', 'is_featured', 'view_count', 'uploaded_by']
    list_filter = ['priority', 'is_featured', 'is_public', 'category', 'event_date', 'created_at']
    search_fields = ['title', 'description', 'people_tagged', 'special_guests', 'event_location']
    readonly_fields = ['view_count', 'tag_list', 'created_at', 'updated_at']
    filter_horizontal = ['tags']
    
    actions = ['make_featured', 'make_public', 'make_private']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.uploaded_by = request.user
        super().save_model(request, obj, form, change)
    
    def make_featured(self, request, queryset):
        queryset.update(is_featured=True)
        self.message_user(request, f"Made {queryset.count()} images featured.")
    make_featured.short_description = "Mark selected images as featured"
    
    def make_public(self, request, queryset):
        queryset.update(is_public=True)
        self.message_user(request, f"Made {queryset.count()} images public.")
    make_public.short_description = "Make selected images public"
    
    def make_private(self, request, queryset):
        queryset.update(is_public=False)
        self.message_user(request, f"Made {queryset.count()} images private.")
    make_private.short_description = "Make selected images private"


@admin.register(GalleryComment)
class GalleryCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'comment_preview', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'created_at']
    search_fields = ['comment', 'user__username', 'image__title']
    readonly_fields = ['created_at', 'updated_at']
    
    def comment_preview(self, obj):
        return obj.comment[:50] + "..." if len(obj.comment) > 50 else obj.comment
    comment_preview.short_description = "Comment Preview"


@admin.register(GalleryLike)
class GalleryLikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'image__title']
    readonly_fields = ['created_at']
    
    def has_change_permission(self, request, obj=None):
        return False