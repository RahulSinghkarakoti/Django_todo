# Generated by Django 5.0.6 on 2024-06-28 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todos_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='todo_id',
            field=models.CharField(default='your_default_value', max_length=100),
        ),
        migrations.AlterField(
            model_name='todos',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
