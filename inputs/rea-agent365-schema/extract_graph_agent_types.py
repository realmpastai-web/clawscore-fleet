#!/usr/bin/env python3
# Extract every EntityType/ComplexType/EnumType whose name contains "agent" from a Graph CSDL file, with properties and descriptions.
# Usage: python3 extract_graph_agent_types.py <csdl.xml> <v1.0|beta> > out.json
import sys, re, json, xml.etree.ElementTree as ET
f, tag = sys.argv[1], sys.argv[2]
NS='{http://docs.oasis-open.org/odata/ns/edm}'
root=ET.parse(f).getroot()
out=[]
for schema in root.iter(NS+'Schema'):
    ns=schema.get('Namespace')
    for kind in ('EntityType','ComplexType','EnumType'):
        for t in schema.findall(NS+kind):
            n=t.get('Name')
            if not re.search(r'agent', n, re.I): continue
            props=[]
            for p in list(t.findall(NS+'Property'))+list(t.findall(NS+'NavigationProperty'))+list(t.findall(NS+'Member')):
                d=None
                for a in p.findall(NS+'Annotation'):
                    if a.get('Term','').endswith('Description'): d=a.get('String')
                props.append({'name':p.get('Name'),'type':p.get('Type') or p.get('Value'),'desc':d})
            td=None
            for a in t.findall(NS+'Annotation'):
                if a.get('Term','').endswith('Description'): td=a.get('String')
            out.append({'metadata':tag,'ns':ns,'kind':kind,'name':n,'base':t.get('BaseType'),'desc':td,'props':props})
json.dump(out,sys.stdout,indent=1)
