
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='subscription',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='plan_type',
            field=models.CharField(choices=[('monthly', 'Mensual'), ('biannual', 'Semestral'), ('annual', 'Anual')], max_length=20),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='status',
            field=models.CharField(choices=[('active', 'Activa'), ('past_due', 'Pago pendiente'), ('canceled', 'Cancelada'), ('incomplete', 'Incompleta'), ('incomplete_expired', 'Incompleta expirada'), ('trialing', 'En periodo de prueba'), ('unpaid', 'No pagada')], default='incomplete', max_length=20),
        ),
    ]
