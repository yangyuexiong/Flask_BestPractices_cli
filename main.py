# -*- coding: utf-8 -*-
# @Time    : 2021/12/9 10:05 上午
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : main.py
# @Software: PyCharm

import os
import shutil

from mako.template import Template
from mako.lookup import TemplateLookup

print(Template("hello ${data}!").render(data="world"))


def gen_dir(path, dir_name, file_list, child):
    """1"""
    result_dir = {
        "path": path,
        "dir_name": dir_name,
        "file_list": file_list,
        "child": child
    }
    return result_dir


def gen_file(p):
    with open(p, 'w') as f:
        f.close()


def gen_project(project_tree=None, parent_dir=None):
    """

    :param project_tree:
    :param parent_dir:
    :return:
    """
    for t in project_tree:
        if isinstance(t, dict):
            print(t)
            current_path = parent_dir + t.get('path') if parent_dir else t.get('path')
            current_file_list = t.get('file_list')
            current_child = t.get('child')
            if os.path.exists(current_path):
                shutil.rmtree(current_path)

            os.mkdir(current_path)
            if current_file_list:
                [gen_file(p=current_path + f) for f in current_file_list]

            if current_child:
                gen_project(project_tree=current_child, parent_dir=current_path)

        if isinstance(t, list):
            [gen_file(p=f) for f in t]


def project_init():
    pass_list = ["README.md", ".gitignore", "main.py", ".idea"]
    for d in os.listdir(base_path):
        current_path = base_path + "/" + d
        if d in pass_list:
            print(d)
        else:
            if os.path.isdir(current_path):
                shutil.rmtree(current_path)
            if os.path.isfile(current_path):
                os.remove(current_path)


base_path = os.getcwd()

file_1_list = [
    base_path + "/all_reference.py",
    base_path + "/ApplicationExample.py",
    base_path + "/run.py"
]

demo_api_dir = gen_dir(path='/demo_api', dir_name='demo_api', file_list=["/__init__.py", "/demo_api.py"], child=[])
api_dir = gen_dir(path='/api', dir_name='api', file_list=["/__init__.py"], child=[demo_api_dir])
models_dir = gen_dir(path='/models', dir_name='api', file_list=["/__init__.py"], child=[])

interceptors_dir = gen_dir(
    path='/interceptors',
    dir_name='interceptors',
    file_list=["/__init__.py", "/ApiHook.py", "/AppHook.py", "/CrmHook.py"],
    child=[]
)

libs_dir = gen_dir(
    path='/libs',
    dir_name='libs',
    file_list=["/__init__.py"],
    child=[]
)

app_child = [api_dir, models_dir]
common_child = [interceptors_dir, libs_dir]
config_child = []
docs_child = []
ExtendRegister_child = []

project = [
    file_1_list,
    gen_dir(path=base_path + '/app', dir_name='app', file_list=["/__init__.py"], child=app_child),
    gen_dir(path=base_path + '/common', dir_name='common', file_list=["/__init__.py"], child=common_child),
    gen_dir(path=base_path + '/config',
            dir_name='config',
            file_list=["/__init__.py", "/config.py", "/dev.ini", "/pro.ini"],
            child=config_child),
    gen_dir(path=base_path + '/docs', dir_name='docs', file_list=[], child=docs_child),
    gen_dir(path=base_path + '/ExtendRegister', dir_name='ExtendRegister', file_list=["/__init__.py"],
            child=ExtendRegister_child),
]

if __name__ == '__main__':
    project_init()
    gen_project(project_tree=project)

