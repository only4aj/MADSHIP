# Generated by Django 4.2.5 on 2023-11-05 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MADSHIP_APP', '0023_customerdetail_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('desc', models.CharField(max_length=5000)),
            ],
        ),
    ]
