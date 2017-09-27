# XML testing playground

import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
print("what is stuff? :",type(stuff))
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text," :: is Type :",type(item.find('name').text))
    print('Id', item.find('id').text," :: is Type :",type(item.find('id').text))
    print('Attribute', item.get("x")," :: is Type :",type(item.get("x")))
