from pyxmler import dict2xml


def test_dict2xml(simple_dict):
    expected_xml = ('<soapenv:RootTag xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">'
                    '<childTag someAttribute="colors are nice"><grandchild>This is a text tag</grandchild>'
                    '</childTag></soapenv:RootTag>')

    xml = dict2xml(simple_dict)
    assert expected_xml == xml


def test_multi_types_conversion(multi_type_dict):
    expected_xml = ('<soapenv:Root xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">'
                    '<Header /><Body><tag1><tag1>1</tag1><tag1>2</tag1><tag1>3</tag1></tag1>'
                    '<tag2><child1> </child1></tag2><tag3>1.0</tag3><tag4><tag4>1</tag4><tag4>2</tag4>'
                    '<tag4>3</tag4></tag4><tag5>False</tag5><tag6 /><tag7 /></Body></soapenv:Root>')

    xml = dict2xml(multi_type_dict)
    assert expected_xml == xml


def test_dict2xml_pretty_indent(simple_dict):
    expected_xml = '<?xml version="1.0" encoding="utf-8"?>\n'
    expected_xml += '<soapenv:RootTag xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">\n'
    expected_xml += '    <childTag someAttribute="colors are nice">\n'
    expected_xml += '        <grandchild>This is a text tag</grandchild>\n'
    expected_xml += '    </childTag>\n'
    expected_xml += '</soapenv:RootTag>\n'

    xml = dict2xml(simple_dict, pretty=True, indent=4)
    assert expected_xml == xml


def test_xml_attributes(multi_attr_dict):
    expected_xml = ('<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><Header />'
                    '<Body><first_tag>foo bar</first_tag><tag2>some value</tag2></Body></soapenv:Envelope>')

    xml = dict2xml(multi_attr_dict)
    assert expected_xml == xml
