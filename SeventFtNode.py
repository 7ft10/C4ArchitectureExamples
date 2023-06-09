#@title Repository
import os
import yaml
from diagrams.c4 import Person, Container, Database, System
from diagrams.custom import Custom
from urllib import request, parse
from IPython.display import display, Markdown

class SevenftNode():
  def __init__(self, nodeType: str):
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
  def GetIcon(name: str, url: str):
    try:
        request.urlretrieve(url, name)
    except:
        try:
          request.urlretrieve("https://cdn-icons-png.flaticon.com/512/10448/10448063.png", name)
        except:
          pass
    return name

  @staticmethod
  def FormatLabel(name: str, key: str, description: str):
    title = f'<font point-size="12"><b>{name}</b></font><br/>'
    subtitle = f'<font point-size="9">[{key}]<br/></font>' if key else ""
    text = f'<br/><font point-size="10">{description}</font>' if description else ""
    return f"<{title}{subtitle}{text}>"

  @staticmethod
  def LoadFromYaml(url: str):
    archetype = None
    a = parse.urlparse(url)
    path = os.path.basename(a.path)
    request.urlretrieve(url, "_" + path)

    with open(path, "r") as stream:
        try:
            archetype = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            display(exc)

    # constructor
    def constructor(self):
        SevenftNode.__init__(self, self.node_type)

    id = str(archetype.pop('id'))
    globals()[id] = type(id, (SevenftNode, ), {
        "__init__": constructor,
        "node_type": archetype.pop("nodeType"),
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
          table = table + """
                            """
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
