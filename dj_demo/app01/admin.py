from django.contrib import admin
from app01 import models

# Register your models here.


@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')



@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')


# admin.site.register(models.UserProfile)