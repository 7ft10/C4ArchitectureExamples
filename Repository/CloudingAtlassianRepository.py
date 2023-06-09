#@title Repository
from urllib import request
from Repository.SeventFtNode import SevenftNode

baseUrl = "https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/"

#@markdown # Imports
request.urlretrieve(baseUrl + 'Repository/SeventFtNode.py', '_SeventFtNode_.py')
from _SeventFtNode_ import SevenftNode

#@markdown ## Personas
class cPersonas():
  def __init__(self):
    self.InternalUser:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Personas/Internal%20User.yaml')
    self.ExternalUser:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Personas/External%20User.yaml')
    self.RemoteUser:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Personas/Remote%20User.yaml')

globals()['Personas'] = cPersonas()

#@markdown # Internal Systems
class cInternalSystems():
  def __init__(self):
    self.Disc:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/Disc.yaml')
    self.Bamboo:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/Bamboo.yaml')
    self.Confluence:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/Confluence.yaml')

globals()['InternalSystems'] = cInternalSystems()

#@markdown # External Systems
class cExternalSystems():
  def __init__(self):
    self.NewRelic:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/External%20Systems/New%20Relic.yaml')

globals()['ExternalSystems'] = cExternalSystems()