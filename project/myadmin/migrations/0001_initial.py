# Generated by Django 4.0.5 on 2022-07-02 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('catid', models.AutoField(primary_key=True, serialize=False)),
                ('catnm', models.CharField(max_length=50)),
                ('caticonnm', models.CharField(max_length=100)),
            ],
        ),
    ]