# Generated by Django 5.1.4 on 2025-01-02 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_group_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='group_id',
            new_name='group',
        ),
    ]
