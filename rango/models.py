from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# A model is the single, definitive source of information about your data.
# It contains the essential fields and behaviors of the data you’re storing.
# Generally, each model maps to a single database table.

# If changes are made, must register them using manage.py makemigrations


class Category(models.Model):
    max_name_length = 128
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, models.CASCADE)
    max_title_length = 128
    title = models.CharField(max_length=max_title_length)
    max_url_length = 200    # might need to remove, also the reference in forms
    url = models.URLField()
    views = models.IntegerField(default=max_url_length)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username
