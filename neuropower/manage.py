#!/usr/bin/env python
import os
import sys

#root_path = os.path.abspath(os.path.split(__file__)[0])
#sys.path.insert(0, os.path.join(root_path, 'neuropowertools'))
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "neuropowertools.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
