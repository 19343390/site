
import os
import glob
import subprocess

_dir_path = os.path.dirname(os.path.realpath(__file__))


def get_notebooks():
    notebooks = [f for f in glob.glob(os.path.join(_dir_path, "**", "*.ipynb",), recursive=True)]
    if len(notebooks) == 0:
        raise ValueError("Could not find any notebooks.")
    return notebooks


def convert_notebooks_to_rst(notebook_list):
    for nb in notebook_list:
        cmd = ["jupyter", "nbconvert", "--ClearOutputPreprocessor.enabled=True",
               nb, "--to", "rst"]
        print(cmd)
        subprocess.run(cmd)


def convert_notebooks_to_jupyter_sphinx_rst(notebook_list):
    for nb in notebook_list:
        cmd = ["jupyter", "nbconvert", "--ClearOutputPreprocessor.enabled=True",
               nb, "--to", "rst"]
        print(cmd)
        subprocess.run(cmd)

        # Read rst file and convert (allow Exceptions)
        with open(nb.replace('.ipynb', '.rst'), 'r') as rst:
            lines = rst.readlines()
            converted_lines = []
            for line in lines:
                if line.startswith(".. code:: ipython3"):
                    # Convert to jupyter-execute
                    line = line.replace(".. code:: ipython3",
                                        ".. jupyter-execute::\n    :raises:\n")

                converted_lines.append(line)

        # Write
        with open(nb.replace('.ipynb', '.rst'), 'w') as rst:
            for line in converted_lines:
                rst.write(line)

notebooks = get_notebooks()
convert_notebooks_to_jupyter_sphinx_rst(notebooks)

