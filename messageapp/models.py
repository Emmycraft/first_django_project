from cgitb import text
from posixpath import split
from django.db import models

# Create your models here.
class message(models.Model):
    'creating a a database tjat accept a text input'
    text=models.TextField()
    
    '''make sure that the local server is terminated before creating a reference that 
    updates the preinstalled apps with a sql command that updates changes on the model
    '''
    def __str__(self) -> str:
        'this returns a model of this split lenght of the admin reference interface and on the client interface'
        #return self.text.split(' ')[0]       
        return self.text[:]
        