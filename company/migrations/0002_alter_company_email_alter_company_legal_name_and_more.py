# Generated by Django 4.1.2 on 2023-03-20 11:51

import company.business_logic
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(db_index=True, error_messages={'unique': 'Not a valid email. Enter again and correctly.'}, max_length=50, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='company',
            name='legal_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='legal_name'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, height_field='url_height', null=True, upload_to=company.business_logic.user_directory_path, validators=[company.business_logic.validate_image_size], width_field='url_width'),
        ),
    ]
