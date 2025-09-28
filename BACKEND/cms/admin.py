from django.contrib import admin
from cms.models import (
    Blog,
    Job,
    Role,
    NewsFeed,
    Event,
    Post,
    Comment,
    RegistrationRequest,
    AlumniVerificationScore
)
from cms.mentorship_models import MentorProfile, MentorshipRequest, MentorshipSession

# Register your models here.
admin.site.register(Blog)
admin.site.register(Job)
admin.site.register(Role)
admin.site.register(NewsFeed)
admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(RegistrationRequest)

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