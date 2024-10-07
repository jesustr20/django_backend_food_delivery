# Generated by Django 5.1.1 on 2024-10-06 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255)),
                ('district', models.CharField(blank=True, max_length=255)),
                ('province', models.CharField(blank=True, max_length=255)),
                ('department', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('postal_code', models.CharField(blank=True, max_length=20)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
