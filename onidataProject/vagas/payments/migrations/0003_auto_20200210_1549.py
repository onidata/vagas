# Generated by Django 2.2.10 on 2020-02-10 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20200208_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='contract_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payments', to='contracts.Contract', verbose_name='Related Contract'),
        ),
    ]