# Generated by Django 4.1.7 on 2023-04-21 17:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_delete_viewlinksmodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="linkshortenermodel",
            name="orginal_url",
            field=models.URLField(max_length=1000),
        ),
    ]
