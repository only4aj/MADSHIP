# Generated by Django 4.2.4 on 2023-10-31 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MADSHIP_APP', '0013_alter_customerdetail_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetail',
            name='mail',
            field=models.EmailField(max_length=254),
        ),
    ]
