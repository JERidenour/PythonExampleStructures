import mySubPackageA
import mySubPackageB
from mySubPackageA import MidLevelModule
from mySubPackageB import MidLevelModule as AnotherMidLevelModule
from mySubPackageA.mySubSubPackageA import LowLevelModule
from mySubPackageA.mySubSubPackageB import LowLevelModule as AnotherLowLevelModule
import pkg_resources
import json

# from myNamespace/mySubPackageA:
midLevelClass = MidLevelModule.MidLevelClass()
print(midLevelClass.member)
print(MidLevelModule.MidLevelFunction())
dataString = pkg_resources.resource_string("mySubPackageA", "data/MidLevelData.json")
midLevelData = json.loads(dataString)
print("Mid Level Data:")
print(midLevelData["element2"])

# from myNamespace/mySubPackageB:
anotherMidLevelClass = AnotherMidLevelModule.MidLevelClass()
print(anotherMidLevelClass.member)
print(AnotherMidLevelModule.MidLevelFunction())
dataString = pkg_resources.resource_string("mySubPackageB", "data/MidLevelData.json")
moreMidLevelData = json.loads(dataString)
print("More Mid Level Data:")
print(moreMidLevelData["element2"])

# from myNamespace/mySubPackageA/mySubSubPackageA:
lowLevelClass = LowLevelModule.LowLevelClass()
print(lowLevelClass.member)
print(LowLevelModule.LowLevelFunction())
dataString = pkg_resources.resource_string("mySubPackageA.mySubSubPackageA", "data/LowLevelData.json")
LowLevelData = json.loads(dataString)
print("Low Level Data:")
print(LowLevelData["element1"])

# from myNamespace/mySubPackageA/mySubSubPackageB:
anotherLowLevelClass = AnotherLowLevelModule.LowLevelClass()
print(anotherLowLevelClass.member)
print(AnotherLowLevelModule.LowLevelFunction())
dataString = pkg_resources.resource_string("mySubPackageA.mySubSubPackageB", "data/LowLevelData.json")
moreLowLevelData = json.loads(dataString)
print("More Low Level Data:")
print(moreLowLevelData["element2"])
