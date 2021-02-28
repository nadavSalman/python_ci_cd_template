#!/usr/bin/env python3
import os , sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))#Add to path parent dir.
from storage.storage_units import *



def call_unit_store_object_summarize():
	# - Create an instance of the class StorageUnit that define in storage_unit.py module .
    instance = StorageUnit('stack-unit:437', 'AIJR')
    # print('dir(instance) -> ',dir(instance))
    print(instance.summarize())   

print('Someone imprted me ...')

def secrate_massage():
    print('Bla bla lal lal 123')
    return 'Bla bla lal lal 123'

def get_items():
    return [x for x in range(1,11)]



def main():
    print('Run : ', os.path.realpath(__file__),' as __main__')

if __name__ == '__main__':
	main()