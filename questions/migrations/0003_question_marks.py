# Generated by Django 5.0 on 2024-06-05 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_alter_question_options_four_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='marks',
            field=models.IntegerField(default=5),
        ),
    ]
