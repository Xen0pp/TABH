from rest_framework import serializers
from django.contrib.auth.models import User
from cms.mentorship_models import MentorProfile, MentorshipRequest, MentorshipSession


class UserBasicSerializer(serializers.ModelSerializer):
    """Basic user info for mentorship serializers"""
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class MentorProfileSerializer(serializers.ModelSerializer):
    user = UserBasicSerializer(read_only=True)
    current_mentees_count = serializers.SerializerMethodField()
    can_accept_mentees = serializers.SerializerMethodField()
    
    class Meta:
        model = MentorProfile
        fields = [
            'id', 'user', 'expertise_areas', 'years_experience', 
            'current_company', 'current_position', 'mentoring_capacity',
            'availability', 'bio', 'linkedin_url', 'github_url', 
            'portfolio_url', 'is_approved', 'is_active', 'average_rating',
            'total_mentorships', 'current_mentees_count', 'can_accept_mentees',
            'created_at'
        ]
        read_only_fields = [
            'is_approved', 'average_rating', 'total_mentorships', 
            'current_mentees_count', 'can_accept_mentees', 'created_at'
        ]
    
    def get_current_mentees_count(self, obj):
        return obj.get_current_mentees_count()
    
    def get_can_accept_mentees(self, obj):
        return obj.can_accept_more_mentees()


class MentorshipRequestSerializer(serializers.ModelSerializer):
    mentee = UserBasicSerializer(read_only=True)
    mentor = UserBasicSerializer(read_only=True)
    mentor_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = MentorshipRequest
        fields = [
            'id', 'mentee', 'mentor', 'mentor_id', 'goals', 'duration_months',
            'preferred_communication', 'status', 'requested_at', 'responded_at',
            'started_at', 'completed_at', 'mentor_response', 'rejection_reason',
            'progress_percentage', 'mentee_rating', 'mentor_rating',
            'mentee_feedback', 'mentor_feedback'
        ]
        read_only_fields = ['requested_at', 'responded_at', 'started_at', 'completed_at']
    
    def create(self, validated_data):
        mentor_id = validated_data.pop('mentor_id')
        mentor = User.objects.get(id=mentor_id)
        validated_data['mentor'] = mentor
        return super().create(validated_data)


class MentorshipSessionSerializer(serializers.ModelSerializer):
    mentorship = MentorshipRequestSerializer(read_only=True)
    mentorship_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = MentorshipSession
        fields = [
            'id', 'mentorship', 'mentorship_id', 'session_date', 'duration_minutes',
            'session_type', 'agenda', 'notes', 'action_items', 'completed',
            'cancelled', 'cancellation_reason', 'meeting_link', 'location',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
