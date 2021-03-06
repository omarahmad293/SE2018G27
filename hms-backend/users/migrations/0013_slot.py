# Generated by Django 2.1.3 on 2019-02-06 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_medicine_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('max_no', models.IntegerField()),
                ('available_no', models.IntegerField(default=0)),
                ('is_open', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='users.HMSProfile')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
    ]
