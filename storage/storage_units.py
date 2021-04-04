#!/usr/bin/env python3
import os , sys



'''
os.path.dirname('/usr/local') -> '/usr'
__file__ -> _storage_unit.py
os.path.realpath(__file__) -> /home/nadav/python_ci_cd_template/storage
os.path.dirname(os.path.dirname(os.path.realpath(__file__))) -> /home/nadav/python_ci_cd_template/
'''
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.

from items.item import *

def generate_unit_name():
    return ""

def check_generate_name_validation(name):
    return True


class StorageUnit(object):
    """Document the class as needed"""
    # Comments are allowed in classes
    # - Object initialization
    def __init__(self, name, description):
        """Object initialization"""
        # - Initialize instance properties from arguments
        self.name = name
        self.description = description
    # - Instance method
    def summarize(self):
        """Document method"""
        if self.description:
            return str('%s: %s' % (self.name, self.description))
        else:
            return self.name


def say_kuku():
    return secrate_massage()
     
    #print('kuku')

    


def false_function():
    return False

def main():
    print('Run : ', os.path.realpath(__file__),' as __main__')
    call_unit_store_object_summarize()

if __name__ == '__main__':
	main()