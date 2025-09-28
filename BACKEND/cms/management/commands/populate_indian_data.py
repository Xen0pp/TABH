import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import transaction
from cms.models import *
from cms.mentorship_models import *
from authorization.models import UserInfo


class Command(BaseCommand):
    help = 'Populate database with Indian-specific fake data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before populating',
        )
        parser.add_argument(
            '--debug',
            action='store_true',
            help='Enable debug output',
        )

    def handle(self, *args, **options):
        self.debug = options.get('debug', False)
        
        if options['clear']:
            self.stdout.write(self.style.WARNING('Clearing existing data...'))
            self.clear_data()
        
        self.stdout.write(self.style.SUCCESS('Starting data population...'))
        
        try:
            # Populate in order due to dependencies
            self.populate_roles()
            self.populate_alumni()
            self.populate_students()
            self.populate_jobs()
            self.populate_events()
            self.populate_mentors()
            self.populate_mentorship_requests()
            self.populate_blogs_and_news()
            
            self.stdout.write(
                self.style.SUCCESS('✅ Successfully populated database with Indian data!')
            )
            
            # Print summary
            # self.print_summary()
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error during population: {str(e)}')
            )
            if self.debug:
                import traceback
                self.stdout.write(traceback.format_exc())

    def debug_print(self, message):
        """Print debug messages if debug mode is enabled"""
        if self.debug:
            self.stdout.write(self.style.WARNING(f'DEBUG: {message}'))

    def clear_data(self):
        """Clear existing data"""
        try:
            with transaction.atomic():
                self.debug_print('Clearing mentorship sessions...')
                MentorshipSession.objects.all().delete()
                
                self.debug_print('Clearing mentorship requests...')
                MentorshipRequest.objects.all().delete()
                
                self.debug_print('Clearing mentor profiles...')
                MentorProfile.objects.all().delete()
                
                self.debug_print('Clearing user info...')
                UserInfo.objects.all().delete()
                
                self.debug_print('Clearing non-superuser users...')
                User.objects.filter(is_superuser=False).delete()
                
                self.debug_print('Clearing jobs...')
                Job.objects.all().delete()
                
                self.debug_print('Clearing events...')
                Event.objects.all().delete()
                
                self.debug_print('Clearing blogs...')
                Blog.objects.all().delete()
                
                self.debug_print('Clearing posts...')
                Post.objects.all().delete()
                
                self.debug_print('Clearing news feed...')
                NewsFeed.objects.all().delete()
                
                self.debug_print('Clearing roles...')
                Role.objects.all().delete()
                
            self.stdout.write(self.style.SUCCESS('✅ Data cleared successfully!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Error clearing data: {str(e)}'))

    # Data arrays
    INDIAN_FIRST_NAMES_MALE = [
        'Aarav', 'Arjun', 'Aditya', 'Ankit', 'Amit', 'Rohit', 'Vikash', 'Pradeep',
        'Rajesh', 'Suresh', 'Ramesh', 'Mahesh', 'Dinesh', 'Rakesh', 'Naresh',
        'Kiran', 'Ravi', 'Sanjay', 'Ajay', 'Vijay', 'Manish', 'Ashish', 'Nishant',
        'Abhishek', 'Akash', 'Vishal', 'Nikhil', 'Sachin', 'Rahul', 'Gaurav'
    ]
    
    INDIAN_FIRST_NAMES_FEMALE = [
        'Priya', 'Pooja', 'Riya', 'Shreya', 'Ananya', 'Kavya', 'Divya', 'Sneha',
        'Neha', 'Meera', 'Sita', 'Geeta', 'Sunita', 'Anita', 'Nita', 'Rita',
        'Shweta', 'Swati', 'Preeti', 'Kriti', 'Aditi', 'Smriti', 'Shakti', 'Bhakti',
        'Asha', 'Usha', 'Nisha', 'Disha', 'Trisha', 'Manisha'
    ]
    
    INDIAN_LAST_NAMES = [
        'Sharma', 'Gupta', 'Singh', 'Kumar', 'Agarwal', 'Bansal', 'Jain', 'Mittal',
        'Verma', 'Tiwari', 'Mishra', 'Pandey', 'Yadav', 'Chauhan', 'Rajput', 'Thakur',
        'Patel', 'Shah', 'Mehta', 'Desai', 'Modi', 'Joshi', 'Trivedi', 'Bhatt',
        'Reddy', 'Rao', 'Nair', 'Menon', 'Iyer', 'Krishnan', 'Pillai', 'Das'
    ]
    
    INDIAN_COMPANIES = [
        'Tata Consultancy Services', 'Infosys', 'Wipro', 'HCL Technologies', 'Tech Mahindra',
        'Accenture India', 'IBM India', 'Microsoft India', 'Google India', 'Amazon India',
        'Flipkart', 'Paytm', 'Zomato', 'Swiggy', 'Ola', 'Uber India', 'PhonePe',
        'BYJU\'S', 'Unacademy', 'Razorpay', 'Freshworks', 'Zoho', 'InMobi', 'Myntra',
        'BigBasket', 'PolicyBazaar', 'MakeMyTrip', 'Nykaa', 'Lenskart', 'Urban Company'
    ]
    
    INDIAN_CITIES = [
        'New Delhi', 'Mumbai', 'Bangalore', 'Hyderabad', 'Chennai', 'Pune', 'Kolkata',
        'Ahmedabad', 'Jaipur', 'Lucknow', 'Kanpur', 'Nagpur', 'Indore', 'Thane',
        'Bhopal', 'Visakhapatnam', 'Pimpri-Chinchwad', 'Patna', 'Vadodara', 'Ghaziabad'
    ]

    def populate_roles(self):
        """Create basic roles"""
        self.debug_print('Creating roles...')
        roles_data = [
            {'role_name': 'Alumni', 'description': 'Graduated students of VIPS-TC'},
            {'role_name': 'Student', 'description': 'Current students of VIPS-TC'},
            {'role_name': 'Admin', 'description': 'Administrative staff'},
            {'role_name': 'Mentor', 'description': 'Alumni who provide mentorship'},
            {'role_name': 'Mentee', 'description': 'Students seeking mentorship'},
        ]
        
        created_count = 0
        for role_data in roles_data:
            role, created = Role.objects.get_or_create(
                role_name=role_data['role_name'],
                defaults={'description': role_data['description']}
            )
            if created:
                created_count += 1
                self.debug_print(f'Created role: {role.role_name}')
        
        self.stdout.write(f'✅ Created {created_count} roles')

    def populate_alumni(self):
        """Create alumni profiles"""
        self.debug_print('Creating alumni profiles...')
        
        try:
            alumni_role = Role.objects.get(role_name='Alumni')
        except Role.DoesNotExist:
            self.stdout.write(self.style.ERROR('❌ Alumni role not found. Run populate_roles first.'))
            return
            
        departments = ['Computer Science Engineering', 'Information Technology', 'Electronics & Communication', 
                      'Mechanical Engineering', 'Civil Engineering', 'Electrical Engineering']
        
        positions = [
            'Software Engineer', 'Senior Software Engineer', 'Tech Lead', 'Engineering Manager',
            'Product Manager', 'Data Scientist', 'DevOps Engineer', 'Full Stack Developer',
            'Backend Developer', 'Frontend Developer', 'Mobile Developer', 'QA Engineer',
            'Business Analyst', 'Project Manager', 'Consultant', 'Architect'
        ]
        
        skills_pool = [
            'Python', 'Java', 'JavaScript', 'React', 'Node.js', 'Django', 'Flask',
            'Spring Boot', 'Angular', 'Vue.js', 'Docker', 'Kubernetes', 'AWS', 'Azure',
            'Machine Learning', 'Data Science', 'SQL', 'MongoDB', 'PostgreSQL', 'Redis',
            'Git', 'Jenkins', 'Terraform', 'Linux', 'Microservices', 'REST APIs'
        ]
        
        interests_pool = [
            'Artificial Intelligence', 'Machine Learning', 'Web Development', 'Mobile Development',
            'Cloud Computing', 'DevOps', 'Data Science', 'Cybersecurity', 'Blockchain',
            'IoT', 'Robotics', 'Gaming', 'Fintech', 'Edtech', 'Healthtech'
        ]
        
        created_count = 0
        with transaction.atomic():
            for i in range(50):
                try:
                    # Random gender selection
                    is_male = random.choice([True, False])
                    first_name = random.choice(self.INDIAN_FIRST_NAMES_MALE if is_male else self.INDIAN_FIRST_NAMES_FEMALE)
                    last_name = random.choice(self.INDIAN_LAST_NAMES)
                    
                    # Create username and email
                    username = f"{first_name.lower()}.{last_name.lower()}{random.randint(10, 99)}"
                    email = f"{username}@gmail.com"
                    
                    # Check if user already exists
                    if User.objects.filter(username=username).exists():
                        username = f"{username}{random.randint(100, 999)}"
                    
                    # Create User
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        password='password123'
                    )
                    
                    # Create UserInfo
                    graduation_year = random.randint(2015, 2023)
                    company = random.choice(self.INDIAN_COMPANIES)
                    position = random.choice(positions)
                    city = random.choice(self.INDIAN_CITIES)
                    department = random.choice(departments)
                    
                    # Generate phone number (Indian format)
                    phone = f"+91 {random.randint(7000000000, 9999999999)}"
                    
                    # Random skills and interests
                    user_skills = random.sample(skills_pool, random.randint(3, 8))
                    user_interests = random.sample(interests_pool, random.randint(2, 5))
                    
                    # Generate experience years
                    experience_years = 2024 - graduation_year + random.randint(0, 2)
                    
                    UserInfo.objects.create(
                        user=user,
                        role=alumni_role,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        phone=phone,
                        address=f"{random.randint(1, 999)} {random.choice(['MG Road', 'Park Street', 'Mall Road', 'Civil Lines', 'Sector ' + str(random.randint(1, 50))])}, {city}",
                        graduation_year=graduation_year,
                        batch=graduation_year,
                        current_company=company,
                        current_position=position,
                        experience=f"{experience_years} years of experience in {department.lower()}",
                        skills=user_skills,
                        interests=user_interests,
                        achievements=f"Successfully working at {company} as {position}. Contributed to multiple projects and mentored junior developers.",
                        linkedin=f"https://linkedin.com/in/{username}",
                        description=f"Experienced {position} at {company} with {experience_years} years in the industry."
                    )
                    created_count += 1
                    
                    if self.debug and i % 10 == 0:
                        self.debug_print(f'Created {i+1} alumni profiles...')
                        
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'❌ Error creating alumni {i+1}: {str(e)}'))
        
        self.stdout.write(f'✅ Created {created_count} alumni profiles')

    def populate_students(self):
        """Create current student profiles"""
        self.debug_print('Creating student profiles...')
        
        try:
            student_role = Role.objects.get(role_name='Student')
        except Role.DoesNotExist:
            self.stdout.write(self.style.ERROR('❌ Student role not found. Run populate_roles first.'))
            return
            
        departments = ['Computer Science Engineering', 'Information Technology', 'Electronics & Communication', 
                      'Mechanical Engineering', 'Civil Engineering', 'Electrical Engineering']
        
        current_year = 2024
        student_years = [2021, 2022, 2023, 2024, 2025]  # Current batches
        
        skills_pool = [
            'Python', 'Java', 'C++', 'JavaScript', 'HTML/CSS', 'React', 'Node.js',
            'Data Structures', 'Algorithms', 'Database Management', 'Web Development',
            'Mobile Development', 'Machine Learning', 'Git', 'Linux'
        ]
        
        interests_pool = [
            'Software Development', 'Web Development', 'Mobile App Development', 'Data Science',
            'Machine Learning', 'Artificial Intelligence', 'Cybersecurity', 'Cloud Computing',
            'Game Development', 'UI/UX Design', 'DevOps', 'Blockchain'
        ]
        
        created_count = 0
        with transaction.atomic():
            for i in range(30):
                try:
                    # Random gender selection
                    is_male = random.choice([True, False])
                    first_name = random.choice(self.INDIAN_FIRST_NAMES_MALE if is_male else self.INDIAN_FIRST_NAMES_FEMALE)
                    last_name = random.choice(self.INDIAN_LAST_NAMES)
                    
                    # Create username and email
                    username = f"{first_name.lower()}.{last_name.lower()}.student{random.randint(100, 999)}"
                    email = f"{username}@vips-tc.edu.in"
                    
                    # Check if user already exists
                    if User.objects.filter(username=username).exists():
                        username = f"{username}{random.randint(1000, 9999)}"
                    
                    # Create User
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        password='password123'
                    )
                    
                    # Student details
                    batch_year = random.choice(student_years)
                    department = random.choice(departments)
                    city = random.choice(self.INDIAN_CITIES)
                    
                    # Generate phone number (Indian format)
                    phone = f"+91 {random.randint(7000000000, 9999999999)}"
                    
                    # Random skills and interests
                    user_skills = random.sample(skills_pool, random.randint(2, 6))
                    user_interests = random.sample(interests_pool, random.randint(2, 4))
                    
                    # Current year calculation
                    current_academic_year = current_year - batch_year + 1
                    if current_academic_year > 4:
                        current_academic_year = 4
                    
                    UserInfo.objects.create(
                        user=user,
                        role=student_role,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        phone=phone,
                        address=f"{random.randint(1, 999)} {random.choice(['Student Hostel', 'PG Accommodation', 'Family Residence'])}, {city}",
                        graduation_year=batch_year + 4,  # Expected graduation
                        batch=batch_year,
                        skills=user_skills,
                        interests=user_interests,
                        description=f"Currently pursuing {department} at VIPS-TC. {current_academic_year}{'st' if current_academic_year == 1 else 'nd' if current_academic_year == 2 else 'rd' if current_academic_year == 3 else 'th'} year student interested in {', '.join(user_interests[:2])}."
                    )
                    created_count += 1
                    
                    if self.debug and i % 5 == 0:
                        self.debug_print(f'Created {i+1} student profiles...')
                        
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'❌ Error creating student {i+1}: {str(e)}'))
        
        self.stdout.write(f'✅ Created {created_count} student profiles')

    def populate_jobs(self):
        """Create job listings"""
        job_titles = [
            'Software Engineer', 'Senior Software Engineer', 'Full Stack Developer', 'Backend Developer',
            'Frontend Developer', 'Mobile App Developer', 'Data Scientist', 'Machine Learning Engineer',
            'DevOps Engineer', 'Cloud Engineer', 'Product Manager', 'Business Analyst',
            'QA Engineer', 'Test Automation Engineer', 'UI/UX Designer', 'Technical Lead',
            'Engineering Manager', 'Scrum Master', 'Database Administrator', 'Cybersecurity Analyst'
         ]
    
        job_descriptions = {
            'Software Engineer': 'Develop and maintain software applications using modern technologies. Work with cross-functional teams to deliver high-quality solutions.',
            'Data Scientist': 'Analyze large datasets to extract meaningful insights. Build predictive models and work with machine learning algorithms.',
            'Product Manager': 'Define product strategy and roadmap. Work closely with engineering and design teams to deliver exceptional user experiences.',
            'DevOps Engineer': 'Manage CI/CD pipelines, cloud infrastructure, and deployment processes. Ensure system reliability and scalability.',
            'Full Stack Developer': 'Work on both frontend and backend development. Build end-to-end web applications using modern frameworks.',
        }
    
    # Salary ranges in INR (per annum)
        salary_ranges = {
            'Software Engineer': (300000, 800000),
            'Senior Software Engineer': (800000, 1500000),
            'Data Scientist': (600000, 1800000),
            'Product Manager': (1000000, 2500000),
            'DevOps Engineer': (700000, 1600000),
            'Full Stack Developer': (400000, 1200000),
        }
    
        for i in range(40):
            title = random.choice(job_titles)
            company = random.choice(self.INDIAN_COMPANIES)
            location = random.choice(self.INDIAN_CITIES)
            job_type = random.choice(['Full-Time', 'Part-Time', 'Remote', 'Intern'])
        
        # Get description or use default
            description = job_descriptions.get(title, f'Exciting opportunity to work as {title} at {company}. Join our dynamic team and contribute to innovative projects.')
        
        # Calculate salary based on role
            if title in salary_ranges:
                min_sal, max_sal = salary_ranges[title]
                salary = random.randint(min_sal, max_sal)
            else:
                salary = random.randint(300000, 1500000)
        
        # Experience requirements
            experience = random.randint(0, 8)
        
        # Deadline (next 30-90 days)
            deadline = timezone.now() + timedelta(days=random.randint(30, 90))
        
        # Contact email
            hr_names = ['hr', 'careers', 'recruitment', 'talent']
            company_domain = company.lower().replace(' ', '').replace('\'', '')[:10]
            email = f"{random.choice(hr_names)}@{company_domain}.com"
        
            Job.objects.create(
                job_title=title,
                company=company,
                location=location,
                description=description,
                jobType=job_type,
                deadline=deadline,
                experience=experience,
                salary=salary,
                email=email
            )
    
        self.stdout.write(f'Created 40 job listings')

    def populate_events(self):
        """Create events"""
        event_types = ['Workshop', 'Seminar', 'Conference', 'Meetup', 'Hackathon', 'Career Fair', 'Alumni Meet', 'Tech Talk']
    
        event_names = [
        'AI/ML Workshop', 'Cloud Computing Seminar', 'Full Stack Development Bootcamp',
        'Data Science Conference', 'Cybersecurity Awareness Workshop', 'Startup Pitch Competition',
        'Alumni Networking Meet', 'Campus Placement Drive', 'Tech Innovation Summit',
        'Mobile App Development Workshop', 'DevOps Best Practices Seminar', 'Women in Tech Conference',
        'Blockchain Technology Workshop', 'Digital Marketing Seminar', 'Career Guidance Session',
        'Industry Expert Talk', 'Coding Competition', 'Technical Paper Presentation',
        'Entrepreneurship Workshop', 'Open Source Contribution Drive'
        ]
    
        venues = [
        'VIPS-TC Auditorium', 'Computer Science Lab', 'Conference Hall A', 'Seminar Hall B',
        'Innovation Center', 'Library Conference Room', 'Student Activity Center',
        'Engineering Block Auditorium', 'Virtual Event (Online)', 'Campus Ground'
        ]
    
        descriptions = {
        'AI/ML Workshop': 'Hands-on workshop covering machine learning fundamentals, popular algorithms, and practical implementation using Python and popular ML libraries.',
        'Alumni Networking Meet': 'Connect with VIPS-TC alumni working in top companies. Share experiences, get career guidance, and expand your professional network.',
        'Campus Placement Drive': 'Multiple companies visiting campus for recruitment. Prepare your resume and practice interview skills for this opportunity.',
        'Hackathon': '48-hour coding competition where teams build innovative solutions to real-world problems. Prizes and internship opportunities available.',
        'Tech Talk': 'Industry experts share insights about latest technology trends, career opportunities, and professional development tips.',
        }
    
        for i in range(20):
            event_name = random.choice(event_names)
            event_type = random.choice(event_types)
            location = random.choice(venues)
        
        # Event date (next 6 months)
            event_date = timezone.now() + timedelta(days=random.randint(1, 180))
        
        # Get description or create default
            description = descriptions.get(event_name.split()[0], f'Join us for an exciting {event_type.lower()} on {event_name}. Great opportunity to learn and network with peers and industry professionals.')
        
            Event.objects.create(
                event_name=event_name,
                date=event_date,
                event_type=event_type,
                location=location,
                description=description
        )
    
        self.stdout.write(f'Created 20 events')

    def populate_mentors(self):
        """Create mentor profiles from alumni"""
        # Get alumni users (first 25 alumni will become mentors)
        alumni_users = User.objects.filter(userinfo__role__role_name='Alumni')[:25]
    
        expertise_areas_pool = [
                'Web Development', 'Mobile App Development', 'Data Science', 'Machine Learning',
                'Artificial Intelligence', 'Cloud Computing', 'DevOps', 'Cybersecurity',
                'Product Management', 'Project Management', 'UI/UX Design', 'Backend Development',
                'Frontend Development', 'Full Stack Development', 'Database Management',
                'Software Architecture', 'Microservices', 'Blockchain', 'IoT', 'Game Development'
            ]
        
        availability_templates = [
                {"weekdays": ["Monday", "Wednesday", "Friday"], "time_slots": ["6:00 PM - 8:00 PM"]},
                {"weekdays": ["Tuesday", "Thursday"], "time_slots": ["7:00 PM - 9:00 PM"]},
                {"weekdays": ["Saturday", "Sunday"], "time_slots": ["10:00 AM - 12:00 PM", "2:00 PM - 4:00 PM"]},
                {"weekdays": ["Monday", "Tuesday", "Wednesday"], "time_slots": ["8:00 PM - 9:00 PM"]},
            ]
    
        mentor_bios = [
                "Passionate about mentoring the next generation of developers. I believe in hands-on learning and practical problem-solving approaches.",
                "With over {} years in the industry, I love sharing knowledge and helping students navigate their career paths in technology.",
                "Experienced professional committed to fostering innovation and creativity in young minds. Let's build amazing things together!",
                "I enjoy mentoring students and helping them develop both technical skills and professional mindset needed for success in tech industry.",
                "Dedicated to helping students bridge the gap between academic learning and industry requirements through practical guidance and mentorship."
            ]
    
        for user in alumni_users:
            user_info = user.userinfo_set.first()
            if not user_info:
                continue
            
        # Random expertise areas (2-4 areas)
            expertise = random.sample(expertise_areas_pool, random.randint(2, 4))
        
        # Years of experience
            graduation_year = user_info.graduation_year or 2020
            years_exp = 2024 - graduation_year + random.randint(0, 2)
        
        # Random availability
            availability = random.choice(availability_templates)
        
        # Bio with experience years
            bio = random.choice(mentor_bios)
            if '{}' in bio:
                bio = bio.format(years_exp)
        
        # Create mentor profile
            MentorProfile.objects.create(
                user=user,
                expertise_areas=expertise,
                years_experience=years_exp,
                current_company=user_info.current_company or random.choice(self.INDIAN_COMPANIES),
                current_position=user_info.current_position or 'Senior Software Engineer',
                mentoring_capacity=random.randint(2, 5),
                availability=availability,
                bio=bio,
                linkedin_url=user_info.linkedin,
                is_approved=True,
                is_active=True,
                approval_date=timezone.now(),
                average_rating=round(random.uniform(4.0, 5.0), 1),
                total_mentorships=random.randint(0, 10)
        )
    
        self.stdout.write(f'Created 25 mentor profiles')

    def populate_mentorship_requests(self):
        """Create mentorship requests between students and mentors"""
    # Get students and mentors
        students = User.objects.filter(userinfo__role__role_name='Student')[:15]
        mentors = User.objects.filter(mentor_profile__isnull=False)
    
        goals_templates = [
            "I want to improve my coding skills and learn industry best practices for software development.",
            "Looking for guidance on career path in data science and machine learning.",
            "Need help with full-stack web development projects and building a strong portfolio.",
            "Seeking mentorship for transitioning from academic projects to real-world applications.",
            "Want to learn about product management and how to build user-centric solutions.",
            "Looking for guidance on preparing for technical interviews at top tech companies.",
            "Need help understanding cloud technologies and DevOps practices.",
            "Seeking career advice for breaking into cybersecurity field.",
            "Want to learn mobile app development and publish apps on app stores.",
            "Looking for mentorship on entrepreneurship and starting a tech startup."
        ]
    
        statuses = ['pending', 'accepted', 'rejected', 'completed']
        communication_prefs = ['video_calls', 'messaging', 'mixed']
    
        for i in range(15):
            student = random.choice(students)
            mentor = random.choice(mentors)
        
        # Avoid duplicate requests
            if MentorshipRequest.objects.filter(mentee=student, mentor=mentor).exists():
                continue
        
            goals = random.choice(goals_templates)
            status = random.choice(statuses)
            duration = random.randint(2, 6)  # 2-6 months
            communication = random.choice(communication_prefs)
        
        # Create request with dates based on status
            request_date = timezone.now() - timedelta(days=random.randint(1, 60))
        
            mentorship_request = MentorshipRequest.objects.create(
                mentee=student,
                mentor=mentor,
                goals=goals,
                duration_months=duration,
                preferred_communication=communication,
                status=status,
                requested_at=request_date
            )
        
        # Add response data for non-pending requests
            if status != 'pending':
                mentorship_request.responded_at = request_date + timedelta(days=random.randint(1, 7))
            
                if status == 'accepted':
                    mentorship_request.mentor_response = "I'd be happy to mentor you! Let's schedule our first session."
                    mentorship_request.started_at = mentorship_request.responded_at
                    mentorship_request.progress_percentage = random.randint(10, 80)
                elif status == 'rejected':
                    mentorship_request.rejection_reason = "Unfortunately, I'm at full capacity right now. Please try again next month."
                elif status == 'completed':
                    mentorship_request.mentor_response = "Great to work with you!"
                    mentorship_request.started_at = mentorship_request.responded_at
                    mentorship_request.completed_at = mentorship_request.started_at + timedelta(days=duration * 30)
                    mentorship_request.progress_percentage = 100
                    mentorship_request.mentee_rating = random.randint(4, 5)
                    mentorship_request.mentor_rating = random.randint(4, 5)
                    mentorship_request.mentee_feedback = "Excellent mentorship experience! Learned a lot."
            
                mentorship_request.save()
    
        self.stdout.write(f'Created 15 mentorship requests')

    def populate_blogs_and_news(self):
        """Create blog posts and news feed items"""
    
    # Blog posts
        blog_titles = [
            'Getting Started with Machine Learning in 2024',
            'Top 10 Programming Languages for Indian Developers',
            'Career Opportunities in Cloud Computing',
            'How to Prepare for Technical Interviews',
            'Building Your First Full-Stack Application',
            'The Rise of AI in Indian Tech Industry',
            'Remote Work Best Practices for Developers',
            'Open Source Contribution: A Beginner\'s Guide',
            'Data Science Career Path in India',
            'Cybersecurity Fundamentals Every Developer Should Know'
        ]
    
        blog_contents = [
            'Machine Learning has become one of the most sought-after skills in the tech industry. In this comprehensive guide, we\'ll explore the fundamentals of ML and how to get started with your journey...',
            'The Indian tech industry is booming, and choosing the right programming language can make a significant difference in your career. Here are the top 10 languages that are in high demand...',
            'Cloud computing has revolutionized how businesses operate. From startups to enterprises, everyone is moving to the cloud. Let\'s explore the various career opportunities...',
            'Technical interviews can be challenging, but with the right preparation, you can ace them. Here\'s a comprehensive guide to help you prepare for your next tech interview...',
            'Building your first full-stack application is an exciting milestone in your development journey. In this tutorial, we\'ll walk through creating a complete web application...'
        ]
    
        for i in range(10):
            title = blog_titles[i] if i < len(blog_titles) else f'Tech Blog Post {i+1}'
            content = blog_contents[i % len(blog_contents)]
        
            Blog.objects.create(
                title=title,
                content=content,
                created_at=timezone.now() - timedelta(days=random.randint(1, 90))
            )
    
    # News feed items
        news_titles = [
            'VIPS-TC Alumni Lands Job at Google India',
            'New AI/ML Lab Inaugurated at Campus',
            'Campus Placement Drive Achieves 95% Success Rate',
            'Student Team Wins National Hackathon',
            'Industry Partnership with Leading Tech Companies',
            'Alumni Startup Raises ₹10 Crore Funding',
            'New Course on Cloud Computing Launched',
            'International Conference on Technology Innovation',
            'Student Research Paper Published in IEEE Journal',
            'Alumni Mentorship Program Reaches 500+ Students',
            'Campus Incubation Center Supports 20+ Startups',
            'Women in Tech Initiative Launched',
            'Virtual Reality Lab Setup Completed',
            'Industry Expert Lecture Series Begins',
            'Alumni Association Annual Meet Scheduled'
        ]
    
        news_contents = [
            'We are proud to announce that our alumnus has joined Google India as a Senior Software Engineer.',
            'The new AI/ML lab equipped with latest hardware and software has been inaugurated to support advanced research.',
            'This year\'s placement drive has been highly successful with top companies recruiting our talented students.',
            'Our student team has won the national hackathon competition with their innovative solution.',
            'VIPS-TC has partnered with leading technology companies to provide better industry exposure to students.'
        ]
    
        news_types = ['Achievement', 'Infrastructure', 'Placement', 'Competition', 'Partnership']
    
        for i in range(15):
            title = news_titles[i] if i < len(news_titles) else f'Campus News {i+1}'
            content = news_contents[i % len(news_contents)]
            news_type = random.choice(news_types)
        
            NewsFeed.objects.create(
                title=title,
                content=content,
                type=news_type,
                date_posted=timezone.now() - timedelta(days=random.randint(1, 30))
            )
    
        self.stdout.write(f'Created 10 blog posts and 15 news items')

