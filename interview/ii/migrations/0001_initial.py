# Generated by Django 3.2.5 on 2022-09-20 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=264, unique=True)),
                ('name', models.CharField(max_length=264)),
                ('password', models.CharField(max_length=264)),
            ],
        ),
    ]
