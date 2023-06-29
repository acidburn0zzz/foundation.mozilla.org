# Generated by Django 3.2.19 on 2023-06-29 02:02

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0090_remove_research_prefixes'),
    ]

    operations = [
        migrations.AddField(
            model_name='rcclandingpage',
            name='body',
            field=wagtail.fields.StreamField([('about', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('image_alt_text', wagtail.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('heading', wagtail.blocks.CharBlock(help_text='Heading for the About Block')), ('content', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link']))]))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AddField(
            model_name='researchlandingpage',
            name='body',
            field=wagtail.fields.StreamField([('about', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('image_alt_text', wagtail.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('heading', wagtail.blocks.CharBlock(help_text='Heading for the About Block')), ('content', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link']))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
