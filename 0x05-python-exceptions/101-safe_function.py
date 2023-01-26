#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        function = fct(*args)
        return function
    except Exception as i:
        import sys
        sys.stderr.write("Exception: {}\n".format(i))
        return None
