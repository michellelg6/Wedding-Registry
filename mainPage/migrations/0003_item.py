# Generated by Django 3.1.5 on 2021-02-03 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0002_auto_20210203_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('caption', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='mainPage/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
