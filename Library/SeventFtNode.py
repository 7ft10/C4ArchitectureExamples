#@title Repository
import os
import yaml
##from diagrams import Node
##from diagrams.c4 import Container, Database, System, C4Node
#from diagrams.custom import Custom
from urllib import request, parse
from IPython.display import display, Markdown
import html
import textwrap
from diagrams import Node, Cluster, Edge

class C4FormatterMixIn:
    def _format_node_label(self, name, key, description):
        """Create a graphviz label string for a C4 node"""
        title = f'<font point-size="12"><b>{html.escape(name)}</b></font><br/>'
        subtitle = f'<font point-size="9">[{html.escape(key)}]<br/></font>' if key else ""
        text = f'<br/><font point-size="10">{self._format_description(description)}</font>' if description else ""
        return f"<{title}{subtitle}{text}>"

    def _format_description(self, description):
        """
        Formats the description string so it fits into the C4 nodes.

        It line-breaks the description so it fits onto exactly three lines. If there are more
        than three lines, all further lines are discarded and "..." inserted on the last line to
        indicate that it was shortened. This will also html-escape the description so it can
        safely be included in a HTML label.
        """
        wrapper = textwrap.TextWrapper(width = 40, max_lines = 3)
        lines = [html.escape(line) for line in wrapper.wrap(description)]
        lines += [""] * (3 - len(lines))  # fill up with empty lines so it is always three
        return "<br/>".join(lines)

    def _format_edge_label(description):
        """Create a graphviz label string for a C4 edge"""
        wrapper = textwrap.TextWrapper(width = 24, max_lines = 3)
        lines = [html.escape(line) for line in wrapper.wrap(description)]
        text = "<br/>".join(lines)
        return f'<<font point-size="10">{text}</font>>'

class C4Node(C4FormatterMixIn, Node):
    def __init__(self, name, summary = "", description = "", type = "Container", **kwargs):
        key = f"{type}: {summary}" if summary else type
        label = self._format_node_label(name, key, description)
        attributes = {
            "icon_path": kwargs.get('icon_path') if kwargs.get('icon_path') else None,
            "labelloc": "c",
            "shape": "rect",
            "width": "2.6",
            "height": "1.6",
            "fixedsize": "true",
            "style": "filled",
            "fillcolor": "dodgerblue3",
            "fontcolor": "white",
        }
        # collapse boxes to a smaller form if they don't have a description
        if not description:
            attributes.update({"width": "2", "height": "1"})
        attributes.update(kwargs)
        super().__init__(label, **attributes)

    def _load_icon(self):
        if self.icon_path == None:
            return super()._load_icon()
        else:
            return self.icon_path

class Container(C4Node):
    def __init__(self, name, summary = "", description = "", **kwargs):
        attributes = { }
        attributes.update(kwargs)
        super().__init__(name, summary, description, "Container", **attributes)

class Component(C4Node):
    def __init__(self, name, summary = "", description = "", **kwargs):
        attributes = { }
        attributes.update(kwargs)
        super().__init__(name, summary, description, "Component", **attributes)

class Database(C4Node):
    def __init__(self, name, summary = "", description = "", **kwargs):
        attributes = {
            "shape": "cylinder",
            "labelloc": "b",
        }
        attributes.update(kwargs)
        super().__init__(name, summary, description, "Database", **attributes)

class System(C4Node):
    def __init__(self, name, summary = "", description = "", **kwargs):
        external = kwargs.get('external') if kwargs.get('external') else False
        attributes = {
            "type": "External System" if external else "System",
            "fillcolor": "gray60" if external else "dodgerblue4",
        }
        attributes.update(kwargs)
        super().__init__(name, summary, description, "Database", **attributes)

class Persona(C4Node):
    def __init__(self, name, summary = "", description = "", **kwargs):
        external = kwargs.get('external') if kwargs.get('external') else False
        attributes = {
            "type": "External Person" if external else "Person",
            "fillcolor": "gray60" if external else "dodgerblue4",
            "style": "rounded,filled",
        }
        attributes.update(kwargs)
        super().__init__(name, summary, description, "Database", **attributes)

class Code(C4Node):
    def __init__(self, name, summary = "", description = "", **kwargs):
        shape = "note"
        external = kwargs.get('external') if kwargs.get('external') else False
        type = "module"
        if type == "abstract": shape = "tab" ## module
        if type == "interface": shape = "circle"
        attributes = {
            "fixedsize": "true" if shape == "circle" else "false",
            "fillcolor": "gray60" if external else "dodgerblue4",
            "shape": shape,
            "fontcolor": "black" if shape == "circle" else "white",
            "width": "0.6" if shape == "circle" else "2.6",
            "height": "0.6" if shape == "circle" else "1.6",
        }
        attributes.update(kwargs)
        super().__init__(name, summary, description, type, **attributes)

class SystemBoundary(C4FormatterMixIn, Cluster):
    def __init__(self, label, **kwargs):
        attributes = {
            "label": html.escape(label),
            "bgcolor": "white",
            "margin": "16",
            "style": "dashed",
        }
        attributes.update(kwargs)
        super().__init__(label = label, graph_attr = attributes)

class Relationship(C4FormatterMixIn, Edge):
    def __init__(self, label = "", **kwargs):
        attributes = {
            "style": "dashed",
            "color": "gray60",
            "label": self._format_edge_label(label) if label else "",
        }
        attributes.update(kwargs)
        super().__init__(label = label, **attributes)

baseUrl = "https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/"

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
    self.default_icon = SevenftNode.GetIcon('_default_icon.png', baseUrl + 'Library/Icons/Missing.png')
    self.default_persona_icon = SevenftNode.GetIcon('_persona.png', baseUrl + 'Library/Icons/Persona.png')

  @staticmethod
  def metadata(args = {}):
    def _metadata(func):
      func.metadata = args or {}
      func.metadata.setdefault('name', 'Name missing')
      func.metadata.setdefault('description', '')
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
    md.setdefault('external', False)
    md.setdefault('summary', '')

    if md.get("icon") != None:
      md["icon_path"] = SevenftNode.GetIcon("_" + md.get('id') + ".png", md.get("icon"))

    match self.nodeType:
      case "Container":
        return Container( md.pop('name'), md.pop('summary'), md.pop('description'), **md )
      case "Persona":
        md.setdefault('icon_path', self.default_persona_icon)
        return Persona( md.pop('name'), md.pop('summary'), md.pop('description'), **md )
      case "Database":
        return Database( md.pop('name'), md.pop('summary'), md.pop('description'), **md )
      case "System":
        return System( md.pop('name'), md.pop('summary'), md.pop('description'), **md )
      case "Component":
        return Component( md.pop('name'), md.pop('summary'), md.pop('description'), **md )
      case "Code":
        return Code( md.pop('name'), md.pop('summary'), md.pop('description'), **md )
      case _:
        return System( md.pop('name'), md.pop('summary'), md.pop('description'), **md )
