from decimal import Decimal
from xml.etree.ElementTree import Element


def parse(dict_obj, parent={}):
    for key, value in dict_obj.items():
        if isinstance(value, (int, float, Decimal, bool)):
            value = str(value)

        if '@ns' in value:
            parent['namespace'] = value['@ns']
            value.pop('@ns')

        if '@attrs' in value:
            parent['attributes'] = value['@attrs']
            value.pop('@attrs')

        if '@name' in value:
            parent['name'] = value['@name']
            value.pop('@name')
        else:
            parent['name'] = key

        if '@value' in value:
            parent['value'] = value['@value']
        else:
            parent['value'] = value

    if 'namespace' in parent:
        parent['name'] = '%s:%s' % (parent['namespace'], parent['name'])

    if 'attributes' in parent:
        element = Element(parent['name'], parent['attributes'])
    else:
        element = Element(parent['name'])

    if isinstance(parent['value'], dict):
        for key, value in parent['value'].items():
            element.append(parse({key: value}, parent={}))

    elif isinstance(parent['value'], (list, set, tuple)):
        for child in parent['value']:
            element.append(parse(child, parent={}))

    else:
        element.text = str(parent['value'])

    return element
