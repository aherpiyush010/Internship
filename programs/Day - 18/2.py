# Abstract Class for File Parsers
# Create an abstract class named FileParser with an abstract method parse(data).
# Create concrete classes:
# JSONParser that implements parse(data) method and prints: “Parsing JSON data...”
# XMLParser that implements parse(data) method and prints: “Parsing XML data...”
# # Test both classes.

from abc import ABC, abstractmethod
class FilePerser(ABC):
    @abstractmethod
    def perse(data):
        pass
        
class JSONParser(FilePerser):
    def perse(self,data):
        print(data)
        
class XMLParser(FilePerser):
    def perse(self,data):
        print(data)
        
obj = XMLParser()
ob = JSONParser()
ob.perse("Parsing JSON data...")
obj.perse("Parsing XML data ...")