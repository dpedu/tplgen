__version__ = "0.0.1"

import os
import yaml
import json
import argparse
import importlib
import pdb
from pprint import pprint


def import_file(fpath):
    spec = importlib.util.spec_from_file_location(os.path.dirname(fpath), os.path.basename(fpath))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def plain_key(s):
    return s.split(".")[0]


def load_data(datadir):
    data = {}
    for fname in os.listdir(datadir):
        if not any([fname.endswith(ext) for ext in (".json", ".yaml", ".yml")]):
            continue
        with open(os.path.join(datadir, fname)) as f:
            data[plain_key(fname)] = yaml.unsafe_load(f)
    return data


def render(datadir, templatedir, outdir):
    data = load_data(datadir)

    # print(json.dumps(data, indent=4))
    print(yaml.dump(data))

    renderer = import_file("nagios.py")

    # call renderer, which yields (ƒpath, fcontents, ) tuples
    for fpath, fcontents in renderer.render(data):
        print(fpath, fcontents)


def main():
    parser = argparse.ArgumentParser(description="Backupdb Agent depends on config: /etc/datadb.ini")

    p_mode = parser.add_subparsers(dest='mode', help='modes (only "rsync")')

    p_generate = p_mode.add_parser('gen', help='generate templates')
    p_generate.add_argument('-d', '--data', required=True, help='path to dir containing data json files')
    p_generate.add_argument('-t', '--templates', required=True, help='template files dir')
    p_generate.add_argument('-o', '--out', required=True, help='output dir')

    args = parser.parse_args()

    render(args.data, args.templates, args.out)


if __name__ == '__main__':
    main()
