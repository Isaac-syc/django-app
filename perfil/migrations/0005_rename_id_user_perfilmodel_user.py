# Generated by Django 4.0.1 on 2022-03-10 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_rename_user_perfilmodel_id_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfilmodel',
            old_name='id_user',
            new_name='user',
        ),
    ]