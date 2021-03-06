# Generated by Django 3.0.8 on 2020-07-23 15:02

from django.db import migrations, models
import django.db.models.deletion
import inside.blocks
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailimages', '0022_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mp4', models.CharField(blank=True, max_length=128, null=True)),
                ('header', models.CharField(blank=True, max_length=255, null=True)),
                ('subheader', models.TextField(blank=True, null=True)),
                ('button_text', models.CharField(default='Find Out More', max_length=50)),
                ('fallback', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=50, null=True)),
                ('content', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(template='blocks/image_block.html'))], blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InsidePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField([('one_column', wagtail.core.blocks.StructBlock([('one_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(required=False)), ('carousel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('0%', '0%'), ('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')])), ('images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False)), ('description', wagtail.core.blocks.TextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(help_text='Enter Link to web page', required=False))]), icon='image', template='include/bcarousel.html'))], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', inside.blocks.MediaBlock(required=False))], icon='arrow-left', label='One column', required=False))])), ('two_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('video', inside.blocks.MediaBlock(required=False))], icon='arrow-left', label='Left column content', required=False)), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('video', inside.blocks.MediaBlock(required='False'))], icon='arrow-right', label='Right column content', required=False))])), ('three_columns', wagtail.core.blocks.StructBlock([('background', wagtail.core.blocks.ChoiceBlock(choices=[('black', 'black'), ('#1b143b', 'navy1'), ('#211849', 'navy2'), ('white', 'white'), ('#e6e6e6', 'light gray'), ('red', 'red'), ('blue', 'blue'), ('green', 'green')])), ('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('video', inside.blocks.MediaBlock(required=False))], icon='arrow-left', label='Left column content')), ('middle_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('video', inside.blocks.MediaBlock(required=False))], icon='arrow-down', label='Middle column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('video', inside.blocks.MediaBlock())], icon='arrow-right', label='Right column content', required=False))])), ('six_columns', wagtail.core.blocks.StructBlock([('column1', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.RichTextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))])), ('column2', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.RichTextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))])), ('column3', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.RichTextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))])), ('column4', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.RichTextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))])), ('column5', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.RichTextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))])), ('column6', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.RichTextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]))])), ('carousel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('0%', '0%'), ('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')])), ('images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False)), ('description', wagtail.core.blocks.TextBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(help_text='Enter Link to web page', required=False))]), icon='image', template='include/bcarousel.html'))])), ('media', inside.blocks.MediaBlock())], blank=True, null=True)),
                ('feed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='inside.Feed')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
