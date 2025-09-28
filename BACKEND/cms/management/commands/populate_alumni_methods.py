# Alumni and Students population methods for populate_indian_data.py

def populate_alumni(self):
    """Create alumni profiles"""
    alumni_role = Role.objects.get(role_name='Alumni')
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
    
    for i in range(50):
        # Random gender selection
        is_male = random.choice([True, False])
        first_name = random.choice(self.INDIAN_FIRST_NAMES_MALE if is_male else self.INDIAN_FIRST_NAMES_FEMALE)
        last_name = random.choice(self.INDIAN_LAST_NAMES)
        
        # Create username and email
        username = f"{first_name.lower()}.{last_name.lower()}{random.randint(10, 99)}"
        email = f"{username}@gmail.com"
        
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
    
    self.stdout.write(f'Created 50 alumni profiles')

def populate_students(self):
    """Create current student profiles"""
    student_role = Role.objects.get(role_name='Student')
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
    
    for i in range(30):
        # Random gender selection
        is_male = random.choice([True, False])
        first_name = random.choice(self.INDIAN_FIRST_NAMES_MALE if is_male else self.INDIAN_FIRST_NAMES_FEMALE)
        last_name = random.choice(self.INDIAN_LAST_NAMES)
        
        # Create username and email
        username = f"{first_name.lower()}.{last_name.lower()}.student{random.randint(100, 999)}"
        email = f"{username}@vips-tc.edu.in"
        
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
    
    self.stdout.write(f'Created 30 student profiles')
