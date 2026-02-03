from rest_framework import viewsets, permissions, filters, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import LimitOffsetPagination

from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import CharFilter, NumberFilter

from .serializers import serializers
from .serializers.serializers import RegistrationRequestSerializer
from cms.models import (
    Job, Event, NewsFeed, Post, Comment, RegistrationRequest, 
    AlumniVerificationScore, Role, GalleryImage, GalleryCategory, 
    GalleryTag, GalleryAlbum
)
from authorization.models import UserInfo
from authorization.serializer import UserInfoSerializer
from authorization.views import AlumniVerificationService

import json

class RegistrationRequestFilter(FilterSet):
    # To enable substring filtering (icontains) across multiple fields, you can define a custom FilterSet with CharFilter for each field, specifying the lookup_expr='icontains'. This allows you to filter multiple fields based on partial matches.

    first_name = CharFilter(field_name="first_name", lookup_expr="icontains")
    last_name = CharFilter(field_name="last_name", lookup_expr="icontains")
    email = CharFilter(field_name="email", lookup_expr="icontains")

    class Meta:
        model = RegistrationRequest
        fields = ["first_name", "last_name", "email"]


# Create your views here.




class JobFilter(FilterSet):
    min_salary = NumberFilter(field_name="salary", lookup_expr="gte")
    max_salary = NumberFilter(field_name="salary", lookup_expr="lte")
    min_experience = NumberFilter(field_name="experience", lookup_expr="gte")
    max_experience = NumberFilter(field_name="experience", lookup_expr="lte")

    class Meta:
        model = Job
        fields = {
            "jobType",
            "location",
            "company",
        }


class JobViewSet(viewsets.GenericViewSet):
    """
    ViewSet for managing job postings.
    """

    queryset = Job.objects.all().order_by("-posted_date")
    pagination_class = LimitOffsetPagination
    serializer_class = serializers.JobSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "id"
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = ["job_title", "company", "description", "location"]
    # filterset_class = JobFilter
    filterset_fields = {
        "jobType": ["iexact"],
        "location": ["iexact"],
        "company": ["iexact"],
    }
    ordering_fields = ["posted_date", "salary", "experience", "job_title"]
    ordering = ["-posted_date"]  # Default ordering by posted date, descending

    def list(self, request):
        """
        List all job postings.
        """
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)
        paginated_queryset = self.paginate_queryset(filtered_queryset)

        if paginated_queryset is not None:
            serializer = self.get_serializer(paginated_queryset, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response({"status": status.HTTP_200_OK, "results": serializer.data})

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a specific job posting.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({"status": status.HTTP_200_OK, "result": serializer.data})

    def create(self, request, *args, **kwargs):
        """
        Create a new job posting.
        """
        if request.user.is_authenticated:

          
            user = request.user
            user_info = UserInfo.objects.get(user=user)

            if user_info.role.id == 1:
                return Response(
                    {
                        "status": status.HTTP_401_UNAUTHORIZED,
                        "message": "You are not authorized to Create this job",
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # headers = self.get_success_headers(serializer.data)
            return Response(
                {
                    "message": "Job created successfully",
                    "status": status.HTTP_201_CREATED,
                    "result": serializer.data,
                }
            )

        else:
            
            return Response(
                {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "You are not authorized to Create this job",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

    def update(self, request, *args, **kwargs):
        """
        Update an existing job posting.
        """
        if request.user.is_authenticated:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "result": serializer.data})
        else:
            return Response(
                {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "You are not authorized to Update this job",
                }
            )

    def destroy(self, request, *args, **kwargs):
        """
        Delete a job posting.
        """
        if request.user.is_authenticated:
            instance = self.get_object()
            instance.delete()
            return Response(
                {"status": status.HTTP_200_OK, "result": "Job deleted successfully"}
            )
        else:
            return Response(
                {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "You are not authorized to delete this job",
                }
            )


class EventViewSet(viewsets.GenericViewSet):
    """
    ViewSet for managing events.
    """

    queryset = Event.objects.all().order_by("-date")  # Default ordering by event date
    pagination_class = LimitOffsetPagination
    serializer_class = serializers.EventSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "id"
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Searchable fields
    search_fields = ["event_name", "description", "location", "event_type"]

    # Filterable fields
    filterset_fields = {
        "event_type": ["iexact"],  # Case-insensitive exact match for event type
        "location": ["iexact"],  # Case-insensitive exact match for location
    }

    # Fields allowed for ordering
    ordering_fields = ["date", "event_name", "event_type", "location"]
    ordering = ["-date"]  # Default ordering by descending event date

    def list(self, request, *args, **kwargs):
        """
        List all events.
        """
        queryset = self.filter_queryset(self.get_queryset()).order_by("-id")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"status": status.HTTP_200_OK, "results": serializer.data})

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a specific event.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({"status": status.HTTP_200_OK, "result": serializer.data})

    def create(self, request, *args, **kwargs):
        """
        Create a new event.
        """
        if request.user.is_authenticated:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {"status": status.HTTP_201_CREATED, "result": serializer.data}
            )
        else:
            return Response(
                {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "error": "You are not authorized to Create this Event",
                }
            )

    def update(self, request, *args, **kwargs):
        """
        Update an existing event.
        """
        if request.user.is_authenticated:
            partial = kwargs.pop("partial", False)
            instance = self.get_object()
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "result": serializer.data})
        else:
            return Response(
                {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "error": "You are not authorized to Update this Event",
                }
            )

    def destroy(self, request, *args, **kwargs):
        """
        Delete an event.
        """
        if request.user.is_authenticated:
            instance = self.get_object()
            instance.delete()
            return Response(
                {"status": status.HTTP_200_OK, "result": "Event deleted successfully"}
            )
        else:
            return Response(
                {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "error": "You are not authorized to delete this Event",
                }
            )


