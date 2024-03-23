from django.db import models
from django.contrib.auth.models import User
from account.models import adminActount

class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=40)
    def __str__(self):
        return self.name
class Projects(models.Model):
    catagory = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='al_content/media/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    technoloties = models.CharField(max_length=250)
    projec_url = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.catagory.name
    
class cv(models.Model):
    user = models.OneToOneField(adminActount, on_delete=models.CASCADE)
    my_cv = models.URLField(null=True, blank=True)
    def __self__(self):
        return self.user.admin_name

LEVEL_CHOICES=[
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Expert', 'Expert'),
]
class SkillModel(models.Model):
    user = models.ForeignKey(adminActount, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255)
    proficiency_level = models.CharField(choices =LEVEL_CHOICES, max_length =15)
    
    def __str__(self):
        return self.user.admin_name
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_no = models.IntegerField()
    message = models.TextField()

STAR_CHOICES=[
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐⭐⭐'),

]
class review(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    rating = models.CharField(choices =STAR_CHOICES, max_length =15)
    def __str__(self):
        return self.name
    
class blog(models.Model):
    user = models.ForeignKey(adminActount, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField()