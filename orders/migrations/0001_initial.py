# Generated by Django 2.0.6 on 2018-07-11 03:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('type', models.CharField(choices=[('fish', 'Fish'), ('meat', 'Meat')], max_length=40)),
                ('delivery_address', models.TextField()),
                ('company_name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('processed', 'PROCESSED'), ('completed', 'COMPLETED')], default='pending', max_length=20)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.User')),
            ],
            options={
                'verbose_name_plural': 'Orders',
                'ordering': ['-timestamp'],
            },
        ),
    ]
