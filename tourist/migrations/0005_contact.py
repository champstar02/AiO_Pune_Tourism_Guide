# Generated by Django 3.0.3 on 2021-01-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0004_places_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=15)),
                ('emailid', models.CharField(max_length=60)),
                ('subject', models.CharField(max_length=300)),
            ],
        ),
    ]
