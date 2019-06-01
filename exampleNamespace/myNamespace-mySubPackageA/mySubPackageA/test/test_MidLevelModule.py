from unittest import TestCase
from mySubPackageA import MidLevelModule
import pkg_resources
import json

class TestMidLevelClass(TestCase):
    def test_member(self):
        midLevelClass = MidLevelModule.MidLevelClass()
        self.assertTrue(isinstance(midLevelClass.member, str))

class TestMidLevelFunction(TestCase):
    def test_function(self):
        retval = MidLevelModule.MidLevelFunction()
        self.assertEqual(retval, "Mid Level Function")

class TestMidLevelData(TestCase):
    def test_data(self):
        dataString = pkg_resources.resource_string("mySubPackageA", "data/MidLevelData.json")
        midLevelData = json.loads(dataString)
        self.assertEqual(midLevelData["element1"]["subElement2"], 2)
