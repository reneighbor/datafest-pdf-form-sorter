import logging
from datafest_politics.doctype import DocType
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises

class TestDocType(object):
    @classmethod
    def setUp(klass):
        pass

    def test_identify_file_match_100_percent(klass):
        foo_strings =  [
            "Goldilocks",
            "bear",
            "granny",
            "hunter"
        ]
        doctype = DocType("goldilocks", foo_strings)

        filename = "file_0"
        filetext = "Goldilocks and the bear ate the granny after they ate the hunter"
        
        doctype.identify_file_match(filename, filetext)
        assert("file_0" in doctype.matching_files.keys())
        assert_equal(doctype.matching_files["file_0"], 1.0)

    def test_identify_file_match_75_percent(klass):
        foo_strings =  [
            "Goldilocks",
            "bear",
            "granny",
            "hunter"
        ]
        doctype = DocType("goldilocks", foo_strings)

        filename = "file_0"
        filetext = "Goldilocks and the bear ate the granny after they ate the reporter"
        
        doctype.identify_file_match(filename, filetext)
        assert("file_0" in doctype.matching_files.keys())
        assert_equal(doctype.matching_files["file_0"], 0.75)

    def test_identify_file_match_zero(klass):
        foo_strings =  [
            "Goldilocks",
            "bear",
            "granny",
            "hunter"
        ]
        doctype = DocType("goldilocks", foo_strings)

        filename = "file_0"
        filetext = "The quick red fox jumped over the lazy brown dog"
        
        doctype.identify_file_match(filename, filetext)
        assert("file_0" not in doctype.matching_files.keys())

