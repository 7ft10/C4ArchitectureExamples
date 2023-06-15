#@title Repository
import os
import yaml
from diagrams.c4 import Person, Container, Database, System
from diagrams.custom import Custom
from urllib import request, parse
from IPython.display import display, Markdown

#@markdown # Seven Ft Repository
class SevenftRepository():
  def Print(self):
    for member in dir(self):
      typ = getattr(self, member)
      if isinstance(typ, SevenftNode):
        typ.Print()

#@markdown # Seven Ft Node
class SevenftNode():
  def __init__(self, nodeType: str):
    self.nodeType = nodeType
    self.default_icon = SevenftNode.GetIcon('_default_icon.png', 'https://cdn-icons-png.flaticon.com/512/10448/10448063.png')

  @staticmethod
  def metadata(args = {}):
    def _metadata(func):
      func.metadata = args or {}
      func.metadata.setdefault('name', "Name missing")
      func.metadata.setdefault('description', "")
      return func
    return _metadata

  @staticmethod
  def GetIcon(name: str, url: str):
    try:
      request.urlretrieve(url, name)
      return name
    except:
      return '_default_icon.png'

  @staticmethod
  def FormatLabel(name: str, key: str, description: str):
    title = f'<font point-size="12"><b>{name}</b></font><br/>'
    subtitle = f'<font point-size="9">[{key}]<br/></font>' if key else ""
    text = f'<br/><font point-size="10">{description}</font>' if description else ""
    return f"<{title}{subtitle}{text}>"

  @staticmethod
  def LoadFromYaml(url: str):
    path = "_" + os.path.basename(parse.urlparse(url).path) ## Temp file
    request.urlretrieve(url, path)
    with open(path, "r") as stream:
      archetype = yaml.safe_load(stream)
    id = str(archetype.get('id'))
    nodeType = str(archetype.get("nodeType"))
    globals()[id] = type(id, (SevenftNode, ), {
      "__init__": lambda self : SevenftNode.__init__(self, nodeType),
      "metadata": archetype
    })
    return globals()[id]()

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
    md: dict = self.metadata.copy()
    if md.get("icon") != None:
      md["icon_path"] = SevenftNode.GetIcon("_" + md.get('id') + ".png", md.get("icon"))
    match self.nodeType:
      case "Container":
        md.setdefault('technology', "Technology missing")
        return Container( md.pop('name'), md.pop('technology'), md.pop('description'), **md )
      case "Person":
        md.setdefault('external', False)
        return Person( md.pop('name'), md.pop('description'), md.pop('external'), **md )
      case "Custom":
        md.setdefault('icon_path', self.default_icon)
        name = md.pop('name')
        if "label" in md:
          name = md.pop('label')
        return Custom(name, md.pop('icon_path'), **md)
      case "Database":
        md.setdefault('technology', "Technology missing")
        return Database( md.pop('name'), md.pop('technology'), md.pop('description'), **md )
      case "System":
        md.setdefault('external', False)
        return System( md.pop('name'), md.pop('description'), md.pop('external'), **md )
      case _:
        md.setdefault('external', False)
        return System( md.pop('name'), md.pop('description'), md.pop('external'), **md )
