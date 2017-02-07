# -*- coding: utf-8 -*-

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Development Team: Stanislav WEB
"""

import unittest2 as unittest
from StringIO import StringIO
from mock import patch
from src.lib.tpl import Tpl, TplError


class TestTpl(unittest.TestCase):
    """TestTpl class"""

    def tearDown(self):
        StringIO().flush()

    def prompt_answer(self):
        ans = Tpl.prompt(msg='fake')
        return ans

    def test_prompt(self):
        """ Tpl.prompt() test """

        with patch('__builtin__.raw_input', return_value='fake') as _raw_input:
            self.assertEqual(self.prompt_answer(), 'fake')
            _raw_input.assert_called_once_with('fake')
    

    def test_line(self):
        """ Tpl.line() test """

        expected = Tpl.line('test')
        self.assertTrue('test' in expected)
    
    def test_line_with_key(self):
        """ Tpl.line() test with key """
        
        expected = Tpl.line(key='report', plugin='testplugin', dest='testdst')
        self.assertTrue('testplugin' in expected)
        self.assertTrue('testdst' in expected)

    def test_line_log(self):
        """ Tpl.line_log() test """

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            Tpl.line_log('test_line_log')
            self.assertTrue('test_line_log' in fakeOutput.getvalue().strip())

    def test_message(self):
        """ Tpl.message() test """

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            Tpl.message('test_message')
            self.assertTrue('test_message' in fakeOutput.getvalue().strip())

    def test_info(self):
        """ Tpl.info() test """

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            Tpl.info('test_info')
            self.assertTrue('test_info' in fakeOutput.getvalue().strip())

    def test_error(self):
        """ Tpl.error() test """

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            Tpl.error('test_error')
            self.assertTrue('test_error' in fakeOutput.getvalue().strip())

    def test_warning(self):
        """ Tpl.warning() test """

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            Tpl.warning('test_warning')
            self.assertTrue('test_warning' in fakeOutput.getvalue().strip())

    def test_line_error_key(self):
        """ Tpl.line() exception test """

        undefined = 'undefined'
        with self.assertRaises(TplError) as context:
            Tpl.line(key=undefined)
        self.assertTrue(undefined in str(context.exception))
        self.assertTrue(TplError == context.expected)

if __name__ == "__main__":
    unittest.main()