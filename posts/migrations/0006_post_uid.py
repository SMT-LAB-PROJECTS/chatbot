# Generated by Django 5.0.4 on 2024-05-06 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_bot_response_alter_post_default_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='uid',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
