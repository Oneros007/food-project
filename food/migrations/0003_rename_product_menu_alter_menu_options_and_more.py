# Generated by Django 4.0.6 on 2022-08-13 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_rename_updated_product_update'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Menu',
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'managed': True, 'verbose_name': 'Menu', 'verbose_name_plural': 'Menu'},
        ),
        migrations.AlterModelTable(
            name='menu',
            table='Menu',
        ),
    ]
