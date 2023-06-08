#@title Repository
from diagrams.c4 import Person, Container, Database, System
from diagrams.custom import Custom
from urllib.request import urlretrieve
from IPython.display import display, Markdown

class SevenftNode():
  def __init__(self, nodeType):
    self.nodeType = nodeType
    self.instance = None

  @staticmethod
  def metadata(args = {}):
    def _metadata(func):
      func.metadata = args or {}
      func.metadata.setdefault('name', "Name missing")
      func.metadata.setdefault('description', "")
      return func
    return _metadata

  @staticmethod
  def GetIcon(name, url):
    try:
        urlretrieve(url, name)
    except:
        try:
          urlretrieve("https://cdn-icons-png.flaticon.com/512/10448/10448063.png", name)
        except:
          pass
    return name

  @staticmethod
  def FormatLabel(name, key, description):
    title = f'<font point-size="12"><b>{name}</b></font><br/>'
    subtitle = f'<font point-size="9">[{key}]<br/></font>' if key else ""
    text = f'<br/><font point-size="10">{description}</font>' if description else ""
    return f"<{title}{subtitle}{text}>"

  def Print(self):
    if (self.metadata != None) and (isinstance(self.metadata, type({}))):
      display(Markdown('---'))
      display(Markdown('## ' + self.__class__.__name__))

      if len(self.metadata.items()) > 0:
        table = """| Key         | Value       |
                   | ----------- | ----------- |"""
        for k, v in self.metadata.items():
          table = table + "\n| " + k + " | " + (v if isinstance(v, str) else str(v)) + " |"
        display(Markdown(table))

  def Get(self):
    md = self.metadata.copy()
    if (self.instance == None):
      match self.nodeType:
        case "Container":
          md.setdefault('technology', "Technology missing")
          self.instance = Container( md.pop('name'), md.pop('technology'), md.pop('description'), **md )
        case "Person":
          md.setdefault('external', False)
          self.instance = Person( md.pop('name'), md.pop('description'), md.pop('external'), **md )
        case "Custom":
          md.setdefault('icon_path', "Icon path missing")
          name = md.pop('name')
          if "label" in md:
            name = md.pop('label')
            if "name" in md:
              md.pop('name')
            else:
              pass
          else:
            pass
          self.instance = Custom(name, md.pop('icon_path'), **md)
        case "Database":
          md.setdefault('technology', "Technology missing")
          self.instance = Database( md.pop('name'), md.pop('technology'), md.pop('description'), **md )
        #case "System":
        case _:
          md.setdefault('external', False)
          self.instance = System( md.pop('name'), md.pop('description'), md.pop('external'), **md )
    return self.instance

#@markdown ----------------------------------------------
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

#@markdown ---
#@markdown # Our Data Stores
class OurDataStores():

  #@markdown + Oracle Database (OracleDB)
  def OracleDB():
    return {
      "name" : "Oracle DB",
      "technology" : "Oracle Database",
      "description" : "Stores user registration information, hashed authentication credentials, access logs, etc.",
    }

#@markdown ----------------------------------------------
#@markdown # Our External Systems
class OurExternalSystems():

  #@markdown + E-mail System (Email)
  def Email():
    return {
      "name" : "E-mail System",
      "description" : "The internal Microsoft Exchange e-mail system.",
      "external" : True
    }

  #@markdown + Mainframe Banking System (Mainframe)
  def Mainframe():
    return {
      "name" : "Mainframe Banking System",
      "description" : "Stores all of the core banking information about customers, accounts, transactions, etc.",
      "external" : True
    }

#@markdown ----------------------------------------------
#@markdown # Our Personas
class OurPersonas():

  #@markdown + Banking Customer (BankingCustomer)
  def BankingCustomer():
    return {
      "name" : "Personal Banking Customer",
      "description" : "A customer of the bank, with personal bank accounts."
    }
