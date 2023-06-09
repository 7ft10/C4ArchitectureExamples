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
    self.ActiveDirectory:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/ActiveDirectory.yaml')
    self.Bamboo:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/Bamboo.yaml')
    self.BitBucket:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/BitBucket.yaml')
    self.Citrix:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/Citrix.yaml')
    self.Confluence:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/Confluence.yaml')
    self.ConfluenceNonProd:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/ConfluenceNonProd.yaml')
    self.Disc:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/Disc.yaml')
    self.GitLab:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/GitLab.yaml')
    self.GlobalProtect:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/GlobalProtect.yaml')
    self.Intranet:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/Intranet.yaml')
    self.Jenkins:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/Jenkins.yaml')
    self.Jira:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/Jira.yaml')
    self.JiraNonProd:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/JiraNonProd.yaml')
    self.Okta:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/Okta.yaml')
    self.PowerBi:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/PowerBi.yaml')
    self.ServiceNow:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Internal%20Systems/ServiceNow.yaml')

globals()['InternalSystems'] = cInternalSystems()

#@markdown # External Systems
class cExternalSystems():
  def __init__(self):
    self.ConfluenceCloud:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/External%20Systems/ConfluenceCloud.yaml')
    self.JiraCloud:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/External%20Systems/JiraCloud.yaml')
    self.NewRelic:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/External%20Systems/New%20Relic.yaml')

globals()['ExternalSystems'] = cExternalSystems()