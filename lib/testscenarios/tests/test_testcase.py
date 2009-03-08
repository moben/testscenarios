#  testscenarios: extensions to python unittest to allow declarative
#  dependency injection ('scenarios') by tests.
#  Copyright (C) 2009  Robert Collins <robertc@robertcollins.net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

import unittest

import testscenarios
from testtools.tests.helpers import LoggingResult


class TestTestWithScenarios(unittest.TestCase):

    def test_no_scenarios_no_error(self):
        class ReferenceTest(testscenarios.TestWithScenarios):
            def test_pass(self):
                pass
        test = ReferenceTest("test_pass")
        result = unittest.TestResult()
        test.run(result)
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(1, result.testsRun)

    def test_with_one_scenario_one_run(self):
        class ReferenceTest(testscenarios.TestWithScenarios):
            scenarios = [('demo', {})]
            def test_pass(self):
                pass
        test = ReferenceTest("test_pass")
        log = []
        result = LoggingResult(log)
        test.run(result)
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(1, result.testsRun)
        self.assertEqual(
            'testscenarios.tests.test_testcase.ReferenceTest.test_pass(demo)',
            log[0][1].id())

    def test_with_two_scenarios_two_run(self):
        class ReferenceTest(testscenarios.TestWithScenarios):
            scenarios = [('1', {}), ('2', {})]
            def test_pass(self):
                pass
        test = ReferenceTest("test_pass")
        log = []
        result = LoggingResult(log)
        test.run(result)
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(2, result.testsRun)
        self.assertEqual(
            'testscenarios.tests.test_testcase.ReferenceTest.test_pass(1)',
            log[0][1].id())
        self.assertEqual(
            'testscenarios.tests.test_testcase.ReferenceTest.test_pass(2)',
            log[4][1].id())
