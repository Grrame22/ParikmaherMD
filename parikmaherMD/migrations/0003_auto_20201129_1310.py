# Generated by Django 3.1.3 on 2020-11-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parikmaherMD', '0002_auto_20201127_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hairdressing',
            name='adding_mage_1',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Добавочная фотография'),
        ),
    ]
