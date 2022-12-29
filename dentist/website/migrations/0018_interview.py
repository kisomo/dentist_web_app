# Generated by Django 4.1 on 2022-12-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_alter_jobdata_education_alter_jobdata_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=200, verbose_name='Last Name')),
                ('interview_time', models.DateTimeField(blank=True, null=True, verbose_name='Interview Time')),
                ('interviewer', models.CharField(max_length=200, verbose_name='Interviewer')),
            ],
        ),
    ]
