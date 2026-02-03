from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
# from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializer import UserInfoSerializer, LoginSerializer,  UserRegisterSerializer, RoleSerializer
from .models import UserInfo
from cms.models import Role, RegistrationRequest, AlumniVerificationScore
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
import re
from datetime import datetime

# Create your views here.

class RegisterView(viewsets.GenericViewSet):
    
    qureyset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request):
         
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():

            try:

                # check if user already exists
                user = User.objects.filter(email=serializer.validated_data['email']).first()

                # print(f"user = {user}")

                if user:
                    # user already exists
                    return Response({"message": "User already exists"}, status=400)
                
                # check if email is valid -- must end with @vipstc.edu.in
                if not serializer.validated_data['email'].endswith("@vipstc.edu.in"):
                    return Response({"message": "Email must be a valid VIPS-TC address (@vipstc.edu.in)"}, status=400)

                # Check if this is an alumni registration (graduated students)
                graduation_year = request.data.get('graduation_year')
                student_id = request.data.get('student_id')
                
                # If graduation year and student ID provided, this is alumni registration
                if graduation_year and student_id:
                    # Create alumni registration request for approval
                    from cms.models import RegistrationRequest
                    
                    alumni_request = RegistrationRequest.objects.create(
                        firstName=serializer.validated_data['first_name'],
                        lastName=serializer.validated_data['last_name'],
                        email=serializer.validated_data['email'],
                        phone=request.data.get('phone', ''),
                        address=request.data.get('address', ''),
                        graduationYear=graduation_year,
                        batch=request.data.get('batch', ''),
                        department=request.data.get('department', ''),
                        studentId=student_id,
                        currentCompany=request.data.get('current_company', ''),
                        currentPosition=request.data.get('current_position', ''),
                        experience=request.data.get('experience', 0),
                        skills=request.data.get('skills', []),
                        interests=request.data.get('interests', []),
                        achievements=request.data.get('achievements', ''),
                        facebook=request.data.get('facebook', ''),
                        twitter=request.data.get('twitter', ''),
                        linkedin=request.data.get('linkedin', ''),
                        instagram=request.data.get('instagram', ''),
                        isApproved=False  # Requires admin approval
                    )
                    
                    return Response({
                        "message": "Alumni registration submitted successfully! Your application is under review. You will be notified once approved.",
                        "status": "pending_approval",
                        "request_id": alumni_request.id
                    }, status=status.HTTP_201_CREATED)
                
                # Otherwise, continue with regular student registration

                # create user
                user = User.objects.create_user(
                username=serializer.validated_data['email'],
                email=serializer.validated_data['email'],
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name'],
                )



                # set hashed password and save user
                user.set_password(serializer.validated_data['password'])
                user.save()

               
                
                # setting student role by default
                role, created = Role.objects.get_or_create(
                    id=1,
                    defaults={
                        'role_name': 'Student',
                        'description': 'Current VIPS-TC student with institutional email'
                    }
                )

                if not role:
                    user.delete()
                    return Response({"message": "Role creation failed"}, status=400)

               
                # create user info
                user_info = UserInfo.objects.create(
                    user=user,
                    role=role,
                    first_name=serializer.validated_data['first_name'],
                    last_name=serializer.validated_data['last_name'],
                    email=serializer.validated_data['email'], 

                )
            
                user_info.save()

                token = RefreshToken.for_user(user)
                access = str(token.access_token)
                refresh = str(token)

                role_serializer = RoleSerializer(role)
                user_info_serializer = UserInfoSerializer(user_info)

                return Response({
                    "message": "User created successfully",
                    "data": {
                       "user_info": user_info_serializer.data,
                       "role": role_serializer.data,                        
                       "status": status.HTTP_201_CREATED,

                    
                        "access": access,
                         "refresh": refresh
                       
                   }
                    
                }, status=status.HTTP_201_CREATED)

            except Exception as e:
                # return Response({"error": str(e)}, status=400)
                return Response({
                    "message": str(e),
                    "status": status.HTTP_400_BAD_REQUEST
                })
                

    
        return Response(serializer.errors)
    


