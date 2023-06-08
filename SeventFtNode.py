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
