from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets.common import SearchBoxViewlet as _SearchBoxViewlet
from plone.app.layout.viewlets.content import DocumentActionsViewlet as _DocumentActionsViewlet
from plone.app.layout.viewlets.common import GlobalSectionsViewlet as _GlobalSectionsViewlet
from plone.app.layout.viewlets.common import PersonalBarViewlet as _PersonalBarViewlet

# Webrichtlijnen
# Override templates, template are altered to conform to webrichtlijnen.
# There's no change in the visual appearance of the viewlets.

class SearchBoxViewlet(_SearchBoxViewlet):
    index = ViewPageTemplateFile('searchbox.pt')

class DocumentActionsViewlet(_DocumentActionsViewlet):
    index = ViewPageTemplateFile("document_actions.pt")

class GlobalSectionsViewlet(_GlobalSectionsViewlet):
    index = ViewPageTemplateFile('sections.pt')

class PersonalBarViewlet(_PersonalBarViewlet):
    index = ViewPageTemplateFile('personal_bar.pt')
