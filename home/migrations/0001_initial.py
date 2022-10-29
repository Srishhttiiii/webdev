# Generated by Django 4.0.6 on 2022-09-19 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Blog',
            },
        ),
        migrations.CreateModel(
            name='Journaling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmpname', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('shortdescription', models.CharField(blank=True, max_length=100, null=True)),
                ('updatedat', models.DateTimeField(auto_now=True)),
                ('createdat', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Work Exp',
            },
        ),
        migrations.CreateModel(
            name='Meditation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Meditation',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Login',
            },
        ),
        migrations.CreateModel(
            name='Therapy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Therapy',
            },
        ),
    ]