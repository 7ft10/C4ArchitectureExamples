#@title Repository
from SeventFt10.C4.Repository import Repository
from SeventFt10.C4.Factory import Factory
from SeventFt10.C4.Diagrams import C4Node

baseUrl = "https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/"

#@markdown ## Personas
class _Personas(Repository):
  def __init__(self):
    self.BankingCustomer:C4Node = Factory.LoadFromYaml(baseUrl + 'Repository/Personas/Banking%20Customer.yaml')
globals()['Personas'] = _Personas()

#@markdown # Internal Systems
class _Systems(Repository):
  def __init__(self):
    self.InternetBankingSystem:C4Node = Factory.LoadFromYaml(baseUrl + 'Repository/Systems/InternetBankingSystem.yaml')
    self.Email:C4Node = Factory.LoadFromYaml(baseUrl + 'Repository/Systems/Email.yaml')
    self.Mainframe:C4Node = Factory.LoadFromYaml(baseUrl + 'Repository/Systems/Mainframe.yaml')
globals()['Systems'] = _Systems()

#@markdown # Internal Applications
class _Applications(Repository):
  def __init__(self):
    self.API:C4Node = Factory.LoadFromYaml(baseUrl + 'Repository/Applications/API.yaml')
    self.MobileApp:C4Node = Factory.LoadFromYaml(baseUrl + 'Repository/Applications/MobileApp.yaml')
    self.Database:C4Node = Factory.LoadFromYaml(baseUrl + 'Repository/Applications/Database.yaml')
    self.SPA:C4Node = Factory.LoadFromYaml(baseUrl + 'Repository/Applications/SPA.yaml')
    self.WebApp:C4Node = Factory.LoadFromYaml(baseUrl + 'Repository/Applications/WebApp.yaml')
globals()['Applications'] = _Applications()
