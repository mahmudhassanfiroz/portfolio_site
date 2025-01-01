from django.contrib import admin
from .models import Project


# Registering the Project model
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'technology', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'technology')
    list_filter = ('technology',)
    prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug based on title
    ordering = ('-created_at',)

admin.site.register(Project, ProjectAdmin)
