# Generated by Django 4.1.4 on 2023-01-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0013_menuitem_dropdown"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menuitem",
            name="dropdown_links",
        ),
        migrations.AddField(
            model_name="menuitem",
            name="dropdown_links",
            field=models.ManyToManyField(blank=True, null=True, to="mainapp.menuitem"),
        ),
    ]
