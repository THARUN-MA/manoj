# Generated by Django 3.2.5 on 2022-11-09 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ii', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='userfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='')),
                ('aid', models.CharField(max_length=264)),
                ('title', models.CharField(max_length=264)),
            ],
        ),
    ]
