import os


def repository_root():
    """The root directory of the repository as absolute path. This function
    relies on the correct setting of the environment variable `REPOSITORY_ROOT`
    which is set during the setup of the utils module.

    Returns
    -------
    root : str
        String containing the root directory
    """
    environ = os.path.dirname(os.path.abspath(__file__))
    root = os.path.abspath(
        os.path.join(environ, os.pardir, os.pardir))
    return root


def data_path():
    """The data folder
    """
    return os.path.join(repository_root(), 'data')
