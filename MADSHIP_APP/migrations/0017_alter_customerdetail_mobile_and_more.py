# Generated by Django 4.2.4 on 2023-10-31 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MADSHIP_APP', '0016_alter_customerdetail_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetail',
            name='mobile',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='pincode',
            field=models.PositiveIntegerField(),
        ),
    ]
