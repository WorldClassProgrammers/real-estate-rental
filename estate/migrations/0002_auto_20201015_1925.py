# Generated by Django 3.1 on 2020-10-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='contract_over',
        ),
        migrations.AlterField(
            model_name='condo',
            name='common_fee_account',
            field=models.TextField(max_length=25),
        ),
        migrations.AlterField(
            model_name='condo',
            name='juristic_persons_number',
            field=models.TextField(max_length=25),
        ),
    ]
