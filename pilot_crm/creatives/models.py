from django.db import models


# Create your models here.
class Creative(models.Model):
    content = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        app_label = 'pilot_crm'  # Set the app label here
