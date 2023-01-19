# Generated by Django 3.2.16 on 2023-01-03 11:53

from django.db import migrations


def remove_airtable_record_id(apps, schema_editor):
    migrations.RemoveField(
        model_name="productpage",
        name="airtable_record_id",
    ),


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailpages", "0073_add_accordion_to_primary_page"),
    ]

    operations = [migrations.RunPython(remove_airtable_record_id)]
