# -*- coding: utf-8 -*-
from rest_framework.routers import SimpleRouter


class OptionalTrailingSlashSimpleRouter(SimpleRouter):
    """
    Router that does not care if there is a leading slash or not.

    The URLs in the hyperlinked fields will use the value given during the
    init but the actual API will work with both.

    Does not appear to have any downsides and it pretty nice to work with.

    Based on a discussion in
    https://github.com/tomchristie/django-rest-framework/issues/905
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trailing_slash = "/?"
