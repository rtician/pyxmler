from pyxmler import dict2xml


def test_dict2xml():
    expected_xml = ('<soapenv:RootTag xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">'
                    '<childTag someAttribute="colors are nice"><grandchild>This is a text tag</grandchild>'
                    '</childTag></soapenv:RootTag>')
    d = {
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

    xml = dict2xml(d)
    assert expected_xml == xml


def test_dict2xml_pretty_indent():
    expected_xml = '<?xml version="1.0" encoding="utf-8"?>\n'
    expected_xml += '<soapenv:RootTag xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">\n'
    expected_xml += '    <childTag someAttribute="colors are nice">\n'
    expected_xml += '        <grandchild>This is a text tag</grandchild>\n'
    expected_xml += '    </childTag>\n'
    expected_xml += '</soapenv:RootTag>\n'

    d = {
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

    xml = dict2xml(d, pretty=True, indent=4)
    assert expected_xml == xml
