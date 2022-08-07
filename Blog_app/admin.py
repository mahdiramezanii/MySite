from django.contrib import admin

from .models import Blog,Category,comment

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(comment)
