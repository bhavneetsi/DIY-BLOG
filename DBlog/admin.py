from django.contrib import admin
from DBlog.models import blog,Comments,Author_bio
# Register your models here.

admin.site.register(blog)
admin.site.register(Comments)
admin.site.register(Author_bio)