# Generated by Django 4.0.5 on 2022-06-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('regid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=1000)),
                ('mobile', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=20)),
                ('status', models.IntegerField()),
                ('role', models.CharField(max_length=20)),
                ('dt', models.CharField(max_length=1000)),
            ],
        ),
    ]
