from django.db import models


class MenuGroup(models.Model):
    name = models.CharField(max_length=32)
    classes = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=32)
    menu = models.ForeignKey(
        MenuGroup, on_delete=models.CASCADE, related_name="menu_items"
    )
    classes = models.CharField(max_length=64, blank=True)
    dropdown_links = models.ManyToManyField("self")
    dropdown = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Logo(models.Model):
    logo = models.ImageField(upload_to="logos")
    menu = models.ForeignKey(MenuGroup, on_delete=models.CASCADE, related_name="logo")
    classes = models.CharField(max_length=64, blank=True)
