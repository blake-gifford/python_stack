from django.db import models


class ShowManager(models.Manager):
    def validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 1:
            errors['title'] = "Please enter in TV Show title in the field provided!"
        if len(post_data['network']) < 1:
            errors['network'] = "Name of Network must be entered."
        if len(post_data['release_date']) < 1:
            errors['release_date'] = "You must enter a date."
        if len(post_data['description']) < 1:
            errors['description'] = "You must enter a description."
        return errors


class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255, default = 'no description')
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()

# Create your models here.
