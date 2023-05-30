#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        i = fct(*args)
        return i
    except Exception as e:
        sys.stderr.write("Exception: {}\n" .format(e))
        return None
