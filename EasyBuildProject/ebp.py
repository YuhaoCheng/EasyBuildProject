"""EBP
Usage:
  ebp use-default <root>
  ebp use <name>
  ebp show-default
  ebp save-default
  ebp (-h | --help)
  ebp (-v | --version)

Options:
  -h --help        Show this screen.
  -v --version     Show version.
"""

import os
import json
from collections import OrderedDict
from docopt import docopt

DEFAULT = {
    "root": "/home/user/",
    "tag": "default",
    "structure": {
        "lib":{
            "package":True,
            "contain":{
                "core":{},
                "config":{},
                "datatools":{}
                }
        },
        "data":{
            "package": False,
            "contain": {}
        },
        "experiments":{
            "package": False,
            "contain": {
                "resnet": {
                    "contain":{
                        "coco": {},
                        "voc":{}
                    }
                },
                "Hrnet":{
                    "contain":{
                        "coco":{},
                        "voc":{}
                    }
                }
            }
        }
    }
}


def build_folder(structure, root_path, package):
    # print(f'build the folder{structure}')
    if not os.path.exists(root_path):
        os.makedirs(root_path)
    if package:
        with open(os.path.join(root_path, '__init__.py'), 'w') as f:
            pass
    if not structure:
        return
    for key in structure.keys():
        temp = os.path.join(root_path, key)
        if 'package' in structure[key]:
            package = structure[key]['package']
        elif package:
            package = package
        else:
            package = False
        if 'contain' in structure[key]:
            build_folder(structure[key]['contain'], temp, package)
        else:
            build_folder(structure[key], temp, package)

def read_structure(json_path):
    with open(json_path, 'r') as f:
        structure = json.load(f)
    structure = OrderedDict(structure)
    return structure['structure'], structure['root']

def save_structure(structure):
    with open('default_structure.json', 'w') as f:
        json.dump(structure, f)
    print('Save in default_structure.json')

def use_custom(json_path):
    structure, root_path = read_structure(json_path)
    build_folder(structure, root_path, False)

def main():
    # print('000')
    # print(__doc__)
    arguments = docopt(__doc__, version="1.0.0")
    # print('123')
    # print(arguments)

    if arguments['use-default']:
        build_folder(DEFAULT['structure'], arguments['<root>'], False)
    if arguments['show-default']:
        print(DEFAULT)
    if arguments['save-default']:
        save_structure(DEFAULT)
    if arguments['use']:
        use_custom(arguments['<name>'])


if __name__ == '__main__':
    main()

