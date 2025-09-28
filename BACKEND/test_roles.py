#!/usr/bin/env python
import os
import sys
import django

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CORE.settings')
django.setup()

from cms.models import Role
from authorization.models import UserInfo
from django.contrib.auth.models import User

def test_roles_and_users():
    print("=== ROLES IN DATABASE ===")
    roles = Role.objects.all()
    for role in roles:
        print(f"ID: {role.id}, Name: {role.role_name}, Description: {role.description}")
    
    print("\n=== USER COUNTS BY ROLE ===")
    for role in roles:
        count = UserInfo.objects.filter(role=role).count()
        print(f"Role '{role.role_name}' (ID: {role.id}): {count} users")
    
    print("\n=== SAMPLE ALUMNI USERS ===")
    try:
        alumni_role = Role.objects.get(role_name='Alumni')
        alumni_users = UserInfo.objects.filter(role=alumni_role)[:5]
        for user_info in alumni_users:
            print(f"- {user_info.first_name} {user_info.last_name} ({user_info.email})")
    except Role.DoesNotExist:
        print("No Alumni role found!")
    
    print("\n=== SAMPLE STUDENT USERS ===")
    try:
        student_role = Role.objects.get(role_name='Student')
        student_users = UserInfo.objects.filter(role=student_role)[:5]
        for user_info in student_users:
            print(f"- {user_info.first_name} {user_info.last_name} ({user_info.email})")
    except Role.DoesNotExist:
        print("No Student role found!")

if __name__ == "__main__":
    test_roles_and_users()
