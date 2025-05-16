#!/usr/bin/python3

def array_of_names(persons):
    ret = []
    persons.items()
    for i in persons:
        ret.append(i.capitalize())
    return ret

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))