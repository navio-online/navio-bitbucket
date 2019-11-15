import pytest
import os
import sys


class TestImport:

    def test_import(self):
        import navio.bitbucket
        from navio.bitbucket import Travis


class Test:

    def test_is_bitbucket(self):
        from navio.bitbucket import Travis

        os.environ.pop('CI', None)
        assert not Travis().is_bitbucket()

        os.environ['CI'] = 'true'
        assert Travis().is_bitbucket()

        os.environ['CI'] = 'false'
        assert not Travis().is_bitbucket()

        os.environ['CI'] = '???'
        assert not Travis().is_bitbucket()

    def test_is_pull_request(self):
        from navio.bitbucket import Travis

        os.environ.pop('BITBUCKET_PR_ID', None)
        assert not Travis().is_pull_request()

        os.environ['CI'] = 'true'

        os.environ['BITBUCKET_PR_ID'] = 'true'
        assert Travis().is_pull_request()

        os.environ['BITBUCKET_PR_ID'] = 'false'
        assert not Travis().is_pull_request()

        os.environ['BITBUCKET_PR_ID'] = '???'
        assert not Travis().is_pull_request()

    def test_branch(self):
        from navio.bitbucket import Travis

        os.environ['CI'] = 'true'
        os.environ.pop('BITBUCKET_BRANCH', None)

        assert Travis().branch() is None

        os.environ['BITBUCKET_BRANCH'] = 'master'
        assert 'master' == Travis().branch()

        os.environ['BITBUCKET_BRANCH'] = 'prod'
        assert 'prod' == Travis().branch()

    def test_commit_hash(self):
        from navio.bitbucket import Travis

        os.environ['CI'] = 'true'
        os.environ.pop('BITBUCKET_COMMIT', None)

        assert '000000000000000000000000000000' == Travis().commit_hash()

        os.environ['BITBUCKET_COMMIT'] = '1f510ab451bb4'
        assert '1f510ab451bb4' == Travis().commit_hash()

        os.environ['BITBUCKET_COMMIT'] = '04124124bcb131'
        assert '04124124bcb131' == Travis().commit_hash()
