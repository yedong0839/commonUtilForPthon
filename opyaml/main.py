# coding:utf8
__author__ = 'dgl'

import os
import yaml
import codecs


def add_unkonw_file(yaml_dir, yaml_file_name, dir_name):
    yaml_path = os.path.join(yaml_dir, yaml_file_name)
    if not os.path.exists(yaml_path):
        return

    with codecs.open(yaml_path, 'r', 'utf-8') as fs:
        yaml_data = yaml.load(fs)

    data = modify_yaml(yaml_dir + "/unknown/", yaml_dir + "/unknown/"+dir_name, yaml_data)

    with codecs.open(yaml_path, 'w', 'utf-8') as fs:
        yaml.dump(data, fs)


def modify_yaml(unknown, add_path, data):
    files = os.listdir(add_path)
    tmp = {}
    for fi in files:
        fi_d = os.path.join(add_path, fi)
        if os.path.isdir(fi_d):
            modify_yaml(unknown, fi_d, data)
        else:
            tmp[fi_d.replace(unknown, "").replace("\\", "/").encode('UTF-8')] = "8"

    if "unknownFiles" not in data:
        data["unknownFiles"] = tmp
    else:
        data["unknownFiles"].update(tmp)

    return data


if __name__ == '__main__':
    add_unkonw_file("C:/Users/Administrator/Desktop/apk", "apktool.yml", "com")