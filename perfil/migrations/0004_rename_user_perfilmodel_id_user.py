# Generated by Django 4.0.1 on 2022-03-10 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_remove_perfilmodel_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfilmodel',
            old_name='user',
            new_name='id_user',
        ),
    ]