class NewsFeedViewSet(viewsets.GenericViewSet):
    """
    ViewSet for managing NewsFeed.
    """

    queryset = NewsFeed.objects.all().order_by(
        "-date_posted"
    )  # Default ordering by date_posted
    pagination_class = LimitOffsetPagination
    serializer_class = serializers.NewsFeedSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "id"
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Searchable fields
    search_fields = ["title", "content", "type"]

    # Filterable fields
    filterset_fields = {
        "type": ["iexact"],  # Case-insensitive exact match for type
    }

    # Fields allowed for ordering
    ordering_fields = ["date_posted", "title", "type"]
    ordering = ["-date_posted"]  # Default ordering by descending date_posted

    def list(self, request, *args, **kwargs):
        """
        List all NewsFeeds.
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"status": status.HTTP_200_OK, "results": serializer.data})

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a specific NewsFeed.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({"status": status.HTTP_200_OK, "result": serializer.data})

    def create(self, request, *args, **kwargs):
        """
        Create a new NewsFeed.
        """
        if request.user.is_authenticated:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {"status": status.HTTP_201_CREATED, "result": serializer.data}
            )
        else:
            return Response(
                {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "error": "You are not authorized to Create this NewsFeed",
                }
            )

    def update(self, request, *args, **kwargs):
        """
        Update an existing NewsFeed.
        """
        if request.user.is_authenticated:
            partial = kwargs.pop("partial", False)
            instance = self.get_object()
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "result": serializer.data})
        else:
            return Response(
                {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "error": "You are not authorized to Update this NewsFeed",
                }
            )

    def destroy(self, request, *args, **kwargs):
        """
        Delete a NewsFeed.
        """
        if request.user.is_authenticated:
            instance = self.get_object()
            instance.delete()
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "result": "NewsFeed deleted successfully",
                }
            )
        else:
            return Response(
                {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "error": "You are not authorized to delete this NewsFeed",
                }
            )


class PostViewSet(viewsets.GenericViewSet):
    """
    ViewSet for managing posts.
    """

    queryset = Post.objects.all().order_by(
        "-created_at"
    )  # Default ordering by date_posted
    pagination_class = LimitOffsetPagination
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = ["post"]

    # filterset_fields = {
    #     "post": ["iexact"],  
    # }

    ordering_fields = ["created_at", "id"]
    ordering = ["-created_at"]  # Default ordering by descending date_posted

    def list(self, request, *args, **kwargs):
        """
        List all posts.
        """
        queryset = self.filter_queryset(self.get_queryset())

        
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"status": status.HTTP_200_OK, "results": serializer.data})

    def create(self, request, *args, **kwargs):
        """
        Create a new post.
        """
        if request.user.is_authenticated:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(created_by=request.user)
            return Response(
                {"status": status.HTTP_201_CREATED, "result": serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "You are not authorized to Create this Post",
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

   
class CommentListGetCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id).order_by('-created_at')

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(user=self.request.user, post_id=post_id)




# Registration Request View

class RegistrationRequestView(viewsets.GenericViewSet):
    queryset = RegistrationRequest.objects.all()
    serializer_class = serializers.RegistrationRequestSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["firstName", "lastName", "email"]
    filterset_fields = {
        # "role": ["id"],  
    }

    def create(self, request):
        """Enhanced alumni registration with auto-approval scoring"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                # Check if user already exists
                existing_user = User.objects.filter(email=serializer.validated_data['email']).first()
                if existing_user:
                    return Response({
                        "message": "User with this email already exists"
                    }, status=status.HTTP_400_BAD_REQUEST)
                
                # Calculate alumni verification score
                verification_scores = AlumniVerificationService.calculate_alumni_score(serializer.validated_data)
                
                # Create verification score record
                alumni_verification = AlumniVerificationScore.objects.create(
                    email=serializer.validated_data['email'],
                    student_id=serializer.validated_data.get('studentId', ''),
                    graduation_year=serializer.validated_data.get('graduationYear', 0),
                    department=serializer.validated_data.get('department', ''),
                    linkedin_profile=serializer.validated_data.get('linkedin', ''),
                    student_id_score=verification_scores['student_id_score'],
                    graduation_year_score=verification_scores['graduation_year_score'],
                    linkedin_score=verification_scores['linkedin_score'],
                    document_score=verification_scores['document_score'],
                    total_score=verification_scores['total_score']
                )
                
                # Check if auto-approval criteria is met
                if alumni_verification.is_auto_approvable():
                    # Auto-approve and create user account
                    user = User.objects.create_user(
                        username=serializer.validated_data['email'],
                        email=serializer.validated_data['email'],
                        first_name=serializer.validated_data['firstName'],
                        last_name=serializer.validated_data['lastName'],
                        password='temp_password_123'  # User will reset via email
                    )
                    
                    # Create UserInfo profile
                    UserInfo.objects.create(
                        user=user,
                        first_name=serializer.validated_data['firstName'],
                        last_name=serializer.validated_data['lastName'],
                        email=serializer.validated_data['email'],
                        phone=serializer.validated_data.get('phone', ''),
                        address=serializer.validated_data.get('address', ''),
                        graduation_year=serializer.validated_data.get('graduationYear'),
                        batch=serializer.validated_data.get('batch'),
                        current_company=serializer.validated_data.get('currentCompany', ''),
                        current_position=serializer.validated_data.get('currentPosition', ''),
                        experience=str(serializer.validated_data.get('experience', '')),
                        skills=serializer.validated_data.get('skills', []),
                        interests=serializer.validated_data.get('interests', []),
                        achievements=serializer.validated_data.get('achievements', ''),
                        linkedin=serializer.validated_data.get('linkedin', ''),
                    )
                    
                    alumni_verification.verification_status = 'auto_approved'
                    alumni_verification.save()
                    
                    return Response({
                        "message": "Congratulations! Your alumni registration has been automatically approved.",
                        "status": "auto_approved",
                        "verification_score": verification_scores['total_score'],
                        "next_steps": "Please check your email for login instructions."
                    }, status=status.HTTP_201_CREATED)
                
                else:
                    # Create registration request for manual review
                    registration_request = serializer.save()
                    alumni_verification.verification_status = 'manual_review'
                    alumni_verification.save()
                    
                    return Response({
                        "message": "Your alumni registration has been submitted for review.",
                        "status": "manual_review",
                        "verification_score": verification_scores['total_score'],
                        "required_score": alumni_verification.auto_approval_threshold,
                        "next_steps": "Our team will review your application within 3-5 business days."
                    }, status=status.HTTP_201_CREATED)
                    
            except Exception as e:
                return Response({
                    "message": f"Registration failed: {str(e)}"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)
        paginated_queryset = self.paginate_queryset(filtered_queryset)
        permission_classes = [permissions.IsAuthenticated]

        if paginated_queryset is not None:
            serializer = self.get_serializer(paginated_queryset, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_queryset, many=True)
        # return Response({"status": status.HTTP_200_OK, "results": serializer.data})
        return Response(serializer.data)    
    def retrieve(self, request, *args, **kwargs):
        permission_classes = [permissions.IsAuthenticated]
        instance = self.queryset.filter(id=kwargs['id']).first()
        if not instance:
            return Response({"status": status.HTTP_404_NOT_FOUND, "message": "Registration request not found."})
        serializer = self.get_serializer(instance, context={'request': request})
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        permission_classes = [permissions.IsAuthenticated]
        instance = self.queryset.filter(id=kwargs['id']).first()
        if not instance:
            return Response({"status": status.HTTP_404_NOT_FOUND, "message": "Registration request not found."})
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "message": "Registration request updated successfully.", "data": serializer.data})
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "Invalid data provided.", "errors": serializer.errors})
    
    def destroy(self, request, *args, **kwargs):
        permission_classes = [permissions.IsAuthenticated]
        instance = self.queryset.filter(id=kwargs['id']).first()
        if not instance:
            return Response({"status": status.HTTP_404_NOT_FOUND, "message": "Registration request not found."})
        instance.delete()
        return Response({"status": status.HTTP_200_OK, "message": "Registration request deleted successfully."})
    
    @action(detail=True, methods=['put'], permission_classes=[permissions.IsAuthenticated])
    def approve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response({"status": status.HTTP_404_NOT_FOUND, "message": "Registration request not found."})

        # # Mark as approved
        # instance.isApproved = True
        # instance.save()

        # Create user if not already exists
        user = User.objects.filter(email=instance.email).first()
      
        if not user:
            user = User.objects.create_user(
                username=instance.email,
                email=instance.email,
                first_name=instance.firstName,
                last_name=instance.lastName,
                password='12345678'
            )
            # Assign default role (id=2) for alumni
            role = Role.objects.filter(id=2).first()
            if not role:
                user.delete()
                return Response({"message": "Role does not exist"}, status=400)

            user_info = UserInfo.objects.create(
                user=user,
                role=role,
                first_name=instance.firstName,
                last_name=instance.lastName,
                email=instance.email,
                avatar=instance.avatar,
                description='As an esteemed graduate of our university, this alumnus embodies the values of excellence, integrity, and lifelong learning. Through dedication to academic pursuits and active engagement in extracurricular activities, they have developed a strong foundation for personal and professional growth. Their commitment to innovation, leadership, and service is evident in their ongoing contributions to their chosen field and broader community. As part of our vibrant alumni network, they continue to foster meaningful connections, support fellow graduates, and inspire future generations. We are proud to recognize their achievements and celebrate their ongoing journey as a valued member of our alumni family.',
                phone=instance.phone,
                address=instance.address,
                graduation_year=instance.graduationYear,
                batch=instance.batch,
                current_company=instance.currentCompany,
                current_position=instance.currentPosition,
                experience=instance.experience,
                skills=instance.skills,
                interests=instance.interests,
                achievements='',
                facebook=instance.facebook,
                twitter=instance.twitter,
                linkedin=instance.linkedin,
                instagram=instance.instagram
            )
            user_info.save()

            instance.isApproved = True
            instance.save()
        else:   
            return Response({
                "status": status.HTTP_200_OK,
                "message": "User already exists.",
            }, status=status.HTTP_400_BAD_REQUEST)

        # Optionally, serialize and return user_info if you want
        return Response({
            "status": status.HTTP_200_OK,
            "message": "Registration request approved and user registered.",
            "user_info": UserInfoSerializer(user_info).data if user_info else None,
        })

    @action(detail=True, methods=['put'], permission_classes=[permissions.IsAuthenticated])
    def reject(self, request, *args, **kwargs):
        instance = self.get_object()
        body = request.data
        if not instance:
            return Response({"status": status.HTTP_404_NOT_FOUND, "message": "Registration request not found."})
        instance.isApproved = False
        instance.rejectionReason = body.get('rejectionReason', '')
        instance.save()

        return Response({
            "status": status.HTTP_200_OK,
            "message": "Registration request rejected.",
        })



