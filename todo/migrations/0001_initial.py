# Generated by Django 5.1.1 on 2024-09-18 09:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
