# Generated by Django 2.1.3 on 2019-02-02 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_subjects_sub_syllabus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='sub_syllabus',
        ),
    ]