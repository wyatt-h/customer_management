# Generated by Django 3.1.4 on 2020-12-23 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201222_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=200, null=True),
        ),
    ]