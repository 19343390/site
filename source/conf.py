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


def get_parent_dir():
    os.path.dirname(os.path.abspath(os.path.dirname(__file__)))


subprocess.run(["jb", "build", "source/"], shell=True, cwd=get_parent_dir())
