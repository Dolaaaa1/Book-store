# Generated by Django 4.2.4 on 2023-09-03 15:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0003_book_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Auther",
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
                ("first_name", models.CharField(max_length=100)),
                ("list_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="book",
            name="rating",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="slug",
            field=models.SlugField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="book",
            name="auther",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="book_outlet.auther",
            ),
        ),
    ]
