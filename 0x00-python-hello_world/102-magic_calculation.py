#!/usr/bin/python3
"""calculation"""
import dis

def magic_calculation(a, b):
    """does exactly same as bytecode given"""
    const = 98
    result = pow(a, b) + const
    return result
print(dis.dis(magic_calculation))
