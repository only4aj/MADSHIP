# Generated by Django 4.2.5 on 2023-10-21 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MADSHIP_APP', '0006_productitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='details',
            field=models.CharField(default='Default Value', max_length=1000),
        ),
        migrations.AddField(
            model_name='productitem',
            name='width',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='image',
            field=models.ImageField(upload_to='images', width_field='width'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MADSHIP_APP.productitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MADSHIP_APP.customer')),
            ],
        ),
    ]