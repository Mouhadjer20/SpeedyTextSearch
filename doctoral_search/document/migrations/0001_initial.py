# Generated by Django 5.1 on 2025-04-04 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('author', models.CharField(max_length=255, verbose_name='Author')),
                ('keywords', models.JSONField(default=list)),
                ('publication_date', models.DateField()),
                ('university', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='uploads/research_papers/')),
                ('file_size', models.PositiveIntegerField(blank=True, null=True)),
                ('file_hash', models.CharField(max_length=64, unique=True)),
                ('file_type', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
