from django.forms.utils import flatatt
from django.utils.html import format_html, format_html_join
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailmedia.blocks import AbstractMediaChooserBlock

from .choices import PERCENT_CHOICES, ALIGN_CHOICES, COLOR_CHOICES


class ImageCarouselBlock(blocks.StructBlock):

    image = ImageChooserBlock()
    caption = blocks.TextBlock(required=False)
    description = blocks.TextBlock(required=False)
    link = blocks.URLBlock(required=False, help_text="Enter Link to web page")
    class Meta:
        icon = 'image'


class CarouselBlock(blocks.StructBlock):

    label = blocks.CharBlock(
        required=False
    )
    size = blocks.ChoiceBlock(
        choices=PERCENT_CHOICES,
        default="100%",
    )
    images = blocks.ListBlock(
        ImageCarouselBlock(),
        template='include/bcarousel.html',
        icon="image"
    )

    class Meta:
        template = 'blocks/carousel_block.html'
        icon = 'placeholder'
        label = 'Carousel'


class ColumnBlock(blocks.StructBlock):

    def __init__(self, *args, **kwargs):
        self.icon = kwargs['icon']
        self.label = kwargs['label']
        self.get(*args, **kwargs)
        super(ColumnBlock, self).__init__(*args, **kwargs)

    def get(self, *args, **kwargs):
        column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('link', blocks.PageChooserBlock()),
            ('html', blocks.RawHTMLBlock()),
            ('table', TableBlock(required=False)),
            ('carousel', CarouselBlock(required=False)),
            ('image', ImageChooserBlock()),
        ], icon=self.icon, label=self.label)
        return column


class MediaBlock(AbstractMediaChooserBlock):
    def render_basic(self, value, context=None):
        if not value:
            return ''

        if value.type == 'media':
            player_code = '''
            <div>
            <video width="100%" controls>
            {0}
            Your browser does not support the video tag.
            </video>
            </div>
            '''
        else:
            player_code = '''
            <div>
            <audio controls>
            {0}
            Your browser does not support the audio element
            </audio>
            </div>
            '''

        return format_html(player_code, format_html_join(
            '\n', "<source{0}>",
            [[flatatt(s)] for s in value.sources]
        ))


class OneColumnBlock(blocks.StructBlock):

    # one_column = ColumnBlock(icon='arrow-left', label='One Column')
    one_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('link', blocks.PageChooserBlock()),
        ('html', blocks.RawHTMLBlock()),
        ('table', TableBlock(required=False)),
        ('carousel', CarouselBlock(required=False)),
        ('image', ImageChooserBlock()),
        ('media', MediaBlock(required=False)),
    ], icon='arrow-left', label='One column', required=False)

    class Meta:
        template = 'blocks/one_column_block.html'
        icon = 'placeholder'
        label = 'One Column'


class TwoColumnBlock(blocks.StructBlock):

    left_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
        ('html', blocks.RawHTMLBlock()),
        ('media', MediaBlock(required=False)),
    ], icon='arrow-left', label='Left column content', required=False)

    right_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
        ('media', MediaBlock(required='False'))
    ], icon='arrow-right', label='Right column content', required=False)

    class Meta:
        template = 'blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'


class ThreeColumnBlock(blocks.StructBlock):

    background = blocks.ChoiceBlock(choices=COLOR_CHOICES, default="black")

    left_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
        ('html', blocks.RawHTMLBlock()),
        ('media', MediaBlock(required=False)),
    ], icon='arrow-left', label='Left column content')

    middle_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
        ('html', blocks.RawHTMLBlock()),
        ('media', MediaBlock(required=False)),
    ], icon='arrow-down', label='Middle column content')

    right_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
        ('html', blocks.RawHTMLBlock()),
        ('media', MediaBlock()),
    ], icon='arrow-right', label='Right column content', required=False)

    class Meta:
        template = 'blocks/three_column_block.html'
        icon = 'placeholder'
        label = 'Three Columns'


class ImageBlock(blocks.StructBlock):

    image = ImageChooserBlock(required=False)
    caption = blocks.RichTextBlock(required=False)
    link = blocks.URLBlock(required=False)


class SixColumnBlock(blocks.StructBlock):

    column1 = ImageBlock()
    column2 = ImageBlock()
    column3 = ImageBlock()
    column4 = ImageBlock()
    column5 = ImageBlock()
    column6 = ImageBlock()

    class Meta:
        template = 'blocks/six_column_block.html'
        icon = 'placeholder'
        label = 'Six Columns'

