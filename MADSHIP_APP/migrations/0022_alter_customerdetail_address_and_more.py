# Generated by Django 4.2.5 on 2023-11-03 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MADSHIP_APP', '0021_alter_customerdetail_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetail',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
