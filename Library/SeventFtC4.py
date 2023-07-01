"""
A set of nodes and edges to visualize software architecture using the C4 model.
"""
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
