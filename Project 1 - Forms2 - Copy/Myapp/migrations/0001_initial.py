# Generated by Django 4.2.6 on 2023-10-20 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.TextField()),
                ('Company', models.TextField()),
                ('closing_date', models.DateField()),
            ],
        ),
    ]