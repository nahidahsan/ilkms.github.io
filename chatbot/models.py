from django.db import models
from django.contrib.auth.models import User 

class chatbot_history(models.Model):

    req = models.CharField(max_length=10000)
    res = models.CharField(max_length=10000, null=True)

    

    def __str__(self):
        return self.req + ' ' + self.res

    class Meta:
        db_table = 'chatbot_history'