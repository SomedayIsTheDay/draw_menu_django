# Generated by Django 4.1.4 on 2023-01-04 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0006_alter_menugroup_name_menuitem"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menugroup",
            name="html",
        ),
        migrations.RemoveField(
            model_name="menugroup",
            name="styles",
        ),
    ]