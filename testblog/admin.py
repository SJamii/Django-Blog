from django.contrib import admin
from .models import Posts,Author,Category
admin.site.register(Posts)
admin.site.register(Author)
admin.site.register(Category)