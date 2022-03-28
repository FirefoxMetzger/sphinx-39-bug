import sys

class Foo:
    """ Summary of class Foo
    
    Here comes extensive documentation.
    
    """


class Bar:
    """ Summary of class Bar

    even more extensive documentation.
    
    """

class LazyImporter:
    __name__ = __name__

    def __getattr__(self, name):
        """Lazy-Import Awesome Things

        Note: this doesn't actually lazy import here, because everything is in
        the same file for demo purposes. In the real world, this calls
        importlib.import_module to make the magic happen.

        """

        if name == "Foo":
            return Foo
        elif name == "Bar":
            return Bar
        else:
            raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

foo = LazyImporter()
foo.__doc__ = """ The demp_project package

    The demp_project consists of the following classes:

    .. autosummary::
        :toctree: _autosummary

        demp_project.Foo
        demp_project.Bar

    """

sys.modules[__name__] = foo
