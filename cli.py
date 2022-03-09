import os
import sys
import functools
import operator
import json
import logging
import itertools

try:
    import jmespath
except ModuleNotFoundError as error:
    logging.warning(error)

class fs:
    @staticmethod
    def read(path):
        content = None
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content

    @staticmethod
    def read_json(path):
        return json.loads(__class__.read(path))
