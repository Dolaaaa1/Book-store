# Generated by Django 4.2.4 on 2023-09-04 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0004_auther_alter_book_rating_alter_book_slug_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="auther",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books",
                to="book_outlet.auther",
            ),
        ),
    ]