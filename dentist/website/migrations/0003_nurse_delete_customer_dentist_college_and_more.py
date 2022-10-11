# Generated by Django 4.1 on 2022-10-11 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_venue_alter_upcomming_apt_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200, verbose_name='Nurse First Name')),
                ('lname', models.CharField(max_length=200, verbose_name='Nurse Last Name')),
                ('phone', models.CharField(max_length=25, verbose_name='Nurse Phone')),
                ('emial', models.EmailField(max_length=25, verbose_name='Nurse Email')),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AddField(
            model_name='dentist',
            name='college',
            field=models.CharField(choices=[('CUN', 'CUNY'), ('NYU', 'NYU'), ('MIT', 'MIT')], max_length=3, null=True, verbose_name='Doctor College'),
        ),
        migrations.AddField(
            model_name='dentist',
            name='experience_yrs',
            field=models.IntegerField(null=True, verbose_name='Doctor Experience yrs'),
        ),
        migrations.AddField(
            model_name='dentist',
            name='lname',
            field=models.CharField(max_length=200, null=True, verbose_name='Doctor Last Name'),
        ),
        migrations.AddField(
            model_name='dentist',
            name='qualification',
            field=models.CharField(choices=[('BA', 'Bachelors'), ('MA', 'Masters'), ('DR', 'PhD')], max_length=2, null=True, verbose_name='Doctor Degree'),
        ),
        migrations.AddField(
            model_name='finished_apt',
            name='apt_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Appointment Time'),
        ),
        migrations.AddField(
            model_name='finished_apt',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='finished_apt',
            name='doc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.dentist'),
        ),
        migrations.AddField(
            model_name='finished_apt',
            name='email_address',
            field=models.EmailField(blank=True, max_length=25, null=True, verbose_name='Customer Email'),
        ),
        migrations.AddField(
            model_name='finished_apt',
            name='is_done',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='finished_apt',
            name='lname',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Customer Last Name'),
        ),
        migrations.AddField(
            model_name='finished_apt',
            name='phone_number',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Customer Phone Number'),
        ),
        migrations.AddField(
            model_name='finished_apt',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.venue'),
        ),
        migrations.AlterField(
            model_name='dentist',
            name='fname',
            field=models.CharField(max_length=200, null=True, verbose_name='Doctor First Name'),
        ),
        migrations.AlterField(
            model_name='finished_apt',
            name='fname',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Customer First Name'),
        ),
        migrations.AlterField(
            model_name='upcomming_apt',
            name='apt_time',
            field=models.DateTimeField(verbose_name='Appointment Time'),
        ),
        migrations.AlterField(
            model_name='upcomming_apt',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='upcomming_apt',
            name='email_address',
            field=models.EmailField(max_length=25, verbose_name='Customer Email'),
        ),
        migrations.AlterField(
            model_name='upcomming_apt',
            name='fname',
            field=models.CharField(max_length=200, verbose_name='Customer First Name'),
        ),
        migrations.AlterField(
            model_name='upcomming_apt',
            name='lname',
            field=models.CharField(max_length=200, verbose_name='Customer Last Name'),
        ),
        migrations.AlterField(
            model_name='upcomming_apt',
            name='phone_number',
            field=models.CharField(max_length=25, verbose_name='Customer Phone Number'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='address',
            field=models.CharField(max_length=300, verbose_name='Venue Physical Address'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='email_address',
            field=models.EmailField(max_length=254, verbose_name='Venue Email Address'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='phone',
            field=models.CharField(max_length=25, verbose_name='Venue Phone'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='vname',
            field=models.CharField(max_length=200, verbose_name='Venue Name'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='web',
            field=models.URLField(verbose_name='Venue Website Address'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='zip_code',
            field=models.CharField(max_length=15, verbose_name='Venue Zip Code'),
        ),
        migrations.AddField(
            model_name='finished_apt',
            name='nurses',
            field=models.ManyToManyField(blank=True, null=True, to='website.nurse'),
        ),
        migrations.AddField(
            model_name='upcomming_apt',
            name='nurses',
            field=models.ManyToManyField(blank=True, to='website.nurse'),
        ),
    ]
