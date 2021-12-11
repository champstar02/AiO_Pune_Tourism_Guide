# Generated by Django 2.2.2 on 2019-07-30 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(null=True, upload_to='')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tourist.Category')),
                ('select_city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tourist.Select_City')),
            ],
        ),
    ]
