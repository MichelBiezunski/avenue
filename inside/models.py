from django.db import models

# from wagtail.core.models import Page
from wagtailmenus.models import MenuPage
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail_blocks.blocks import HeaderBlock, ListBlock, ImageTextOverlayBlock, CroppedImagesWithTextBlock, \
    ListWithImagesBlock, ThumbnailGalleryBlock, ChartBlock, MapBlock, ImageSliderBlock

from inside.blocks import OneColumnBlock, TwoColumnBlock, ThreeColumnBlock, SixColumnBlock, CarouselBlock, MediaBlock
from inside.snippets import Feed

class InsidePage(MenuPage):

    def get_context(self, request, *args, **kwargs):

        context = super(InsidePage, self).get_context(request, *args, **kwargs)
        context['inside_page'] = self

        context['menuitems'] = self.get_children().filter(
            live=True, show_in_menus=True
        )
        return context

    feed = models.ForeignKey(
         Feed,
         null=True,
         blank=True,
         on_delete=models.SET_NULL,
         related_name='+',
     )

    body = StreamField([
        ('one_column', OneColumnBlock()),
        ('two_columns', TwoColumnBlock()),
        ('three_columns', ThreeColumnBlock()),
        ('six_columns', SixColumnBlock()),
        ('carousel', CarouselBlock()),
        ('media', MediaBlock()),
        ('map', MapBlock()),

    ], blank=True, null=True)

    content_panels = MenuPage.content_panels + [
        StreamFieldPanel('body'),
        # SnippetChooserPanel('feed'),
    ]

