#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, json, json, os, subprocess

def go_out(index):
    if (index == 1):
        print ("Error: Can't find the configuration file, Please check your ~/.private.json")
    else:
        print ("Usage: ")

    sys.exit(0)


if __name__ == "__main__":
    command = ["rsync", "-aPz"];

    if (len(sys.argv) < 2):
        go_out(0);

    if (len(sys.argv) == 4):
        if (sys.argv[3] == '-d'):
            command.append("--delete")
        else:
            go_out(0)

    json_file = os.path.expanduser("~/.private.json")
    with open(os.path.expanduser("~/.private.json")) as tmp_file:
        tmp = json.load(tmp_file)["Applications"]["rsync"]
        if sys.argv[1] in tmp:
            config = tmp[sys.argv[1]]
        else:
            go_out(1)

    abs_of_local = os.path.abspath(os.path.expanduser(config['local']))
    local_dir_name = os.path.basename(abs_of_local)
    local_dir_father = os.path.abspath(os.path.join(abs_of_local, os.pardir))
    dst = config['name'] + '@' + config['server'] + ':'

    if (len(sys.argv) > 2 and sys.argv[2] == 'in'):
        command.append(dst + config['rmote'] + '/' + local_dir_name)
        command.append(local_dir_father)
        subprocess.call(command)
    else:
        command.append(abs_of_local)
        command.append(dst + config['rmote'])
        subprocess.call(command)

