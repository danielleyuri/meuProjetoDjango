# Generated by Django 3.2.6 on 2021-08-05 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_alter_transacao_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='date_criacao',
            new_name='dt_criacao',
        ),
    ]
