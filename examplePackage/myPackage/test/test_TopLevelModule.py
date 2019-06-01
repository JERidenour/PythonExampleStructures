from unittest import TestCase
from myPackage import TopLevelModule
import pkg_resources
import json

class TestTopLevelClass(TestCase):
    def test_member(self):
        topLevelClass = TopLevelModule.TopLevelClass()
        self.assertTrue(isinstance(topLevelClass.member, str))

class TestTopLevelFunction(TestCase):
    def test_function(self):
        retval = TopLevelModule.TopLevelFunction()
        self.assertEqual(retval, "Top Level Function")

class TestTopLevelData(TestCase):
    def test_data(self):
        dataString = pkg_resources.resource_string("myPackage", "data/TopLevelData.json")
        topLevelData = json.loads(dataString)
        self.assertEqual(topLevelData["element1"]["subElement1"], 1)
