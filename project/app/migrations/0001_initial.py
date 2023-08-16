# Generated by Django 4.2.4 on 2023-08-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDataBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Contact', models.IntegerField()),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EnquiryDataBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Studentname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Contact', models.IntegerField()),
                ('Enquiry', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserDataBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Contact', models.IntegerField()),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]
