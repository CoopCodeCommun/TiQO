# Generated by Django 4.1.7 on 2023-03-10 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiqo_parser', '0008_alter_contact_email_alter_transaction_initiator_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]