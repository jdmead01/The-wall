from django.db import models
from datetime import date, datetime
from django.contrib import messages
import re
import bcrypt

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class UserManager(models.Manager):
    def f_name_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = f"{postData['first_name']} is not at least 2 characters."
        if errors:
            return errors
    def l_name_validator(self, postData):
        errors = {}
        if len(postData['last_name']) < 2:
            errors['last_name'] = f"{postData['last_name']} is not at least 2 characters."
        if errors:
            return errors
    def password_validator(self, postData):
        errors = {}
        if len(postData['password']) < 8:
            errors['password'] = "Please enter a password that is at least 8 characters."
        if errors:
            return errors
    def email_validator(self, postData):
        errors = {}
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.fullmatch(pattern, postData['email']):
            errors['email'] = "Please enter a valid email address."
        db_emails = User.objects.filter(email=postData['email'])
        if len(db_emails) > 0:
            errors['unique_email'] = "That email address is already in use."
        if errors:
            return errors
    
    def validate_registration(self, postData):
        errors = {}
        if self.f_name_validator(postData):
            errors.update(self.f_name_validator(postData))
        if self.l_name_validator(postData):
            errors.update(self.l_name_validator(postData))
        if self.email_validator(postData):
            errors.update(self.email_validator(postData))
        if self.password_validator(postData):
            errors.update(self.password_validator(postData))
        # if self.birthdate_validator(postData):
        #     errors.update(self.birthdate_validator(postData))
        return errors

    # def birthdate_validator(self, postData):
    #     errors = {}
    #     bday = postData['birthdate']
    #     today = date.today()
    #     years13 = subtract_years(today, 13)
    #     if datetime.strptime(bday, '%Y-%m-%d').date() > years13:
    #         errors['bday'] = f"You must be born before {years13} to register on this site."
    #     if errors:
    #         print(errors)
    #         return errors
    
    def __repr__(self):
        return f"[User Object: Name({self.first_name} {self.last_name}) id({self.id})]"
    def bcrypt_password(self):
        pw = self.password
        try:
            self.password = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        except:
            raise Exception("Password not hashed")

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class Message(models.Model):
    message = models.TextField()
    author = models.ForeignKey(User, related_name="messages") # one to many relationship between User and Messafe 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class Comment(models.Model):
    comment = models.TextField()
    commented_on = models.ForeignKey(Message, related_name="comments")
    author = models.ForeignKey(User, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(BaseModel):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=32)
    # birthdate = models.DateField()
    objects = UserManager()