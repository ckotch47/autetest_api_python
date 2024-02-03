import shutil


def create_module(path: str):
    copy_example(path)

def copy_example(path: str):
    shutil.copytree('src/common/example', path)
