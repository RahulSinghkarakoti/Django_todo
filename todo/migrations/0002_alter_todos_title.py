# Generated by Django 5.0.6 on 2024-06-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
