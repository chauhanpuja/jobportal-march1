
from django.db import models
from autoslug import AutoSlugField
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User






# Create your models here.


# class Category(models.Model):
#     name=models.CharField(max_length=200)
#     slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)

#     def __str__(self):
#         return self.name

class Category2(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=50,null=True)

    def __str__(self):
        return self.name


# not use
class Job2(models.Model):
    category=models.ForeignKey(Category2,on_delete=CASCADE)
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=50,null=True)
    city=models.CharField(max_length=200)
    location=models.CharField(max_length=300)
    timing=models.CharField(max_length=100)
    salary=models.IntegerField()
    desc=models.TextField()
    
    def __str__(self) :
        return self.name




# not use
class JobApply(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    criteria=models.CharField(max_length=200)
    exp=models.IntegerField()
    # resume=models.CharField(max_length=200)
    resume=models.FileField(upload_to='image',max_length=250,null=True,default=None)

    def __str__(self):
        return self.name


class Company(models.Model):
    name=models.CharField(max_length=200)
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)
    image=models.ImageField(upload_to='image')

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name=models.CharField(max_length=200)
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)
    image=models.ImageField(upload_to='image')

    def __str__(self):
        return self.name

class Curriculum(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    resume=models.FileField(upload_to='image',max_length=250,null=True,default=None)
    carrier=models.CharField(max_length=200)
    email=models.EmailField(blank=True,unique=False)
    
    salary=models.IntegerField()
    exp=models.IntegerField()
    desc=models.TextField()
   
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=200)
    desc=models.CharField(max_length=500)
    address=models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Service(models.Model):
    name=models.CharField(max_length=50)
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)

    def __str__(self):
        return self.name


class StudentUser(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE)
    mobile=models.CharField(max_length=15)
    image=models.FileField(null=True)
    gender=models.CharField(max_length=10)
    address=models.TextField(null=True)
    type=models.CharField(max_length=15)
    def __str__(self):
        return self.user.username

class Recruiter(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE)
    mobile=models.CharField(max_length=15)
    image=models.FileField(null=True)
    gender=models.CharField(max_length=10)
    company=models.CharField(max_length=100)
    type=models.CharField(max_length=15)
    status=models.CharField(max_length=20)
    def __str__(self):
        return self.user.username



class AddJob(models.Model):
    recruiter=models.ForeignKey(Recruiter,on_delete=CASCADE)
    title=models.CharField(max_length=200)
    start_date=models.DateField()
    end_date=models.DateField()
    logo=models.FileField()
    company_name=models.CharField(max_length=200)
    experience=models.CharField(max_length=50)
    city=models.CharField(max_length=200)
    location=models.CharField(max_length=300)
    salary=models.FloatField(max_length=20)
    desc=models.CharField(max_length=300)
    creationdate=models.DateField()

    def __str__(self):
        return self.title
    
class JobApplied(models.Model):
    job=models.ForeignKey(AddJob,on_delete=CASCADE)
    student=models.ForeignKey(StudentUser,on_delete=CASCADE)
    resume=models.FileField(null=True)
    applydate=models.DateField()
  
    def __str__(self) :
        return self.id

