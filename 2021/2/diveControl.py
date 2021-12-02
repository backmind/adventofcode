# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:20:02 2021

@author: backm
"""

import pandas as pd

def instructionInterpreter(row):
    """


    Parameters
    ----------
    row : pandas dataframe row
        Row with composed instruction information and value.

    Returns
    -------
    Value in complex form: forward imaginary part, up-down real part.

    """

    instruction = row.instruction
    value = row.value

    if instruction=="forward":
        value = complex(0, value)
    elif instruction=="down":
        value = complex(value, 0)
    else:
        value = complex(-value, 0)
    return value



dc = pd.read_csv("input.txt", delimiter=" ", header=None)
dc.rename(columns={0:"instruction",1:"value"}, inplace=True)

dc["complex"] = dc.apply(instructionInterpreter, axis=1)
answer1= dc["complex"].sum().real*dc["complex"].sum().imag



dc["aim"] = dc.complex.cumsum()
dc["depth"] = dc["aim"].apply(lambda x: x.real)*dc["complex"].apply(lambda x: x.imag)
answer2 = dc["depth"].sum()*dc["complex"].sum().imag
