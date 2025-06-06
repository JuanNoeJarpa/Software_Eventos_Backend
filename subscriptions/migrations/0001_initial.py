# Generated by Django 5.2 on 2025-05-05 01:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0002_alter_company_logo_url_alter_company_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_type', models.CharField(choices=[('monthly', 'Plan Mensual'), ('biannual', 'Plan Semestral'), ('annual', 'Plan Anual')], max_length=20)),
                ('status', models.CharField(choices=[('active', 'Activa'), ('past_due', 'Pago Pendiente'), ('canceled', 'Cancelada'), ('expired', 'Expirada')], default='active', max_length=20)),
                ('stripe_customer_id', models.CharField(blank=True, max_length=100, null=True)),
                ('stripe_subscription_id', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='companies.company')),
            ],
        ),
    ]
