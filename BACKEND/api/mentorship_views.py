from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.utils import timezone
from cms.mentorship_models import MentorProfile, MentorshipRequest, MentorshipSession
from .serializers.mentorship_serializers import (
    MentorProfileSerializer, 
    MentorshipRequestSerializer, 
    MentorshipSessionSerializer
)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def mentor_profiles(request):
    """
    GET: List all approved mentors
    POST: Create mentor profile (apply to become mentor)
    """
    if request.method == 'GET':
        mentors = MentorProfile.objects.filter(is_approved=True, is_active=True)
        
        # Filter by expertise if provided
        expertise = request.GET.get('expertise')
        if expertise:
            mentors = mentors.filter(expertise_areas__icontains=expertise)
        
        # Filter by company if provided
        company = request.GET.get('company')
        if company:
            mentors = mentors.filter(current_company__icontains=company)
        
        serializer = MentorProfileSerializer(mentors, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # Check if user already has a mentor profile
        if hasattr(request.user, 'mentor_profile'):
            return Response(
                {'error': 'You already have a mentor profile'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = MentorProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def mentor_profile_detail(request, pk):
    """
    GET: Get mentor profile details
    PUT: Update mentor profile (only own profile)
    DELETE: Delete mentor profile (only own profile)
    """
    try:
        mentor_profile = MentorProfile.objects.get(pk=pk)
    except MentorProfile.DoesNotExist:
        return Response({'error': 'Mentor profile not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MentorProfileSerializer(mentor_profile)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        if mentor_profile.user != request.user:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = MentorProfileSerializer(mentor_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        if mentor_profile.user != request.user:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        
        mentor_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def mentorship_requests(request):
    """
    GET: List user's mentorship requests (as mentee or mentor)
    POST: Create new mentorship request
    """
    if request.method == 'GET':
        if hasattr(request.user, 'id') and request.user.id:
            user_type = request.GET.get('type', 'all')  # 'mentee', 'mentor', or 'all'
            
            if user_type == 'mentee':
                requests = MentorshipRequest.objects.filter(mentee=request.user)
            elif user_type == 'mentor':
                requests = MentorshipRequest.objects.filter(mentor=request.user)
            else:
                requests = MentorshipRequest.objects.filter(
                    Q(mentee=request.user) | Q(mentor=request.user)
                )
        else:
            # For testing, return all requests
            requests = MentorshipRequest.objects.all()
            
        serializer = MentorshipRequestSerializer(requests, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MentorshipRequestSerializer(data=request.data)
        if serializer.is_valid():
            # Check if mentor exists and is approved
            mentor_id = request.data.get('mentor_id')
            try:
                mentor_profile = MentorProfile.objects.get(user_id=mentor_id, is_approved=True)
                if not mentor_profile.can_accept_more_mentees():
                    return Response(
                        {'error': 'Mentor has reached maximum capacity'}, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
            except MentorProfile.DoesNotExist:
                return Response(
                    {'error': 'Mentor not found or not approved'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # For testing without authentication, use a default user
            if hasattr(request.user, 'id') and request.user.id:
                serializer.save(mentee=request.user)
            else:
                # Use first available user for testing (replace with actual logic)
                from django.contrib.auth.models import User
                test_user = User.objects.first()
                serializer.save(mentee=test_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def mentorship_request_detail(request, pk):
    """
    GET: Get mentorship request details
    PUT: Update mentorship request (accept/reject/update progress)
    """
    try:
        mentorship_request = MentorshipRequest.objects.get(pk=pk)
    except MentorshipRequest.DoesNotExist:
        return Response({'error': 'Mentorship request not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Check permissions
    if mentorship_request.mentee != request.user and mentorship_request.mentor != request.user:
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    
    if request.method == 'GET':
        serializer = MentorshipRequestSerializer(mentorship_request)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MentorshipRequestSerializer(mentorship_request, data=request.data, partial=True)
        if serializer.is_valid():
            # Handle status changes
            new_status = request.data.get('status')
            if new_status and new_status != mentorship_request.status:
                if new_status == 'accepted':
                    mentorship_request.responded_at = timezone.now()
                    mentorship_request.started_at = timezone.now()
                elif new_status == 'rejected':
                    mentorship_request.responded_at = timezone.now()
                elif new_status == 'completed':
                    mentorship_request.completed_at = timezone.now()
            
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
