# -*- coding: utf-8 -*-

from __future__ import absolute_import

# External Libraries
from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView


from .views import (
    About,
    Classes,
    Contact,
    Dance,
    Index,
    Music,
    Volunteers,
    Survey,
)

urlpatterns = [
    url(r"^about.html", About.as_view()),
    url(r"^classes.html", Classes.as_view()),
    url(r"^dance.html", Dance.as_view()),
    url(r"^music.html", Music.as_view()),
    url(r"^volunteers.html", Volunteers.as_view()),
    url(r"^survey.html", Survey.as_view()),
    url(r"^contact/?", Contact.as_view()),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    url(r"^$", Index.as_view()),
]
