from django.db import models

class skill(models.Model):
    skill_name = models.CharField(max_length=250, null=True, blank=True)
    

    def __str__(self):
        return self.skill_name
    
class SubSkill(models.Model):
    skill = models.ForeignKey(skill, on_delete=models.CASCADE, related_name='subskills')
    subskill_name = models.CharField(max_length=250, null=True, blank=True)
    skill_percentage = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.subskill_name} - {self.skill_percentage}%"


class Home(models.Model):
    subskills = models.ManyToManyField(SubSkill, blank=True)
    username = models.CharField(max_length=250, null=True, blank=True)
    designation = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    resume = models.FileField(upload_to='files/', null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.designation}- {self.subskills}"
    
class Projects(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    environment = models.CharField(max_length=250, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    roles_and_responsibilities = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    company_name = models.CharField(max_length=250, null=True, blank=True)
    designation = models.CharField(max_length=250, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.company_name
    
class SocialMediaLink(models.Model):
    platform_name = models.CharField(max_length=250, null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.platform_name
class Contact(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    social_media_links = models.ManyToManyField (SocialMediaLink,related_name='contacts', blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

