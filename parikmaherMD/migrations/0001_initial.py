# Generated by Django 3.1.3 on 2020-11-27 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название райнона')),
            ],
        ),
        migrations.CreateModel(
            name='Hairdressing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('phone', models.CharField(max_length=20, unique=True, verbose_name='Телефон')),
                ('main_image', models.ImageField(blank=True, upload_to='', verbose_name='Фотографии на главную')),
                ('adding_mage_1', models.ImageField(blank=True, upload_to='', verbose_name='Добавочная фотография')),
                ('adding_image_2', models.ImageField(blank=True, upload_to='', verbose_name='Добавочная фотография')),
                ('adding_image_3', models.ImageField(blank=True, upload_to='', verbose_name='Добавочная фотография')),
                ('description', models.TextField(verbose_name='Описание')),
                ('address_location', models.CharField(max_length=100, unique=True, verbose_name='Адресс')),
                ('schedule_for_calculating', models.TextField(verbose_name='Расписание(для расчёта)')),
                ('schedule_for_clients', models.TextField(verbose_name='Расписание(для клиентов)')),
                ('specializations', models.TextField(verbose_name='Специализации')),
                ('price_list', models.TextField(verbose_name='Тарифы')),
                ('sales', models.TextField(blank=True, verbose_name='Скидки')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parikmaherMD.area')),
            ],
        ),
    ]
