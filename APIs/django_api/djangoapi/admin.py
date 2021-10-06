from django.contrib import admin
from django.contrib.auth.models import Group, User
from djangoapi.models import *

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.site_header = "Apis Admin"

#Article Model
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','text','created_at','updated_at')
    list_filter = ['created_at']
    search_fields = ['title','text','created_at']
admin.site.register(Article, ArticleAdmin)

#Person Model
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','created_at','updated_at')
    list_filter = ['first_name','created_at']
    search_fields = ['first_name','last_name','email','created_at']

    #concating first_name and last_name in one column
    def full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)
admin.site.register(Person, PersonAdmin)