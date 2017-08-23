from django.contrib import admin
from blog.models import Category, Meme

# Register your models here.


class MemeAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ('id', 'image', 'category', 'pub_date')
    list_filter = ('pub_date',)


admin.site.register(Category)
admin.site.register(Meme, MemeAdmin)
