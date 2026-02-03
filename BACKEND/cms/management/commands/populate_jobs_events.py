# Jobs and Events population methods for populate_indian_data.py

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
    
    # Salary ranges in INR (Lakhs per annum)
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
