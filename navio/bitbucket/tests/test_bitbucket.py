import pytest
import os
import sys


class TestImport:

    def test_import(self):
        import navio.bitbucket
        from navio.bitbucket import Bitbucket


class Test:

    def test_is_bitbucket(self):
        from navio.bitbucket import Bitbucket

        os.environ.pop('CI', None)
        assert not Bitbucket().is_bitbucket()

        os.environ['CI'] = 'true'
        assert Bitbucket().is_bitbucket()

        os.environ['CI'] = 'false'
        assert not Bitbucket().is_bitbucket()

        os.environ['CI'] = '???'
        assert not Bitbucket().is_bitbucket()

    def test_is_pull_request(self):
        from navio.bitbucket import Bitbucket

        os.environ.pop('BITBUCKET_PR_ID', None)
        assert not Bitbucket().is_pull_request()

        os.environ['CI'] = 'true'

        os.environ['BITBUCKET_PR_ID'] = '123'
        assert Bitbucket().is_pull_request()

        os.environ['BITBUCKET_PR_ID'] = '456'
        assert Bitbucket().is_pull_request()

        os.environ['BITBUCKET_PR_ID'] = '???'
        assert Bitbucket().is_pull_request()

    def test_branch(self):
        from navio.bitbucket import Bitbucket

        os.environ['CI'] = 'true'
        os.environ.pop('BITBUCKET_BRANCH', None)

        assert Bitbucket().branch() is None

        os.environ['BITBUCKET_BRANCH'] = 'master'
        assert 'master' == Bitbucket().branch()

        os.environ['BITBUCKET_BRANCH'] = 'prod'
        assert 'prod' == Bitbucket().branch()

    def test_commit_hash(self):
        from navio.bitbucket import Bitbucket

        os.environ['CI'] = 'true'
        os.environ.pop('BITBUCKET_COMMIT', None)

        assert '000000000000000000000000000000' == Bitbucket().commit_hash()

        os.environ['BITBUCKET_COMMIT'] = '1f510ab451bb4'
        assert '1f510ab451bb4' == Bitbucket().commit_hash()

        os.environ['BITBUCKET_COMMIT'] = '04124124bcb131'
        assert '04124124bcb131' == Bitbucket().commit_hash()

    def test_short_commit_hash(self):
        from navio.bitbucket import Bitbucket

        os.environ['CI'] = 'true'
        os.environ.pop('BITBUCKET_COMMIT', None)

        assert '00000000' == Bitbucket().commit_hash()

        os.environ['BITBUCKET_COMMIT'] = '1f510ab451bb4'
        assert '1f510ab4' == Bitbucket().commit_hash()

        os.environ['BITBUCKET_COMMIT'] = '04124124bcb131'
        assert '04124124' == Bitbucket().commit_hash()
