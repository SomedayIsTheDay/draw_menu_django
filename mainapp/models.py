from django.db import models


class Logo(models.Model):
    name = models.CharField(max_length=32)
    logo = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class TextElements(models.Model):
    font_family = models.CharField(max_length=64)
    font_family_generic = models.CharField(max_length=32)
    font_size = models.IntegerField()
    color = models.CharField(max_length=32)


class Menu(models.Model):
    name = models.CharField(max_length=32)
    logo = models.OneToOneField(Logo, on_delete=models.CASCADE)
    elements = models.ForeignKey(TextElements, on_delete=models.CASCADE)
    background_color = models.CharField(max_length=32)
    padding = models.IntegerField()
