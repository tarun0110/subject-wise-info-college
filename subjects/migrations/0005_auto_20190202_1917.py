# Generated by Django 2.1.3 on 2019-02-02 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0004_topics_today'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topics_today',
            old_name='topic_today_text',
            new_name='topics_today_text',
        ),
    ]