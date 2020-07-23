COLOR_CHOICES = (
    ('black', 'black'),
    ('#1b143b', 'navy1'),
    ('#211849', 'navy2'),
    ('white', 'white'),
    ('#e6e6e6', 'light gray'),
    ('red', 'red'),
    ('blue', 'blue'),
    ('green', 'green'),
)


ALIGN_CHOICES = (
    ('left', "Left"),
    ('right', "Right"),
    ('center', "Center"),
    ('justify', "Justify")
)

SIZE_CHOICES = (
    ('auto', "Auto"),
    ('cover', "Cover"),
    ('30%', '30%'),
    ('50%', "50%"),
    ('100%', "100%"),
    ('200%', "200%"),
)

PERCENT_CHOICES = (
    ('0%', '0%'),
    ('10%', "10%"),
    ('20%', "20%"),
    ('30%', "30%"),
    ('40%', "40%"),
    ('50%', "50%"),
    ('60%', "60%"),
    ('70%', "70%"),
    ('80%', "80%"),
    ('90%', "90%"),
    ('100%', "100%"),
)

WIDTH_CHOICES = (
    ('auto', 'auto'),
)

HEIGHT_CHOICES = (
    ('auto', 'auto'),
    ('50vh', '50vh'),
    ('70vh', '70vh'),
)

BACKGROUND_ATTACHMENT_CHOICES = (
    ('scroll', 'scroll'),
    ('fixed', 'fixed'),
    ('local', 'local'),
    ('initial', 'initial'),
    ('inherit', 'inherit'),
)

# Used for background-clip and background-origin
# background-clip lets you control hoe far a background image or color extends beyond an element's padding or content.
# background-origin defines where to paint the background: across the whole element, inside the border, or inside the padding.
BACKGROUND_ORIGIN_CLIP_CHOICES = (
    ('border-box', 'border-box'),
    ('padding-box', 'padding-box'),
    ('content-box', 'content-box'),
    ('inherit', 'inherit'),
)

BACKGROUND_REPEAT_CHOICES = (
    ('repeat', 'repeat'),
    ('repeat-x', 'repeat-x'),
    ('repeat-y', 'repeat-y'),
    ('no-repeat', 'no-repeat'),
)
