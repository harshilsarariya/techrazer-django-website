# Generated by Django 3.1.7 on 2021-04-09 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210407_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Coding', 'Coding'), ('Gadget', 'Gadget'), ('Technology', 'Technology'), ('Phone', 'Phone')], default='', max_length=255),
        ),
    ]
