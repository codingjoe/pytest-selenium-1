# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

import pytest

pytestmark = pytest.mark.nondestructive


def test_launch(testdir):
    binary = 'chromedriver'
    paths = os.environ['PATH'].split(os.pathsep)
    if not any(map(lambda x: os.path.isfile(x) and os.access(x, os.X_OK),
                   [os.path.join(path, binary) for path in paths])):
        pytest.skip('{} not found on path'.format(binary))

    file_test = testdir.makepyfile("""
        import pytest
        @pytest.mark.nondestructive
        def test_pass(webtext):
            assert webtext == u'Success!'
    """)
    testdir.quick_qa('--driver', 'Chrome', file_test, passed=1)
