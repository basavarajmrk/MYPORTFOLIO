from django.contrib import admin
from .models import skill, SubSkill, Home, Projects, Experience, SocialMediaLink, Contact
# Register your models here.

class SubSkillInline(admin.TabularInline):  
    model = SubSkill
    extra = 1

class SkillAdmin(admin.ModelAdmin):
    inlines = [SubSkillInline]
    list_display = ('skill_name',)

# class SubSkillAdmin(admin.ModelAdmin):
#     model = SubSkill
#     list_display = ('skill', 'subskill_name', 'skill_percentage')
#     search_fields = ('subskill_name',)
#     list_filter = ('skill',)

class HomeAdmin(admin.ModelAdmin):
    model = Home
    list_display = ('username', 'designation', 'description', 'image', 'resume')
    search_fields = ('username', 'designation')
    list_filter = ('username', 'designation')

class ProjectsAdmin(admin.ModelAdmin):  
    model = Projects
    list_display = ('title', 'description', 'image', 'link', 'environment', 'start_date', 'end_date', 'roles_and_responsibilities')
    search_fields = ('title',)
    list_filter = ('start_date', 'end_date')

class ExperienceAdmin(admin.ModelAdmin):
    model = Experience
    list_display = ('company_name', 'designation', 'start_date', 'end_date', 'description')
    search_fields = ('company_name',)
    list_filter = ('start_date', 'end_date')

# class SocialMediaLinkAdmin(admin.TabularInline):
#     model = SocialMediaLink
#     extra = 1

class ContactAdmin(admin.ModelAdmin):
    model = Contact
    # inlines = [SocialMediaLinkAdmin]
    list_display = ('name', 'email', 'message',)
    search_fields = ('name', 'email')
    list_filter = ('name',)

admin.site.register(skill, SkillAdmin)
# admin.site.register(SubSkill, SubSkillAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(SocialMediaLink)
admin.site.register(Contact, ContactAdmin)
# admin.site.register(skill)