# Generated by Django 4.1.7 on 2023-03-11 08:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tiqo_parser', '0018_transaction_beneficiary_transaction_reference_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OdooContact',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('type', models.CharField(choices=[('M', 'membership'), ('B', 'beneficiarie')], max_length=1)),
            ],
        ),
    ]
