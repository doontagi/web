# Generated by Django 2.1.5 on 2019-02-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('introduction', models.TextField()),
                ('area', models.CharField(max_length=15)),
                ('party_number', models.IntegerField(default=0)),
            ],
        ),
    ]
