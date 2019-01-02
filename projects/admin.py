from django.contrib import admin

# Register your models here.
from projects.models import Project, Category

class ProjectsInline(admin.TabularInline):
    model = Project

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    inlines = [ProjectsInline]

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'video', 'description', 'is_principal')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
