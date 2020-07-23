from wagtail.images.formats import Format, register_image_format, unregister_image_format
register_image_format(Format('thumbnail', 'Thumbnail', 'richtext-image thumbnail img-responsive', 'width-120'))
