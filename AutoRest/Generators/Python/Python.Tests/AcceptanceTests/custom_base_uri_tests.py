﻿# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

import unittest
import subprocess
import sys
import isodate
import os
from datetime import date, datetime, timedelta
from os.path import dirname, pardir, join, realpath, sep, pardir

cwd = dirname(realpath(__file__))
root = realpath(join(cwd , pardir, pardir, pardir, pardir, pardir))
sys.path.append(join(root, "ClientRuntimes" , "Python", "msrest"))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "CustomBaseUri"))

from msrest.exceptions import (
    DeserializationError,
    SerializationError,
    ClientRequestError,
    ValidationError)

from autorestparameterizedhosttestclient import (
    AutoRestParameterizedHostTestClient,
    AutoRestParameterizedHostTestClientConfiguration)

from autorestparameterizedhosttestclient.models import Error, ErrorException


class CustomBaseUriTests(unittest.TestCase):

    def test_custom_base_uri_positive(self):
        config = AutoRestParameterizedHostTestClientConfiguration(
            "host:3000")

        config.log_level = log_level
        client = AutoRestParameterizedHostTestClient(config)
        client.paths.get_empty("local")

    def test_custom_base_uri_negative(self):
        config = AutoRestParameterizedHostTestClientConfiguration(
            "host:3000")

        config.log_level = log_level
        config.retry_policy.retries = 0
        client = AutoRestParameterizedHostTestClient(config)

        with self.assertRaises(ClientRequestError):
            client.paths.get_empty("bad")

        with self.assertRaises(ValidationError):
            client.paths.get_empty(None)

        client.config.host = "badhost:3000"
        with self.assertRaises(ClientRequestError):
            client.paths.get_empty("local")

if __name__ == '__main__':
    
    
    unittest.main()