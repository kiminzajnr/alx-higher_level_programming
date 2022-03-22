#!/usr/bin/python3
"safe function"


def safe_function(fct, *args):
    try:
        resul = fct(*args)
        return resul
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
