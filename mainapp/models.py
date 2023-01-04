from django.db import models


class MenuGroup(models.Model):
    name = models.CharField(max_length=32)
    logo = models.ImageField(upload_to="logos")

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=32)
    menu = models.ForeignKey(
        MenuGroup, on_delete=models.CASCADE, related_name="menu_items"
    )

    def __str__(self):
        return self.name
