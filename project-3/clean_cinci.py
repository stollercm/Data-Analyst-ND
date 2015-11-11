street_mapping = {"Ave": "Avenue",
           "Avene": "Avenue",
           "Avnue": "Avenue",
           "avenue": "Avenue",
           "State" : "Avenue",
           "Dr" : "Drive",
           "dr." : "Drive",
           "meadow" : "Meadow Drive",
           "Rd.": "Road",
           "Rd": "Road",
           "St": "Street",
           "street" : "Street",
           "ter" : "Terrace"}

def update_name(name, mapping):
    for key in mapping:
        if name.endswith(key):
            type_start = name.find(key)
            name = name[:type_start] + mapping[key]
    return name

state_mapping = {'Oh': "OH", 
                 'oh': "OH", 
                 'OHIO': "OH", 
                 'Ohop': "OH", 
                 'ohio': "OH", 
                 'Ohio': "OH", 
                 'OH - Ohio': "OH", 
                 'Kentucky': "KY", 
                 'ky': "KY"}

def update_state(name, mapping):
    # change state name to 2-letter code
    for key in mapping:
        if name == key:
            name = mapping[key]
    return name

city_mapping = { 'CIncinnati': "Cincinnati", 
                 'cincinnati': "Cincinnati", 
                 'Cincinnati, OH': "Cincinnati", 
                 'Cincinnati, Ohio': "Cincinnati", 
                 'Cincinnati, Oh': "Cincinnati", 
                 'Cincinnati, oh': "Cincinnati", 
                 'Cincinnati; Symmes': "Symmes Township",
                 'Cincinnati;Blue Ash': "Blue Ash", 
                 'Cincinnati;Symmes': "Montgomery",
                 'Newport, Kentucky': "Newport",
                 'forest Park': "Forest Park",
                 'fort thomas': "Fort Thomas" }

def update_city(name, mapping):
    # fix inconsistent or incorrect city identifiers
    for key in mapping:
        if name == key:
            name = mapping[key]
    return name

def update_postcode(code):
    # strip suffix of postal code if present
    if len(code) > 5:
        return code[:5]
    else:
        return code

import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

    
def has_addr(element):
    for child in element:
        if child.tag == "tag":
            k = child.attrib["k"]
            if k.find("addr") != -1:
                return True
    return False


def shape_element(element):
    node = {}
    if element.tag == "node" or element.tag == "way" :
        attributes = element.attrib
        node["type"] = element.tag
        node["created"] = {}
        
        if "lat" in attributes and "lon" in attributes:
            node["pos"] = [ float(attributes["lat"]), float(attributes["lon"]) ]
        if has_addr(element):
            node["address"] = {}
        
        for key in attributes:
            if key in CREATED:
                node["created"][key] = attributes[key]
            elif key != "lat" and key != "lon":
                node[key] = attributes[key]
        
        if element.findall("tag"):
            for child in element.iter("tag"):
                k = child.attrib["k"]
                v = child.attrib["v"]
                
                if k.find("addr") != -1:
                    new_key = k[5:]
                    if new_key.find(":") != -1:
                        pass
                    elif new_key == "street":
                        v = update_name(v, street_mapping)
                    elif new_key == "state":
                        v = update_state(v, state_mapping) 
                    elif new_key == "postcode":
                        v = update_postcode(v)
                    elif new_key == "city":
                        comma = v.find(",")
                        if comma != -1:
                            state = v[comma + 2:]
                            state = update_state(state, state_mapping)
                            node["address"]["state"] = state
                        v = update_city(v, city_mapping)
                    node["address"][new_key] = v
                elif problemchars.search(k):
                    pass
                else:
                    node[k] = v
        
        if element.tag == "way":
            node["node_refs"] = []
            if element.findall("nd"):
                for child in element.iter("nd"):
                    value = child.attrib["ref"]
                    node["node_refs"].append(value)
                    
        return node
    else:
        return None



def process_map(file_in, pretty = False):
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        # get an iterable & turn it into an iterator
        context = ET.iterparse(file_in, events=("start", "end"))
        context = iter(context)
        # get the root element
        event, root = context.next()

        for event, element in context:
            el = shape_element(element)
            if event == "end" and el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
                root.clear()
        
    return data

# NOTE: if you are running this code on your computer, with a larger dataset, 
# call the process_map procedure with pretty=False. The pretty=True option adds 
# additional spaces to the output, making it significantly larger.
import time

localtime = time.asctime( time.localtime(time.time()) )
print "Start at ", localtime

data = process_map('cincinnati_ohio.osm', pretty=False)

localtime = time.asctime( time.localtime(time.time()) )
print "Finish at ", localtime
