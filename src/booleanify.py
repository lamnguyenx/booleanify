#!/usr/bin/env python3

# Copyright 2020-2024 (author: lamnguyenx)


# technical
import typing as tp



### CONSTS
STR_TO_BOOL = {
    1       : True,
    '1'     : True,
    'on'    : True,
    't'     : True,
    'true'  : True,
    'y'     : True,
    'yes'   : True,
    0       : False,
    'off'   : False,
    'f'     : False,
    'false' : False,
    'n'     : False,
    'no'    : False,
}



### FUNCTIONS
def booleanify(value: tp.Union[int, str, bytes, bool]) -> bool:

    '''
    sauce : https://docs.pydantic.dev/2.0/usage/types/booleans/

    A standard bool field will raise a ValidationError if the value is not one of the following:

    -   A valid boolean (i.e. True or False),
    -   The integers 0 or 1,
    -   a str which when converted to lower case is one of '0', 'off', 'f', 'false', 'n', 'no', '1', 'on', 't', 'true', 'y', 'yes'
    -   a bytes which is valid per the previous rule when decoded to str
    '''

    if isinstance(value, bool):
        return value

    elif isinstance(value, str):
        try:
            return STR_TO_BOOL[value.lower()]
        except KeyError:
            raise ValueError(f'The input value cant be converted to boolean (value="{value}")')

    elif isinstance(value, int):
        try:
            return STR_TO_BOOL[value]
        except KeyError:
            raise ValueError(f'The input value cant be converted to boolean (value="{value}")')

    elif isinstance(value, bytes):
        return booleanify(value.decode())
