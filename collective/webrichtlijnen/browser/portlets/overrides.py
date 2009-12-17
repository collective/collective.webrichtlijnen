from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.portlets.portlets.calendar import Renderer as CalendarRenderer
from plone.app.portlets.portlets.events import Renderer as EventsRenderer
from plone.app.portlets.portlets.news import Renderer as NewsRenderer
from plone.app.portlets.portlets.recent import Renderer as RecentRenderer
from plone.app.portlets.portlets.review import Renderer as ReviewRenderer
from plone.app.portlets.portlets.rss import Renderer as RSSRenderer
from plone.app.portlets.portlets.search import Renderer as SearchRenderer

# Webrichtlijnen changes:
# Portlets below had a xmlns attribute on the dl element. This is not
# valid W3C strict HTML. Why was this attribute placed on the dl element? These
# namespace definitions are done on top level of the html.
#
# This change isn't perfect but tit is the best way to get rid of the xmlns attribute.

class Calendar(CalendarRenderer):
    _template = ViewPageTemplateFile('calendar.pt')

class Events(EventsRenderer):
    _template = ViewPageTemplateFile('events.pt')

class News(NewsRenderer):
    _template = ViewPageTemplateFile('news.pt')

class Recent(RecentRenderer):
    _template = ViewPageTemplateFile('recent.pt')

class Review(ReviewRenderer):
    _template = ViewPageTemplateFile('review.pt')

class RSS(RSSRenderer):
    _template = ViewPageTemplateFile('rss.pt')

class Search(SearchRenderer):
    _template = ViewPageTemplateFile('search.pt')

