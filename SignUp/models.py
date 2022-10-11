from django.db import models
from django.contrib.auth.models import User 

class IlkmsUser(User):

    occupation = models.CharField(max_length=64)
    user_type = models.CharField(max_length=64, null=True, default="general_user")

    

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'ilkms_users'
