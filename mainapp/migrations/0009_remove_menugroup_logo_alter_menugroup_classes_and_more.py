# Generated by Django 4.1.4 on 2023-01-04 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0008_menugroup_classes_menuitem_classes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menugroup",
            name="logo",
        ),
        migrations.AlterField(
            model_name="menugroup",
            name="classes",
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name="menuitem",
            name="classes",
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.CreateModel(
            name="Logo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("logo", models.ImageField(upload_to="logos")),
                ("classes", models.CharField(blank=True, max_length=64)),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="logo",
                        to="mainapp.menugroup",
                    ),
                ),
            ],
        ),
    ]
