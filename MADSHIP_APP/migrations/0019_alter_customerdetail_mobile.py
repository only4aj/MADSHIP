# Generated by Django 4.2.4 on 2023-10-31 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MADSHIP_APP', '0018_alter_customerdetail_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetail',
            name='mobile',
            field=models.PositiveBigIntegerField(),
        ),
    ]
