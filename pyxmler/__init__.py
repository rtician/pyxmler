from xml.dom import minidom
from xml.etree.ElementTree import tostring

from pyxmler.parser import parse


def dict2xml(d, encoding="utf-8", pretty=False, indent=4):
    """
    Converts a python dictionary into a valid XML string

    Args:
        d: the dictionary to be converted.
        encoding: specifies the encoding to be included in the encoding
        segment. If set to False no encoding segment will be displayed.
        pretty: format the xml string to a readable style.
        indent: the size of spaces that will be added before the line start.

    Returns:
        string: A XML formatted string representing the dictionary.
    """

    xml_string = tostring(parse(d), encoding=encoding)

    if pretty:
        xml_pretty_string = minidom.parseString(xml_string)
        xml = xml_pretty_string.toprettyxml(encoding=encoding, indent=''.ljust(indent)).decode(encoding)
    else:
        xml = xml_string.decode(encoding)

    return xml

