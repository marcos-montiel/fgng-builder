# Generated by Django 4.2.7 on 2023-11-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("builder", "0002_alter_strenght_force_locked"),
    ]

    operations = [
        migrations.AlterField(
            model_name="strenght",
            name="force_locked",
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]