from django.db import models
from django.template.defaultfilters import slugify

class Game(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    url = models.CharField(max_length=255, default='#')

    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        ordering = ('-id',)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)



class GameImage(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE, primary_key=True, related_name='image')
    url = models.CharField(max_length=255)