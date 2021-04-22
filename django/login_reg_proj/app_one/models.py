from django.db import models

import bcrypt
import re

class UserManager(models.Manager):
    def registration_validator(self, post_data):
        errors = {}

        if len(post_data['first_name']) < 1:
            errors['first_name'] = "First name must be filled out."
        if len(post_data['last_name']) < 1:
            errors['last_name'] = "Last name must be filled out."
    
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):           
            errors['email'] = "Invalid email address!"
        else:
            user_list = User.objects.filter(email = post_data['email'])
            if len(user_list) > 0:
                errors['email'] = "Email is already in use."
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = "Password and Confirm password must match."
        return errors
        

    def login_validator(self, post_data):
        errors = {}
        user_list = User.objects.filter(email = post_data['email'])
        if len(user_list) > 0:
            user = user_list[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors['password'] = "Invalid Login"
        else:
            errors['email'] = "Invalid email"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

# Create your models here.
