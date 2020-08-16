from django.contrib import admin
from projects.models import Project,Details,Comment,Reviews

# Register your models here.
admin.site.register(Project)
admin.site.register(Details)
admin.site.register(Reviews)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('name','Comment','Details','created_on','active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'Comment')
    actions = ['approve_comments']
    def approve_comments(self, request, queryset):
        queryset.update(active=True)