from unittest import TestCase
from mySubPackageA.mySubSubPackageA import LowLevelModule
import pkg_resources
import json

class TestLowLevelClass(TestCase):
    def test_member(self):
        lowLevelClass = LowLevelModule.LowLevelClass()
        self.assertTrue(isinstance(lowLevelClass.member, str))

class TestLowLevelFunction(TestCase):
    def test_function(self):
        retval = LowLevelModule.LowLevelFunction()
        self.assertEqual(retval, "Low Level Function")

class TestLowLevelData(TestCase):
    def test_data(self):
        dataString = pkg_resources.resource_string("mySubPackageA.mySubSubPackageA", "data/LowLevelData.json")
        LowLevelData = json.loads(dataString)
        self.assertEqual(LowLevelData["element2"]["subElement1"], 1)
