# Generated by Django 2.2.1 on 2019-05-10 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0068_auto_20190509_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='donation_modals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='petition', to='wagtailpages.DonationModals'),
        ),
    ]
