from django.db import models
from datetime import datetime


#bellow is our model
class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    
    #basically its the main field we want to refer to - name 
    def __str__(self):
        return self.name

#firts create new app python manage.py startapp contacts 
#then add this app in the installed apps in the btre settings  
#then create a model-funcion (as above)
#after creating model above we want to create tables, so we need to make migrations as a next stet[]
#python manage.py makemigrations contacts 
#python manage.py migrate (to migrate the data), if you want to check then 