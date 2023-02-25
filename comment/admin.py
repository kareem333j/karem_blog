from django.contrib import admin
from .models import Comment, Report, Admin,Edit
# Register your models here.

class CommentUser(admin.ModelAdmin):
    list_display = ["name","comment","activate"]
    list_editable = ["activate"]

class AdminUser(admin.ModelAdmin):
    list_display = ["name_admin","activate"]
    list_editable = ["activate"]

admin.site.register(Comment,CommentUser)
admin.site.register(Report)
admin.site.register(Edit)
admin.site.register(Admin,AdminUser)

