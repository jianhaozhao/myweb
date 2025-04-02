#!/usr/bin/env python
import os
import sys


class Test:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"这是我的名字：{self.name}"

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myweb.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
