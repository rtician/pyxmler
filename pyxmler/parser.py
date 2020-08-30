from decimal import Decimal
from xml.etree.ElementTree import Element


def parse(dict_obj, parent={}):
    for key, value in dict_obj.items():
        if isinstance(value, (int, float, Decimal, bool)):
            value = str(value)

        parent['name'] = key
        parent['value'] = value

        if isinstance(value, dict):
            if value.get('@ns'):
                parent['namespace'] = value['@ns']
                value.pop('@ns')

            if value.get('@attrs'):
                parent['attributes'] = value['@attrs']
                value.pop('@attrs')

            if value.get('@name'):
                parent['name'] = value['@name']
                value.pop('@name')

            if value.get('@value'):
                parent['value'] = value['@value']

    if parent.get('namespace'):
        parent['name'] = '{ns}:{name}'.format(ns=parent['namespace'], name=parent['name'])

    element = Element(parent['name'], parent.get('attributes', {}))

    if isinstance(parent['value'], (dict, list, tuple, set)):
        try:
            for key, value in parent['value'].items():
                element.append(parse({key: value}, parent={}))
        except AttributeError:
            for child in parent['value']:
                child_element = Element(parent['name'], parent.get('attributes', {}))
                child_element.text = str(child)
                element.append(child_element)
    else:
        element.text = parent['value']

    return element
