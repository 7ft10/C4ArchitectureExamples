#@title Repository
from urllib import request
from SeventFtNode import SevenftNode

baseUrl = "https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/"

#@markdown # Imports
request.urlretrieve(baseUrl + 'SeventFtNode.py', '_SeventFtNode_.py')
from _SeventFtNode_ import SevenftNode

#@markdown ## Personas

InternalUser = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Personas/Internal%20User.yaml')

#@markdown # Systems

Disc = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Systems/Disc.yaml')
##Bamboo = SevenftNode.LoadFromYaml(baseUrl + 'Repository/Systems/Bamboo.yaml')
