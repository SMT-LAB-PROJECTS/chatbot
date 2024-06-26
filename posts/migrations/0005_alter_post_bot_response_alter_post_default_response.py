# Generated by Django 5.0.4 on 2024-05-02 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0002_alter_answer_options'),
        ('posts', '0004_alter_post_bot_response_alter_post_default_response'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bot_response',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bot_response', to='answers.answer'),
        ),
        migrations.AlterField(
            model_name='post',
            name='default_response',
            field=models.ManyToManyField(blank=True, null=True, related_name='default_response', to='questions.qustion'),
        ),
    ]
