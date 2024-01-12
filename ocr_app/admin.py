from django.contrib import admin

# Register your models here.
from ocr_app.models import *
admin.site.register(documents)

admin.site.register(studies)

admin.site.register(userprofile)

admin.site.register(File)
admin.site.register(comments)
admin.site.register(replies)