# Generated by Django 3.2.15 on 2022-11-04 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20221103_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('OPERATIONS', 'OperationsUser'), ('CUSTOMER', 'CustomerUser'), ('ADMIN', 'AdminUser')], max_length=50, verbose_name='Type'),
        ),
    ]