# Generated by Django 4.2.5 on 2023-11-05 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MADSHIP_APP', '0025_alter_customer_pnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='PNumber',
            field=models.PositiveBigIntegerField(),
        ),
    ]
