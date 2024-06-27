# Generated by Django 5.0.6 on 2024-06-27 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Patients', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('billing_id', models.AutoField(primary_key=True, serialize=False)),
                ('services', models.TextField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(max_length=50)),
                ('billing_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('inpatient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patients.inpatient')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patients.patient')),
            ],
        ),
    ]