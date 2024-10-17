from django.contrib import admin
from feedback.models import feedbackform

class  feedbackadmin(admin.ModelAdmin):
  list_display=['name','feedback']
admin.site.register(feedbackform,feedbackadmin)
