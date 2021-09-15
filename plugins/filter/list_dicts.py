#!/usr/bin/python
from ansible.utils.vars import merge_hash
from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.plugins.filter.core import subelements, combine

__metaclass__ = type

def subelements_combined(obj, subelems):
    try:
        aux = subelements(obj, subelems)
        aux2 = []
        for i in range(len(aux)):
            aux2.append(combine(aux[i][0], aux[i][1]))
        return aux2

    except Exception as e:
        raise AnsibleFilterError('Subelements_combined filter plugin error: %s' % (to_native(e)) )



def zip_merge(my_list, spells):
    try:
        aux = my_list.copy()

        for i in range(len(aux)):
            aux[i] = merge_hash(my_list[i], spells[i])

        return aux

    except Exception as e:
        raise AnsibleFilterError('Zip merge filter plugin error: %s' % (to_native(e)) )

class FilterModule(object):

    def filters(self):
       return {
            'zip_merge' : zip_merge,
            'subelements_combined' : subelements_combined,
       }

