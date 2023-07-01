#@title Repository
from urllib import request

baseUrl = "https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/"
##[name, response] = request.urlretrieve(baseUrl + 'Library/SeventFtNode.py', '_SeventFtNode.py')
##from _SeventFtNode import SevenftRepository, SevenftNode

from Library.SeventFtNode import SevenftRepository, SevenftNode

#@markdown ## Personas
class _Personas(SevenftRepository):
  def __init__(self):
    self.BankingCustomer:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Personas/Banking%20Customer.yaml')
globals()['Personas'] = _Personas()

#@markdown # Internal Systems
class _Systems(SevenftRepository):
  def __init__(self):
    self.InternetBankingSystem:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Systems/InternetBankingSystem.yaml')
    self.Email:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Systems/Email.yaml')
    self.Mainframe:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Systems/Mainframe.yaml')
globals()['Systems'] = _Systems()

#@markdown # Internal Applications
class _Applications(SevenftRepository):
  def __init__(self):
    self.API:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Applications/API.yaml')
    self.MobileApp:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Applications/MobileApp.yaml')
    self.Database:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Applications/Database.yaml')
    self.SPA:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Applications/SPA.yaml')
    self.WebApp:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Applications/WebApp.yaml')
globals()['Applications'] = _Applications()
