from django.contrib import admin

from .models import Blog, Category, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass  


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
