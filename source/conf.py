project = "Introduction to Python for Geographic Data Analysis"
copyright = "2020, Henrikki Tenkanen, Vuokko Heikinheimo & Dave Whipp"
author = "Henrikki Tenkanen, Vuokko Heikinheimo & Dave Whipp"

# The full version, including alpha/beta/rc tags
version = release = "0.5.2"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]


def jupyter_book_build_handler(app, docname, source):
    print('This would execute the Jupyter-book build command ...')


def setup(app):
    app.connect('jupyter-book-build', jupyter_book_build_handler)