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
    return '***Another, quite new and good massage place in Kamala, \n along the short cut road of the first traffic light to the beach road. Khun Fo, \n who was running Andaman massage before in Surin moved to Kamala recently. Excellent service and friendly staff'

def get_items():
    return [x for x in range(1,11)]



def main():
    print('Run : ', os.path.realpath(__file__),' as __main__')

if __name__ == '__main__':
	main()