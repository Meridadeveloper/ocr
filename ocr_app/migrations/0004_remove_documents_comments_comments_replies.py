# Generated by Django 5.0.1 on 2024-01-12 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr_app', '0003_alter_studies_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='comments',
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocr_app.documents')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocr_app.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='replies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocr_app.comments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocr_app.userprofile')),
            ],
        ),
    ]