# Generated by Django 5.1.3 on 2025-03-04 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='uploaded_at',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='posts',
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_tags', to='posts.post')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_tags', to='posts.tag')),
            ],
        ),
    ]
