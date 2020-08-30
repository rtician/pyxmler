import pytest


@pytest.fixture
def simple_dictionary():
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
