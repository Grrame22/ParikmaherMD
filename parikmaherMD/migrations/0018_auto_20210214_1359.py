# Generated by Django 3.1.3 on 2021-02-14 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parikmaherMD', '0017_auto_20210213_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hairdressing',
            name='services_for_face_and_body',
        ),
        migrations.AddField(
            model_name='hairdressing',
            name='services_for_body',
            field=models.TextField(blank=True, verbose_name='Услуги для тела'),
        ),
        migrations.AddField(
            model_name='hairdressing',
            name='services_for_eyebrows',
            field=models.TextField(blank=True, verbose_name='Услуги для бровей'),
        ),
        migrations.AddField(
            model_name='hairdressing',
            name='services_for_face',
            field=models.TextField(blank=True, verbose_name='Услуги для лица'),
        ),
    ]
