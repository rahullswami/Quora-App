from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Space)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Notification)
admin.site.register(Follow)