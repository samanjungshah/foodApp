from dataclasses import fields
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


    


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    img = models.CharField(max_length=500,default='https://cdn.dribbble.com/users/1012566/screenshots/4187820/media/985748436085f06bb2bd63686ff491a5.jpg?compress=1&resize=400x300&vertical=top')
    def __str__(self):
        return self.item_name
    
    
    # Queryset is collection of objects stored in database
    # Manager is something we have at least in one model
    # Model makes simple to interact with database ,it uses orm(object relational mapper) for sql commands
    # item.objects.all()
    # where item is model , object is Manager and all is Method

class ItemInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    
    item = models.ForeignKey('Item',on_delete=models.SET_NULL,null=True)
    ordered_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.item.item_name
    

    