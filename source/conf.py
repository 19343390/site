project = "Introduction to Python for Geographic Data Analysis"
copyright = "2020, Henrikki Tenkanen, Vuokko Heikinheimo & Dave Whipp"
author = "Henrikki Tenkanen, Vuokko Heikinheimo & Dave Whipp"

# The full version, including alpha/beta/rc tags
version = release = "0.5.2"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

master_doc = "index"

# Build Jupyter-book
import subprocess
import os
import shutil


def current_dir():
    return os.path.abspath(os.path.dirname(__file__))


def get_parent_dir():
    return os.path.dirname(current_dir())

# Build the Jupyter-book pages
# ----------------------------

root_directory = get_parent_dir()
docs_dir_name = os.path.basename(current_dir())

subprocess.run(["jb", "build", f"{docs_dir_name}/"], shell=True, cwd=root_directory)

# Replace Sphinx build with Jupyterbook
shutil.rmtree(os.path.join(root_directory, "_build"))
shutil.copytree(os.path.join(current_dir(), "_build"), root_directory)