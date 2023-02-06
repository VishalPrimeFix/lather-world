# Generated by Django 4.0.5 on 2022-07-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('subcatid', models.AutoField(primary_key=True, serialize=False)),
                ('catnm', models.CharField(max_length=50, unique=True)),
                ('subcatnm', models.CharField(max_length=50, unique=True)),
                ('subcaticonnm', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='catnm',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