class LoginView(viewsets.GenericViewSet):
    qureyset = User.objects.all()
    serializer_class = LoginSerializer
   
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():

            # find the user
            user = User.objects.filter(email=serializer.validated_data['email']).first()

            if user is None:
                return Response({"error": "User does not exist"}, status=400)

            # check password
            if not user.check_password(serializer.validated_data['password']):
                return Response({"error": "Email or Password wrong"}, status=400)

            # create token
            token = RefreshToken.for_user(user)
            access = str(token.access_token)
            refresh = str(token)

            user_info = UserInfo.objects.filter(user=user).first()

            if user_info is None:
                user_info = UserInfo.objects.create(
                    user=user,
                    first_name='',
                    last_name='',
                    email=user.email,
                    role= Role.objects.get(id=1)
                )

            user_info_serializer = UserInfoSerializer(user_info)
            role_serializer = RoleSerializer(user_info.role)

            return Response({
                "message": "User logged in successfully",
                "status": status.HTTP_200_OK,
                "data": {
                   "user_info": user_info_serializer.data,
                   "role": role_serializer.data,

                   
                   "access": access,
                    "refresh": refresh
                   
               }
                
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors)
    

class UserInfoView(viewsets.GenericViewSet):
    queryset = UserInfo.objects.all().order_by('first_name')
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    lookup_field = 'user'
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["first_name", "last_name", "email"]
    filterset_fields = {
        # "role": ["id"],  
        # "role": ["id"],
    }
    # ordering_fields = ["first_name", "last_name", "email", "id", 'created_at', 'updated_at']
    # ordering = ["-first_name"]

    def get_queryset(self):
        queryset = super().get_queryset()
        role_id = self.request.query_params.get('role')
        if role_id is not None:
            queryset = queryset.filter(role_id=role_id)
        return queryset

    def list(self, request):
        
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)
        paginated_queryset = self.paginate_queryset(filtered_queryset)

        if paginated_queryset is not None:
            serializer = self.get_serializer(paginated_queryset, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_queryset, many=True, context={'request': request})
        return Response({"status": status.HTTP_200_OK, "results": serializer.data})
    
    def retrieve(self, request, *args, **kwargs):
        # extract user id from params
        user_id = kwargs.get('user')
        instance = self.queryset.filter(user=user_id).first()
        if not instance:
            return Response({"status": status.HTTP_404_NOT_FOUND, "message": "User info not found."})
        serializer = self.get_serializer(instance, context={'request': request})
        return Response(serializer.data)
            

class UserRolesView(viewsets.GenericViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["name"]
    filterset_fields = {
        # "role": ["id"],  
    }
    # ordering_fields = ["first_name", "last_name", "email", "id", 'created_at', 'updated_at']
    # ordering = ["-first_name"]

    def list(self, request):
        
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)
        paginated_queryset = self.paginate_queryset(filtered_queryset)

        if paginated_queryset is not None:
            serializer = self.get_serializer(paginated_queryset, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response({"status": status.HTTP_200_OK, "results": serializer.data})
    

class AlumniVerificationService:
    """Service class for alumni verification scoring"""
    
    @staticmethod
    def validate_student_id_format(student_id):
        """Validate VIPS-TC student ID format"""
        # Assuming format: VIPS/TC/YEAR/NUMBER (e.g., VIPS/TC/2020/001)
        pattern = r'^VIPS/TC/\d{4}/\d{3,4}$'
        if re.match(pattern, student_id.upper()):
            return 2  # Perfect format
        elif 'VIPS' in student_id.upper() and any(char.isdigit() for char in student_id):
            return 1  # Partial match
        return 0
    
    @staticmethod
    def validate_graduation_year(year):
        """Validate graduation year"""
        current_year = datetime.now().year
        if 2000 <= year <= current_year:
            if current_year - 5 <= year <= current_year:  # Recent graduates
                return 2
            else:  # Older graduates
                return 1
        return 0
    
    @staticmethod
    def validate_linkedin_profile(linkedin_url):
        """Basic LinkedIn profile validation"""
        if linkedin_url and 'linkedin.com' in linkedin_url.lower():
            if 'vips' in linkedin_url.lower() or 'vivekananda' in linkedin_url.lower():
                return 2  # Profile mentions VIPS
            else:
                return 1  # Valid LinkedIn profile
        return 0
    
    @staticmethod
    def validate_documents(cv_file, proof_file):
        """Validate uploaded documents"""
        score = 0
        if cv_file:
            score += 1
        if proof_file:
            score += 1
        return score
    
    @classmethod
    def calculate_alumni_score(cls, registration_data):
        """Calculate total alumni verification score"""
        student_id_score = cls.validate_student_id_format(registration_data.get('studentId', ''))
        graduation_year_score = cls.validate_graduation_year(registration_data.get('graduationYear', 0))
        linkedin_score = cls.validate_linkedin_profile(registration_data.get('linkedin', ''))
        document_score = cls.validate_documents(
            registration_data.get('cv'), 
            registration_data.get('proofDocument')
        )
        
        return {
            'student_id_score': student_id_score,
            'graduation_year_score': graduation_year_score,
            'linkedin_score': linkedin_score,
            'document_score': document_score,
            'total_score': student_id_score + graduation_year_score + linkedin_score + document_score
        }
