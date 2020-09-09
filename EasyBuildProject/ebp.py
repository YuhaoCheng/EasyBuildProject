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
import pprint
from collections import OrderedDict
from docopt import docopt

DEFAULT = {
    "root": "/home/user/",
    "tag": "default",
    "structure": {
        "lib":{
            "package":True,
            "contain":{
                "core":{
                    "package":True,
                    "contain":{}
                },
                "config":{
                    "package":True,
                    "contain":{}
                },
                "datatools":{
                    "package":True,
                    "contain":{
                        "abstract":{
                            "package":True,
                            "contain":{}
                        },
                        "augment":{
                            "package":True,
                            "contain":{}
                        },
                        "buid":{
                            "package":True,
                            "contain":{}
                        },
                        "dataclass":{
                            "package":True,
                            "contain":{}
                        },
                        "evaluate":{
                            "package":True,
                            "contain":{}
                        },
                        "sampler":{
                            "package":True,
                            "contain":{}
                        }
                    }
                },
                "networks":{
                    "package":True,
                    "contain":{
                        "abstract":{
                            "package":True,
                            "contain":{}
                        },
                        "auxiliary":{
                            "package":True,
                            "contain":{}
                        },
                        "build":{
                            "package":True,
                            "contain":{}
                        },
                        "parts":{
                            "package":True,
                            "contain":{}
                        }
                    }
                },
                "loss":{
                    "package":True,
                    "contain":{
                        "abstract":{
                            "package":True,
                            "contain":{}
                        },
                        "build":{
                            "package":True,
                            "contain":{}
                        },
                        "functions":{
                            "package":True,
                            "contain":{}
                        }
                    }
                }
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
        },
        "script":{
            "package": False,
            "contain":{}
        }
    },
    "main_file":True
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
    main_flag = structure['main_file']
    return structure['structure'], structure['root'], main_flag

def save_structure(structure):
    with open('default_structure.json', 'w') as f:
        json.dump(structure, f)
    print('Save in default_structure.json')

def use_custom(json_path):
    structure, root_path, main_flag = read_structure(json_path)
    if main_flag:
        with open(os.path.join(root_path, 'main.py'), 'w') as f:
            pass
    build_folder(structure, root_path, False)

def main():
    arguments = docopt(__doc__, version="1.0.3")

    if arguments['use-default']:
        build_folder(DEFAULT['structure'], arguments['<root>'], False)
    if arguments['show-default']:
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(DEFAULT)
    if arguments['save-default']:
        save_structure(DEFAULT)
    if arguments['use']:
        use_custom(arguments['<name>'])


if __name__ == '__main__':
    main()

