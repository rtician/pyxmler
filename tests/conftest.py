import pytest


@pytest.fixture
def simple_dict():
    return {
        'RootTag': {
            '@ns': 'soapenv',
            '@attrs': {
                'xmlns:soapenv': 'http://schemas.xmlsoap.org/soap/envelope/'
            },
            'childTag': {
                '@attrs': {
                    'someAttribute': 'colors are nice'
                },
                'grandchild': 'This is a text tag'
            }
        }
    }


@pytest.fixture
def multi_type_dict():
    return {
        'Root': {
            '@ns': 'soapenv',
            '@attrs': {
                'xmlns:soapenv': 'http://schemas.xmlsoap.org/soap/envelope/'
            },
            'Header': '',
            'Body': {
                'tag1': [1, 2, 3],
                'tag2': {
                    'child1': ' '
                },
                'tag3': 1.0,
                'tag4': {1, 2, 3},
                'tag5': False,
                'tag6': tuple(),
                'tag7': None
            }
        }
    }


@pytest.fixture
def multi_attr_dict():
    return {
        'Envelope': {
            '@ns': 'soapenv',
            '@attrs': {
                'xmlns:soapenv': 'http://schemas.xmlsoap.org/soap/envelope/'
            },
            'Header': '',
            'Body': {
                'tag1': {
                    '@name': 'first_tag',
                    '@value': 'foo bar'
                },
                'tag2': 'some value'
            }
        }
    }
