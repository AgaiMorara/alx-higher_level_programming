#!/usr/bin/python3

import dis
import importlib.util

def print_module_names(module_path):
    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = dir(module)
    names = sorted(filter(lambda name: not name.startswith("__"), names))

    for name in names:
        print(name)

if __name__ == "__main__":
    print_module_names("hidden_4.pyc")