# Gallery API Views

@api_view(['GET'])
@permission_classes([AllowAny])
def gallery_images(request):
    """Get all public gallery images with filtering"""
    try:
        # Get query parameters
        category = request.GET.get('category', None)
        tag = request.GET.get('tag', None)
        search = request.GET.get('search', None)
        
        # Base queryset - only public images
        queryset = GalleryImage.objects.filter(is_public=True).select_related('category', 'album', 'uploaded_by').prefetch_related('tags')
        
        # Apply filters
        if category and category != 'all':
            queryset = queryset.filter(category__category_type=category)
        
        if tag and tag != 'all':
            queryset = queryset.filter(tags__name__icontains=tag)
        
        if search:
            queryset = queryset.filter(
                title__icontains=search
            ).union(
                queryset.filter(description__icontains=search)
            ).union(
                queryset.filter(people_tagged__icontains=search)
            ).union(
                queryset.filter(special_guests__icontains=search)
            )
        
        # Order by priority and date
        queryset = queryset.order_by('-priority', '-event_date', '-created_at')
        
        # Serialize data
        images_data = []
        for image in queryset:
            # Increment view count
            image.increment_view_count()
            
            images_data.append({
                'id': image.id,
                'title': image.title,
                'description': image.description,
                'image': request.build_absolute_uri(image.image.url) if image.image else None,
                'thumbnail': request.build_absolute_uri(image.thumbnail.url) if image.thumbnail else None,
                'category': image.category.category_type if image.category else None,
                'tags': [tag.name for tag in image.tags.all()],
                'event_date': image.event_date.isoformat(),
                'event_location': image.event_location,
                'people_tagged': image.people_tagged,
                'special_guests': image.special_guests,
                'view_count': image.view_count,
                'likes': image.likes.count(),
                'comments': image.comments.filter(is_approved=True).count(),
                'photographer': image.photographer,
                'priority': image.priority,
                'is_featured': image.is_featured,
            })
        
        return Response({
            'status': status.HTTP_200_OK,
            'count': len(images_data),
            'results': images_data
        })
        
    except Exception as e:
        return Response({
            'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message': f'Error fetching gallery images: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([AllowAny])
def gallery_categories(request):
    """Get all active gallery categories with image counts"""
    try:
        categories = GalleryCategory.objects.filter(is_active=True).order_by('order', 'name')
        
        categories_data = []
        for category in categories:
            image_count = GalleryImage.objects.filter(category=category, is_public=True).count()
            categories_data.append({
                'id': category.id,
                'name': category.name,
                'category_type': category.category_type,
                'color_code': category.color_code,
                'count': image_count
            })
        
        # Add "All Photos" option
        total_count = GalleryImage.objects.filter(is_public=True).count()
        all_photos = {
            'id': 'all',
            'name': 'All Photos',
            'category_type': 'all',
            'color_code': '#dc2626',
            'count': total_count
        }
        
        return Response({
            'status': status.HTTP_200_OK,
            'results': [all_photos] + categories_data
        })
        
    except Exception as e:
        return Response({
            'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message': f'Error fetching categories: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([AllowAny])
def gallery_tags(request):
    """Get featured gallery tags"""
    try:
        tags = GalleryTag.objects.filter(is_featured=True).order_by('tag_type', 'name')
        
        tags_data = [tag.name for tag in tags]
        
        return Response({
            'status': status.HTTP_200_OK,
            'results': tags_data
        })
        
    except Exception as e:
        return Response({
            'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message': f'Error fetching tags: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)