# Generated by Django 4.2.7 on 2023-11-27 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('disciplines', '0001_initial'),
        ('states', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='states.state'),
        ),
    ]
