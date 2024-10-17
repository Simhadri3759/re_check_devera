from django.db import models
class feedbackform(models.Model):
  name=models.CharField(max_length=30)
  feedback=models.TextField(max_length=100)
