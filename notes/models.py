from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    name=models.CharField(max_length=150)
    image=models.ImageField(upload_to='notes/')
    created_At=models.DateTimeField(auto_now_add=True)
    description=models.TextField(default='')

    def __str__(self):
        return self.name
    
# one to many 
class Reviews(models.Model):
    chai=models.ForeignKey(Note,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='reviews')
    rating=models.IntegerField()
    comment=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
# Many to Many
class store(models.Model):
    name=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    note_varities=models.ManyToManyField(Note,related_name="note_varities")

# One to One
class certificate(models.Model):
    note=models.OneToOneField(Note,on_delete=models.CASCADE,related_name='certificate')
    certificate_name=models.CharField(max_length=150)
    issue_date=models.DateTimeField(auto_now_add=True)
    valid_until=models.DateTimeField()

    def __str__(self):
        return f'Certificate Number is: {self.name.note}'
        
