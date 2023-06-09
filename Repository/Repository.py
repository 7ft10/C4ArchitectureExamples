#@title Repository
from urllib import request

baseUrl = "https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/"
request.urlretrieve(baseUrl + 'Repository/SeventFtNode.py', '_SeventFtNode_.py')
from _SeventFtNode_ import SevenftNode

#@markdown ## Personas
class cPersonas():
  def __init__(self):
    self.BankingCustomer:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Personas/Banking%20Customer.yaml')

globals()['Personas'] = cPersonas()

#@markdown # Internal Systems
class cSystems():
  def __init__(self):
    self.API:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Systems/API.yaml')
    self.CustomA:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Systems/CustomA.yaml')
    self.Email:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Systems/Email.yaml')
    self.Mainframe:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Systems/Mainframe.yaml')
    self.MobileApp:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Systems/MobileApp.yaml')
    self.OracleDB:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Systems/OracleDB.yaml')
    self.SPA:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Systems/SPA.yaml')
    self.WebApp:SevenftNode = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Systems/WebApp.yaml')

globals()['Systems'] = cSystems()
