# Generated by Django 3.1.6 on 2021-03-18 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_num_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='store.product'),
        ),
    ]
