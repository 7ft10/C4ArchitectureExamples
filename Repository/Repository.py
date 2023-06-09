#@title Repository
from urllib import request
from SeventFtNode import SevenftNode

baseUrl = "https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/"

#@markdown # Imports
request.urlretrieve(baseUrl + 'SeventFtNode.py', '_SeventFtNode_.py')
from _SeventFtNode_ import SevenftNode

#@markdown ## Personas
class cPersonas():
  def __init__(self):
    self.InternalUser = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Personas/Internal%20User.yaml')

globals()['Personas'] = cPersonas()

#@markdown # Internal Systems
class cInternalSystems():
  def __init__(self):
    self.Disc = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Systems/Disc.yaml')
    self.Bamboo = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Systems/Bamboo.yaml')
    self.Confluence = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Systems/Confluence.yaml')

globals()['InternalSystems'] = cInternalSystems()