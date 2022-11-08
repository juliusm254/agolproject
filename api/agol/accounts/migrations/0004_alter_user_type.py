# Generated by Django 3.2.15 on 2022-11-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('OPERATIONS', 'Operations'), ('CUSTOMER', 'Customer'), ('ADMIN', 'Admin')], max_length=25),
        ),
    ]
