# Generated by Django 4.0.4 on 2022-05-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_email_alter_profile_age_alter_profile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='calories_exercise',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='calories_food',
            field=models.IntegerField(),
        ),
    ]
