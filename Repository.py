#@title Respository
from urllib.request import urlretrieve

#@markdown ----------------------------------------------
#@markdown # Our Systems
class OurSystems():

  #@markdown + Web Application (WebApp)
  def WebApp(): 
    return {
      "name" : "Web Application", 
      "technology" : "Java and Spring MVC", 
      "description" : "Delivers the static content and the Internet banking single page application.",
      "tech-radar-ring" : "adopt",
      "tech-radar-quadrant" : "tools",
      "isNew" : "TRUE"
    }

  #@markdown + Single Page Application (SPA)
  def SPA(): 
    return { 
      "name" : "Single-Page Application",
      "technology" : "Javascript and Angular",
      "description" : "Provides all of the Internet banking functionality to customers via their web browser.",
    }

  #@markdown + Mobile Application (MobileApp)
  def MobileApp(): 
    return { 
      "name" : "Mobile App",
      "technology" : "Xamarin",
      "description" : "Provides a limited subset of the Internet banking functionality to customers via their mobile device.",
    }

  #@markdown + Application Programming Interface (API)
  def API():
    return { 
      "name" : "API Application",
      "technology" : "Java and Spring MVC",
      "description" : "Provides Internet banking functionality via a JSON/HTTPS API.",
    }

  #@markdown + Customer Application (CustomerA)
  def CustomA():
    diagrams_icon = "diagrams.png"
    urlretrieve("https://github.com/mingrammer/diagrams/raw/master/assets/img/diagrams.png", diagrams_icon)
    return { 
      "label" : "Custom Application",
      "icon_path" : diagrams_icon
    }

#@markdown ---
#@markdown # Our Data Stores
class OurDataStores(): 

  #@markdown + Oracle Database (OracleDB)
  def OracleDB(): 
    return { 
      "name" : "Oracle DB",
      "technology" : "Oracle Database",
      "description" : "Stores user registration information, hashed authentication credentials, access logs, etc.",
    }

#@markdown ----------------------------------------------
#@markdown # Our External Systems
class OurExternalSystems(): 

  #@markdown + E-mail System (Email)
  def Email(): 
    return { 
      "name" : "E-mail System", 
      "description" : "The internal Microsoft Exchange e-mail system.", 
      "external" : True
    }

  #@markdown + Mainframe Banking System (Mainframe)
  def Mainframe(): 
    return { 
      "name" : "Mainframe Banking System",
      "description" : "Stores all of the core banking information about customers, accounts, transactions, etc.",
      "external" : True
    }

#@markdown ----------------------------------------------
#@markdown # Our Personas
class OurPersonas(): 

  #@markdown + Banking Customer (BankingCustomer)
  def BankingCustomer(): 
    return {
      "name" : "Personal Banking Customer", 
      "description" : "A customer of the bank, with personal bank accounts."
    }
