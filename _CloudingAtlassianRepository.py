#@title Repository
from SeventFt10.C4.Repository import Repository
from SeventFt10.C4.Factory import Factory
from SeventFt10.C4.Diagrams import C4Node

baseUrl = "https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/"

#@markdown ## Personas
class _Personas(Repository):
  def __init__(self):
    self.InternalUser:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Personas/Internal%20User.yaml')
    self.ExternalUser:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Personas/External%20User.yaml')
    self.RemoteUser:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Personas/Remote%20User.yaml')
globals()['Personas'] = _Personas()

#@markdown # Internal Systems
class _InternalSystems(Repository):
  def __init__(self):
    self.ActiveDirectory:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Internal%20Systems/ActiveDirectory.yaml')
    self.Bamboo:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Internal%20Systems/Bamboo.yaml')
    self.BitBucket:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Internal%20Systems/BitBucket.yaml')
    self.Citrix:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Internal%20Systems/Citrix.yaml')
    self.Confluence:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Internal%20Systems/Confluence.yaml')
    self.ConfluenceNonProd:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Internal%20Systems/ConfluenceNonProd.yaml')
    self.Disc:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Internal%20Systems/Disc.yaml')
    self.GitLab:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Internal%20Systems/GitLab.yaml')
    self.GlobalProtect:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Internal%20Systems/GlobalProtect.yaml')
    self.Intranet:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Internal%20Systems/Intranet.yaml')
    self.Jenkins:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Internal%20Systems/Jenkins.yaml')
    self.Jira:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Internal%20Systems/Jira.yaml')
    self.JiraNonProd:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Internal%20Systems/JiraNonProd.yaml')
    self.Okta:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Internal%20Systems/Okta.yaml')
    self.PowerBi:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Internal%20Systems/PowerBi.yaml')
    self.ServiceNow:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/Internal%20Systems/ServiceNow.yaml')
globals()['InternalSystems'] = _InternalSystems()

#@markdown # External Systems
class _ExternalSystems(Repository):
  def __init__(self):
    self.ConfluenceCloud:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/External%20Systems/ConfluenceCloud.yaml')
    self.JiraCloud:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/External%20Systems/JiraCloud.yaml')
    self.NewRelic:C4Node = Factory.LoadFromYaml(baseUrl + 'CloudingRepository/External%20Systems/New%20Relic.yaml')
globals()['ExternalSystems'] = _ExternalSystems()
