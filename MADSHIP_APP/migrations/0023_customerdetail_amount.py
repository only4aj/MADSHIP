# Generated by Django 4.2.5 on 2023-11-04 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MADSHIP_APP', '0022_alter_customerdetail_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdetail',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
