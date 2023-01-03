from django.db import models


class MenuGroup(models.Model):
    name = models.CharField(max_length=50)
    styles = models.TextField()

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        MenuGroup, on_delete=models.CASCADE, related_name="menu_items"
    )
    text = models.CharField(max_length=50)
    url = models.TextField()
    styles = models.TextField()

    def __str__(self):
        return self.text


class Logo(models.Model):
    menu = models.ForeignKey(MenuGroup, on_delete=models.CASCADE, related_name="logo")
    image = models.ImageField(upload_to="logos")
    styles = models.TextField()

    def __str__(self):
        return f"{self.menu} logo"
