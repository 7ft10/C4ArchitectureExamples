# C4 Architecture Examples

## Why

Keeping architecture diagrams up to date is difficult. Creating them is just as difficult. Architects spend most of their time gathering the right icons, drawing lines in Miro or Visio making sure that they are the right type etc. etc. etc. What a waste of time.

Instead architects should be focused on ensuring that the current state is correct and that proposed changes to the enterprise ecosystem have taken into account all other systems that may be impacted.

Architecture diagrams as code (ADAC) is a way of allowing architects to focus on the right things and stop wasting time. It can also help other areas of the business by creating or leveraging a configuration management database (CMDB).

ADAC can also be extended to include the personas that interact with the systems. This is an important part of the impact analysis and can be the starting point for other agile techniques such as epic and story writing.

## Guide

Colab is a free tool for google users to run end edit Jupyter files which makes it a perfect candidate for any company but especially a company that uses google drive. It is possible to connect this repository to Google Drive and/or Github for further document control and archiving.

*C4 Model* is a great starting point for any architecture diagram repository as they can easily map to the the levels of testing, for example context is system testing, code is unit testing. With the right diagrams and subsequently the right level of thinking architecture, development and testing can all use the same diagrams to create meaningful and valuable assets for the company. See <https://c4model.com/> for more details.

*SeventFt10.Python.C4diagrams* is a Python library that uses the *diagrams* library, to create diagrams from code. See <https://diagrams.mingrammer.com/docs/nodes/c4> for more details.

## How to run

Run notebook cells in order. The simplest way to do this is Ctrl-F9 to "Run all".

## Create Repository

The repository can be extracted into a stand alone Python file (.py) based on a set of YAML files. The YAML files can be generated from the CMDB or whatever. Note: Json or any other kind of simple text based storage could also be used.

Create a set of YAML files, like the following, called API.yaml:

```YAML
id: API
nodeType: Container
name: API
description: |-
  Python application
```

These are the default identification names of a container. More attributes can be added, such as..

```YAML
id: API
nodeType: Container
name: API
description: |-
  Python application
server: 192.168.0.1
port: 8080
sourceCodeLocation: github/dddd
```

These attributes can be used for other details within the diagrams.

A repository has namespaces encapsulate the systems, personas, etc. The following example shows a persona namespace with a banking customer persona loaded from the repository yaml file.

```python
class _Personas(SevenftRepository):
  def __init__(self):
    self.BankingCustomer:C4Node = Factory.LoadYamlFromUrl('Repository/Personas/Banking%20Customer.yaml')
globals()['Personas'] = _Personas()
```

The final line puts the personas into the global namespace.

First step is to load the library

```python
import os
result = os.system('pip install git+https://github.com/7ft10/SeventFt10.Python.C4diagrams/')
```

or via the requirements.txt file. 

The repository can then be loaded like this...

```python
from SeventFt10.C4 import Repository
Repo = Repository.LoadFromUrl('https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/Repository/', module_name = "Repository")
```

Then the personas, systems etc. are loaded via the Repo variable using the get function.

```python
with Diagram(** settings) as diagram:
  banking_customer = Repo.Personas.BankingCustomer.Get()
```

Repositories could also be versioned and released as required with leadership oversight and approvals. There could also be current state and future state repositories which update as new systems are added and retired.

### Printed

To display all elements within the namespace use the print function.

```python
Personas.Print()
```

Or to print a specific element's details, use the print function on the element.

```python
Personas.BankingCustomer.DisplayMarkdown()
```

There is also a generic DisplayMarkdown() function that can be used.

### Images

Custom icons and elements can also be created with the icon url added as a url parameter, such as

```yaml
id: GitLab
nodeType: Custom
name: GitLab
description: |-
  GitLab
icon: https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/Repository/Internal%20Systems/GitLab.png

```

The created images can be exported to google drive or downloaded manually and included in confluence documentation. There is also Jupyter plugins for confluence that allow for visualisation (e.g. <https://marketplace.atlassian.com/apps/1220365/jupyter-notebook-viewer-for-confluence?tab=overview&hosting=cloud>)
