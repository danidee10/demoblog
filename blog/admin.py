from django.contrib import admin
from .models import Post, Category, Comment

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

    def save_model(self, request, obj, form, change):
        """Set the author to the current logged in user."""
        if not obj.author:
            obj.author = request.user

        obj.save()

admin.site.register(Post, PostAdmin)
admin.site.register((Category, Comment))