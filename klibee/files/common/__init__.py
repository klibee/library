# diwo
# =======================================
from klibee.logger import Logger


# third-party
# =======================================
import os
import site
import importlib.util


# function
# =======================================
def make_folders(self, filepath):

    try:
        # Split the file path into directory and file name
        directory, filename = os.path.split(filepath)

        # check
        if os.path.exists(directory):
            return

        # Create directories recursively if they do not exist
        os.makedirs(directory, exist_ok=True)

        # Log
        Logger.success("{} successfully created.".format(directory))

    except Exception as exception:
        raise exception


# function
# =======================================
def exists(self, filepath):
    return os.path.isfile(filepath)


# function
# =======================================
def packages_folder(self):
    return site.getsitepackages()[0]    # /usr/local/lib/python3.8/dist-packages


# function
# =======================================
def load_class(self, className, path):

    # quick exit
    if not exists(path):
        Logger.error("Class {} does not exists. ref. {}".format(className, path))
        return None

    # load
    spec = importlib.util.spec_from_file_location(className, path)
    obj  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)

    # bye
    return obj

