# Mentorship and Blogs population methods for populate_indian_data.py

def populate_mentors(self):
    """Create mentor profiles from alumni"""
    mentor_role = Role.objects.get(role_name='Mentor')
    
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
        mentor_profile = MentorProfile.objects.create(
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
        
        # Update user role to include mentor
        mentor_role_obj, created = Role.objects.get_or_create(role_name='Mentor')
        # Note: User can have multiple roles, but our current model supports only one role
        # In a real scenario, you might want to implement many-to-many relationship
    
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
