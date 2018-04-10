TODO: Reflect on what you learned this week and what is still unclear
'''I have learnt
r = request.get(url)
response.jason=json.loads(r.text)
JSON FORMAT https://www.youtube.com/watch?v=pTT7HMqDnJw
1. Json: true and false
    python none = null
    contain all possible data types: keys, strings, numbers, booleans, null, or other Json object.
2. XML
    <>
how to import json into python?
import json
dir(json) is to know the commend of the json file
load and dump methods
json.load(f): allows to load json data from file
json.loads(s): allows to load json data from a string
json.dump(j,f): allows to write json object to file (or file-like object)
json.dumps(j): allows to output json object as string

example:
    json_file = open(F:/data/movie_1.txt", "r")
    name = json.load(json_file)
    json_file.close()
    dictionary
    look through the json file by using Dictionary
    name["lol"]
''' Brackets [] are used to define mutable data type as lists or list comprehensions (list)
Brackets can be used for indexing and lookup of list elements
can be used to access the individual characters of a string or to making string slicing

{} are used in python to define a set or dictionary. set.
dictionary name[key name]
() can e used to create immutable sequence data type tuple.
() can also be used to specify the order of operations in expressions. (1+2)**2
() can be used define the parameters of a functoin definition and a function call'''

TODO: Reflect on what you learned this week and what is still unclear.
