from rest_framework import serializers
from .models import  Home, SubSkill, Projects, Experience, Contact, SocialMediaLink
from collections import defaultdict


class HomeSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField()
    class Meta:
        model = Home
        fields = ['id', 'username', 'designation', 'description', 'image', 'resume','skills']  # Include all fields from the Skill model

    def get_skills(self, obj):
        grouped = defaultdict(list)
        for subskill in obj.subskills.all():
            grouped[subskill.skill.skill_name].append({
                'id': subskill.id,
                'subskill_name': subskill.subskill_name,
                'skill_percentage': subskill.skill_percentage
            })
        return [{'skill_name': k, 'subskills': v} for k, v in grouped.items()]
    
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'image', 'link', 'environment', 'start_date', 'end_date', 'roles_and_responsibilities']  # Include all fields from the Skill model

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'company_name', 'designation', 'start_date', 'end_date', 'description']  # Include all fields from the Skill model

class socialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = ['id', 'platform_name', 'link']  # Include all fields from the Skill model

class ContactSerializer(serializers.ModelSerializer):
    social_media_links = socialMediaLinkSerializer(many=True, read_only=True) 
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email','phone','image', 'message','social_media_links']  # Include all fields from the Skill model  