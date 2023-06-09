#@title Repository
from urllib import request
from Repository.SeventFtNode import SevenftNode

#@markdown # Imports'

#@markdown + https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/SeventFtNode.py'))
request.urlretrieve('https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/SeventFtNode.py', '_SeventFtNode_.py')

from _SeventFtNode_ import *

#@markdown ----------------------------------------------
#@markdown # Personas

#@markdown + BankingCustomer
@SevenftNode.metadata({
    "name": "Banking Customer",
    "description": "Banking Customer"
})
class BankingCustomer(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Person")

#@markdown ----------------------------------------------
#@markdown ## Internal Systems
@SevenftNode.metadata({
    "name": "Web App",
    "description": "C# Web application"
})
class WebApp(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Container")

@SevenftNode.metadata({
    "name": "Single Page App",
    "description": "C# Web application"
})
class SPA(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Container")

@SevenftNode.metadata({
    "name": "API",
    "description": "C# application"
})
class API(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Container")

@SevenftNode.metadata({
    "name": "Android App"
})
class MobileApp(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Container")

@SevenftNode.metadata({
    "name": "Oracle DB"
})
class OracleDB(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Container")

@SevenftNode.metadata({
    "name": "Our Custom App"
})
class CustomA(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "Custom")

#@markdown ----------------------------------------------
#@markdown ## External Systems

@SevenftNode.metadata({
    "name": "Email System",
    "description": "Microsoft Exchange"
})
class Email(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "System")

@SevenftNode.metadata({
    "name": "Mainframe System",
    "description": "AS400"
})
class Mainframe(SevenftNode):
  def __init__(self):
    SevenftNode.__init__(self, "System")
