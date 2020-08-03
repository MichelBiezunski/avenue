# Generated by Django 3.0.8 on 2020-08-02 03:59

from django.db import migrations
import inside.blocks
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('inside', '0003_auto_20200801_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insidepage',
            name='body',
            field=wagtail.core.fields.StreamField([('one_column', wagtail.core.blocks.StructBlock([('one_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(required=False)), ('carousel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('0%', '0%'), ('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')])), ('images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False)), ('description', wagtail.core.blocks.TextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(help_text='Enter Link to web page', required=False))]), icon='image', template='include/bcarousel.html'))], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('media', inside.blocks.MediaBlock(required=False))], icon='arrow-left', label='One column', required=False))])), ('two_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('media', inside.blocks.MediaBlock(required=False))], icon='arrow-left', label='Left column content', required=False)), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('media', inside.blocks.MediaBlock(required='False'))], icon='arrow-right', label='Right column content', required=False))])), ('three_columns', wagtail.core.blocks.StructBlock([('background', wagtail.core.blocks.ChoiceBlock(choices=[('black', 'black'), ('#1b143b', 'navy1'), ('#211849', 'navy2'), ('white', 'white'), ('#e6e6e6', 'light gray'), ('red', 'red'), ('blue', 'blue'), ('green', 'green')])), ('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('media', inside.blocks.MediaBlock(required=False))], icon='arrow-left', label='Left column content')), ('middle_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('media', inside.blocks.MediaBlock(required=False))], icon='arrow-down', label='Middle column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('media', inside.blocks.MediaBlock())], icon='arrow-right', label='Right column content', required=False))])), ('six_columns', wagtail.core.blocks.StructBlock([('column1', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.RichTextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))])), ('column2', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.RichTextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))])), ('column3', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.RichTextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))])), ('column4', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.RichTextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))])), ('column5', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.RichTextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))])), ('column6', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.RichTextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]))])), ('carousel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('0%', '0%'), ('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')])), ('images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False)), ('description', wagtail.core.blocks.TextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(help_text='Enter Link to web page', required=False))]), icon='image', template='include/bcarousel.html'))])), ('media', inside.blocks.MediaBlock()), ('map', wagtail.core.blocks.StructBlock([('marker_title', wagtail.core.blocks.CharBlock(default="Marker Title 'This will be updated after you save changes.'", max_length=120)), ('marker_description', wagtail.core.blocks.RichTextBlock()), ('zoom_level', wagtail.core.blocks.IntegerBlock(default='2', max_value=18, min_value=0, required=False)), ('location_x', wagtail.core.blocks.FloatBlock(default='35.0', required=False)), ('location_y', wagtail.core.blocks.FloatBlock(default='0.16', required=False)), ('marker_x', wagtail.core.blocks.FloatBlock(default='51.5', required=False)), ('marker_y', wagtail.core.blocks.FloatBlock(default='-0.09', required=False))]))], blank=True, null=True),
        ),
    ]
