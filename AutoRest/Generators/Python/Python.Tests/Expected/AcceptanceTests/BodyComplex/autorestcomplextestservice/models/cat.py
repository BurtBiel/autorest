# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .pet import Pet


class Cat(Pet):
    """Cat

    :param int id:
    :param str name:
    :param str color:
    :param list hates:
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'color': {'key': 'color', 'type': 'str'},
        'hates': {'key': 'hates', 'type': '[Dog]'},
    }

    def __init__(self, id=None, name=None, color=None, hates=None, **kwargs):
        super(Cat, self).__init__(id=id, name=name, **kwargs)
        self.color = color
        self.hates = hates
