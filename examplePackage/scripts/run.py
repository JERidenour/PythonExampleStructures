import myPackage
from myPackage import TopLevelModule
from myPackage.mySubPackageA import MidLevelModule
from myPackage.mySubPackageB import MidLevelModule as AnotherMidLevelModule
from myPackage.mySubPackageA.mySubSubPackageA import LowLevelModule
from myPackage.mySubPackageA.mySubSubPackageB import LowLevelModule as AnotherLowLevelModule
import pkg_resources
import json

# from the myPackage root:
topLevelClass = TopLevelModule.TopLevelClass()
print(topLevelClass.member)
print(TopLevelModule.TopLevelFunction())
dataString = pkg_resources.resource_string("myPackage", "data/TopLevelData.json")
topLevelData = json.loads(dataString)
print("Top Level Data:")
print(topLevelData["element1"])

# from myPackage/mySubPackageA:
midLevelClass = MidLevelModule.MidLevelClass()
print(midLevelClass.member)
print(MidLevelModule.MidLevelFunction())
dataString = pkg_resources.resource_string("myPackage.mySubPackageA", "data/MidLevelData.json")
midLevelData = json.loads(dataString)
print("Mid Level Data:")
print(midLevelData["element2"])

# from myPackage/mySubPackageB:
anotherMidLevelClass = AnotherMidLevelModule.MidLevelClass()
print(anotherMidLevelClass.member)
print(AnotherMidLevelModule.MidLevelFunction())
dataString = pkg_resources.resource_string("myPackage.mySubPackageB", "data/MidLevelData.json")
moreMidLevelData = json.loads(dataString)
print("More Mid Level Data:")
print(moreMidLevelData["element2"])

# from myPackage/mySubPackageA/mySubSubPackageA:
lowLevelClass = LowLevelModule.LowLevelClass()
print(lowLevelClass.member)
print(LowLevelModule.LowLevelFunction())
dataString = pkg_resources.resource_string("myPackage.mySubPackageA.mySubSubPackageA", "data/LowLevelData.json")
LowLevelData = json.loads(dataString)
print("Low Level Data:")
print(LowLevelData["element1"])

# from myPackage/mySubPackageA/mySubSubPackageB:
anotherLowLevelClass = AnotherLowLevelModule.LowLevelClass()
print(anotherLowLevelClass.member)
print(AnotherLowLevelModule.LowLevelFunction())
dataString = pkg_resources.resource_string("myPackage.mySubPackageA.mySubSubPackageB", "data/LowLevelData.json")
moreLowLevelData = json.loads(dataString)
print("More Low Level Data:")
print(moreLowLevelData["element2"])
