# Generated by Django 4.1 on 2022-12-22 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_webdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cppdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200, verbose_name='File Name')),
                ('file_location', models.CharField(max_length=200, verbose_name='File Location')),
                ('file_extension', models.CharField(max_length=200, verbose_name='File Extension')),
            ],
        ),
    ]
