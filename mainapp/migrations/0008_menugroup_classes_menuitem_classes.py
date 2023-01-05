# Generated by Django 4.1.4 on 2023-01-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0007_remove_menugroup_html_remove_menugroup_styles"),
    ]

    operations = [
        migrations.AddField(
            model_name="menugroup",
            name="classes",
            field=models.CharField(default="menu", max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="menuitem",
            name="classes",
            field=models.CharField(default="item", max_length=64),
            preserve_default=False,
        ),
    ]