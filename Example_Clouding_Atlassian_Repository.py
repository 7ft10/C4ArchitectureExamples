#@title Repository
from diagrams.c4 import Person, Container, Database, System
from diagrams.custom import Custom
from urllib import request
from IPython.display import display, Markdown

display(Markdown('# Imports'))

display(Markdown('+ https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/SeventFtNode.py'))
request.urlretrieve('https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/SeventFtNode.py', 'SeventFtNode.tmp')

from SeventFtNode import *

#@title Repository

#@markdown ----------------------------------------------
#@markdown # Our Systems

#@markdown + Disc (Disc)
@SevenftNode.metadata({
    "name": "Disc",
    "technology": "IBMi",
    "description": "http://ddafsd/dsf",
    "icon_path": SevenftNode.GetIcon("NewRelic.png", "https://icons/NewRelic.png"),
    "one": "two"
})
class Disc(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Custom")

#@markdown + Bamboo (Server) (Bamboo)
@SevenftNode.metadata({
    "name" : "Bamboo (Server)",
    "technology" : "Linux",
    "description" : "Bamboo.",
    "label": SevenftNode.FormatLabel("Bamboo (Server)", "Container", "Linux <br/> bamboo.budgetdirect.com.au <br/> 192.168.61.150"),
    "_attributes": {
        "CPU": "",
        "RAM": "",
        "Storage": "124.5GB",
        "Type": "V",
        "OS": "Linux",
        "Network Zone": "",
        "Confluence Application Version": "8.13.2"
    }
})
class Bamboo(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Container")

#@markdown + Confluence (Server) (Confluence)
@SevenftNode.metadata({
    "name" : "Confluence (Server)",
    "technology" : "Linux",
    "description" : "Confluence",
    "label": SevenftNode.FormatLabel("Confluence (Server)", "Container", "Linux <br/> confluence.budgetdirect.com.au <br/> 192.168.110.100"),
    "_attributes": {
        "CPU": "",
        "RAM": "",
        "Storage": "124.5GB",
        "Type": "V",
        "OS": "Linux",
        "Network Zone": "",
        "Confluence Application Version": "8.13.2"
    }
})
class Confluence(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Container")

#@markdown + Jira (Server) (Jira)
@SevenftNode.metadata({
    "name" : "Jira (Server)",
    "technology" : "Linux",
    "description" : "jira.budgetdirect.com.au",
    "label": SevenftNode.FormatLabel("Jira (Server)", "Container", "Linux <br/> jira.budgetdirect.com.au <br/> 192.168.110.46"),
    "_attributes": {
        "CPU": "",
        "RAM": "",
        "Storage": "124.5GB",
        "Type": "V",
        "OS": "Linux",
        "Network Zone": "",
        "Confluence Application Version": "8.13.2"
    }
})
class Jira(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Container")

#@markdown + Active Directory (ActiveDirectory)
@SevenftNode.metadata({
    "label" : "Active Directory",
    "icon_path" : SevenftNode.GetIcon("ActiveDirectory.png", "https://www.outsystems.com/Forge_CW/_image.aspx/Q8LvY--6WakOw9afDCuuGXsjTvpZCo5fbFxdpi8oIBI=/active-directory-core-simplified-2023-01-04%2000-00-00-2023-05-05%2011-44-13")
})
class ActiveDirectory(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Custom")

#@markdown + The Hub (TheHub)
@SevenftNode.metadata({
    "name" : "The Hub",
    "description" : "The hub.",
    "_attributes": {
        "Notes": """
                Part of the on-prem confluence implementation,
                to be migrated not a new system.
                """,
    }
})
class TheHub(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "System")

#@markdown + Confluence (Server) (Confluence)
@SevenftNode.metadata({
    "name" : "Confluence (Server) (Non-Prod)",
    "technology" : "Linux",
    "description" : "df-conflu-app.budgetdirect.com.au",
    "label": SevenftNode.FormatLabel("Confluence (Server) (Non-Prod)", "Container", "Linux <br/> df-conflu-app.budgetdirect.com.au <br/> 192.168.61.164"),
    "_attributes": {
        "CPU": "",
        "RAM": "",
        "Storage": "124.5GB",
        "Type": "V",
        "OS": "Linux",
        "Network Zone": "",
        "Confluence Application Version": "8.13.2"
    }
})
class ConfluenceNonProd(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Container")

#@markdown + Jira (Server) (Jira)
@SevenftNode.metadata({
    "name" : "Jira (Server) (Non-Prod)",
    "technology" : "Linux",
    "description" : "jiradev.budgetdirect.com.au",
    "label": SevenftNode.FormatLabel("Jira (Server) (Non-Prod)", "Container", "Linux <br/> jiradev.budgetdirect.com.au <br/> 192.168.64.22"),
    "_attributes": {
        "CPU": "",
        "RAM": "",
        "Storage": "124.5GB",
        "Type": "V",
        "OS": "Linux",
        "Network Zone": "",
        "Confluence Application Version": "8.13.2"
    }
})
class JiraNonProd(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Container")

#@markdown + BitBucket (BitBucket)
@SevenftNode.metadata({
    "label" : "BitBucket",
    "icon_path" : SevenftNode.GetIcon("BitBucket.png", "https://bitbucket.icon")
})
class BitBucket(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Container")

#@markdown + Jenkins (Jenkins)
@SevenftNode.metadata({
    "label" : "Jenkins",
    "icon_path" : SevenftNode.GetIcon("Jenkins.png", "https://jenkins.icon")
})
class Jenkins(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Custom")

#@markdown + Power BI (PowerBI)
@SevenftNode.metadata({
    "label" : "Power BI",
    "icon_path" : SevenftNode.GetIcon("PowerBI.png", "https://www.clipartmax.com/png/middle/16-161548_power-bi-logo-microsoft-vector-eps-free-download-icons-power-bi-logo.png")
})
class PowerBI(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Custom")

#@markdown + Service Now (ServiceNow)
@SevenftNode.metadata({
    "label" : "Service Now",
    "icon_path" : SevenftNode.GetIcon("ServiceNow.png", "https://servicenow.icon")
})
class ServiceNow(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Custom")


#@markdown + GitLab (GitLab)
@SevenftNode.metadata({
    "label" : "GitLab",
    "icon_path" : SevenftNode.GetIcon("Gitlab.png", "https://about.gitlab.com/images/press/logo/png/gitlab-logo-100.png")
})
class GitLab(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Custom")

#@markdown + Okta (Okta)
@SevenftNode.metadata({
    "label" : "Okta",
    "icon_path" : SevenftNode.GetIcon("Okta.png", "https://okta.icon")
})
class Okta(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Custom")

#@markdown + Citrix (Citrix)
@SevenftNode.metadata({
    "label" : "Citrix",
    "icon_path" : SevenftNode.GetIcon("Citrix.png", "https://citrix.icon")
})
class Citrix(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Custom")

#@markdown + Global Protect (GlobalProtect)
@SevenftNode.metadata({
    "label" : "Global Protect",
    "icon_path" : SevenftNode.GetIcon("GlobalProtect.png", "https://globalprotect.icon")
})
class GlobalProtect(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Custom")


#@markdown + Confluence (Atlassian) (Confluence)
@SevenftNode.metadata({
    "name" : "Confluence (Atlassian)",
    "technology" : "Cloud",
    "description" : "Confluence",
    "label": SevenftNode.FormatLabel("Confluence (Server)", "SAAS", "Atlassian"),
    "_attributes": {
        "one": "two"
    }
})
class ConfluenceCloud(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "System")

#@markdown + Jira (Atlassian) (Jira)
@SevenftNode.metadata({
    "name" : "Jira (Atlassian)",
    "technology" : "Linux",
    "description" : "Jira",
    "label": SevenftNode.FormatLabel("Jira (Server)", "SAAS", "Atlassian"),
})
class JiraCloud(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "System")

#@markdown + NewRelic (NewRelic)
@SevenftNode.metadata({
    "label" : "NewRelic",
    "icon_path" : SevenftNode.GetIcon("NewRelic.png", "https://icons/NewRelic.png")
})
class NewRelic(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Custom")

#@markdown ----------------------------------------------
#@markdown ## Personas

#@markdown + A&G Internal Users (AGInternalUsers)
@SevenftNode.metadata({
    "name" : "A&G Internal Users",
    "description" : "A&G Internal Users."
})
class AGInternalUsers(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Person")

#@markdown + A&G Remote Users (AGRemoteUsers)
@SevenftNode.metadata({
    "name" : "A&G Remote Users",
    "description" : "A&G Remote Users."
})
class AGRemoteUsers(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Person")

#@markdown + A&G External Users (AGExternalUsers)
@SevenftNode.metadata({
    "name" : "A&G External Users",
    "description" : "A&G External Users."
})
class AGExternalUsers(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Person")