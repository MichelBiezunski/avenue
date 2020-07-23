import os
from django.conf import settings
from django.db import models
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock

# ------------------------------------------- #
#  SNIPPETS
# ------------------------------------------- #


@register_snippet
class Feed(models.Model):

    # webm = models.CharField(null=True, blank=True, max_length=128)
    mp4 = models.CharField(null=True, blank=True, max_length=128)
    fallback = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+',
        blank=True,
        null=True,
    )
    header = models.CharField(max_length=255, null=True, blank=True)
    subheader = models.TextField(null=True, blank=True)
    button_text = models.CharField(max_length=50, default='Find Out More')

    panels = [
        # FieldPanel('webm'),
        FieldPanel('mp4'),
        ImageChooserPanel('fallback'),
        FieldPanel('header'),
        FieldPanel('subheader'),
        FieldPanel('button_text'),
    ]

    def save(self, *args, **kwargs):
        # self.webm = os.path.join(settings.STATIC_URL, self.webm)
        self.mp4 = os.path.join(settings.STATIC_URL, self.mp4)
        super(Feed, self).save(*args, **kwargs)

    def __str__(self):
        return self.header


@register_snippet
class Footer(models.Model):
    label = models.CharField(max_length=50, null=True, blank=True)
    content = StreamField(
        [
            ('paragraph', blocks.RichTextBlock()),
            ('html', blocks.RawHTMLBlock()),
            ('table', TableBlock()),
            ('image', ImageChooserBlock(template='blocks/image_block.html')),
        ],
        null=True,
        blank=True
    )
    panels = [
        FieldPanel('label'),
        StreamFieldPanel('content'),
    ]

    def __str__(self):
        if self.label:
            return self.label
        else:
            return ''
