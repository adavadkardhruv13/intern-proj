# Generated by Django 4.0.1 on 2023-10-04 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_listing_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='ends_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='URL',
            field=models.ImageField(upload_to=''),
        ),
    ]
