# Generated by Django 4.1.1 on 2022-10-05 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=50)),
                ('nim', models.CharField(max_length=50)),
                ('nama', models.CharField(max_length=50)),
                ('ttl', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
