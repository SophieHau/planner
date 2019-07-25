from django.db import models


class Guest(models.Model):
    
    INVITATION_STATUS = [
        ('sent', 'Invitation has been sent'),
        ('not_sent', 'Invitation has not been sent')
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    invitation_status = models.CharField(max_length=10, choices=INVITATION_STATUS, default='not_sent')
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)