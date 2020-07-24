from django import template
from django.conf import settings

# from wagtail.core.models import Page
from inside.snippets import Footer, Feed

register = template.Library()


# settings value
@register.simple_tag
def get_google_maps_key():
    return getattr(settings, 'GOOGLE_MAPS_KEY', "")


@register.simple_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('resistance/tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):

    menuitems = parent.get_children().live().in_menu()
    # median is the number that will be used to separate
    # the left menu from the right menu.
    median = int(len(menuitems) / 2)
    left_menuitems = []
    right_menuitems = []

    for idx, menuitem in enumerate(menuitems):
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)
        if idx < median:
            menuitem.position = 'left'
            left_menuitems.append(menuitem)
        else:
            menuitem.position = 'right'
            right_menuitems.append(menuitem)

    # Separation between left and right menu items.
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        'left_menuitems': left_menuitems,
        'right_menuitems': right_menuitems,
        'median': median,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag(
    'resistance/tags/top_menu_children.html',
    takes_context=True
)
def top_menu_children(context, parent):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves all live pages which are children of the calling page
# for standard index listing
@register.inclusion_tag(
    'resistance/tags/standard_index_listing.html',
    takes_context=True
)
def standard_index_listing(context, calling_page):
    pages = calling_page.get_children().live()
    return {
        'pages': pages,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag('resistance/tags/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=2)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }


# Footer snippets
@register.inclusion_tag('resistance/tags/footer.html', takes_context=True)
def footer(context):
    return {
        'footer': Footer.objects.all(),
        'request': context['request'],
    }


# Feed Video
@register.inclusion_tag('resistance/tags/feed.html', takes_context=True)
def feed(context):
    return {
        'feed': Feed.objects.all(),
        'request': context['request'],
    }
