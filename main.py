#!/usr/bin/env python3
from storage.storage_units import *
from items.item import *
import sys , os 
import pkg_resources


def main():
	installed_packages = pkg_resources.working_set
	installed_packages_list = sorted(["%s==%s" % (i.key, i.version)for i in installed_packages])
	print(installed_packages_list)
	print('~~~~~~~~~~~~~~~~~')
	# say_kuku()
	print('__file__ -> ',__file__)
	currentdir = os.path.dirname(os.path.realpath(__file__))
	print('currentdir -> ',currentdir)
	parentdir = os.path.dirname(currentdir)
	print('parentdir -> ',parentdir)
	# sys.path.append(parentdir)
    
    # print(get_items())
    
    # instance = StorageUnit("RS:2111","tork-g59")
    # print('instance.summarize() -> ', instance.summarize())

    # print('dir() -> ',dir())

if __name__ == "__main__":
    main()
