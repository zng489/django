from django.db import models

import csv
from django.core.management.base import BaseCommand



# Create your models here
# 
# In Django, a "model" is a class that represents a database table.
# Each instance of the model class corresponds to a record in the table. 
# Django models are used to define and interact with the data in your application. 
# They provide a high-level abstraction for working with the database, allowing you to define the schema, manage data, and perform database operations using Python code.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15,
                                decimal_places=2, default=99.99)
    
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    def get_discount(self):
        return "122"



#####################################################################################
# GENERICS.LISTCREATEAPIVIEW 
#####################################################################################

class Data(models.Model):
    PIPELINE = models.CharField(max_length=255)
    FOLDER = models.CharField(max_length=255)
    SCRIPT = models.CharField(max_length=255)
    # Add fields corresponding to your CSV columns

    def __str__(self):
        return
        # return f'{self.column1} - {self.column2}'

# ['NAME_PIPELINE', 'FOLDER', 'BOT_SCRIPT_NAME']
# ['lnd_org_raw_aco_brasil_prod_aco_nacional', 'lnd/crw/aco_brasil', 'org_raw_aco_brasil_prod_aco_nacional']



#####################################################################################
# API_VIEW['POST', 'GET', 'DELETE', 'PUT']
#####################################################################################

class DataRecord(models.Model):
    PIPELINE = models.CharField(max_length=255)
    FOLDER = models.CharField(max_length=255)
    SCRIPT = models.CharField(max_length=255)
    # Add fields corresponding to your CSV columns
    
    def __str__(self):
        return 
        #return self.column1



