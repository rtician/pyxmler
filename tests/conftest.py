from collections import OrderedDict

import pytest


def _create_dict_header(root):
    d = OrderedDict()
    d[root] = OrderedDict()
    d[root]['@ns'] = 'soapenv'
    d[root]['@attrs'] = OrderedDict()
    d[root]['@attrs']['xmlns:soapenv'] = 'http://schemas.xmlsoap.org/soap/envelope/'
    return d


@pytest.fixture
def simple_dict():
    d = _create_dict_header('RootTag')
    d['RootTag']['childTag'] = OrderedDict()
    d['RootTag']['childTag']['@attrs'] = OrderedDict()
    d['RootTag']['childTag']['@attrs']['someAttribute'] = 'colors are nice'
    d['RootTag']['childTag']['grandchild'] = 'This is a text tag'

    return d


@pytest.fixture
def multi_type_dict():
    d = _create_dict_header('Root')
    d['Root']['Header'] = ''
    d['Root']['Body'] = OrderedDict()
    d['Root']['Body']['tag1'] = [1, 2, 3]
    d['Root']['Body']['tag2'] = OrderedDict()
    d['Root']['Body']['tag2']['child1'] = ' '
    d['Root']['Body']['tag3'] = 1.0
    d['Root']['Body']['tag4'] = {1, 2, 3}
    d['Root']['Body']['tag5'] = False
    d['Root']['Body']['tag6'] = tuple()
    d['Root']['Body']['tag7'] = None

    return d


@pytest.fixture
def multi_attr_dict():
    d = _create_dict_header('Envelope')
    d['Envelope']['Header'] = ''
    d['Envelope']['Body'] = OrderedDict()
    d['Envelope']['Body']['tag1'] = OrderedDict()
    d['Envelope']['Body']['tag1']['@name'] = 'first_tag'
    d['Envelope']['Body']['tag1']['@value'] = 'foo bar'
    d['Envelope']['Body']['tag2'] = 'some value'

    return d
