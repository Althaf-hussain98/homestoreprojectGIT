# Generated by Django 4.1 on 2022-09-22 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homestoreapp', '0007_remove_products_productid_buying_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buying',
            name='paymwnt',
            field=models.CharField(default='Pending', max_length=255),
        ),
    ]
