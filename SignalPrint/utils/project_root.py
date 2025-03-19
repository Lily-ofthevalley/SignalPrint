import os

def get_project_root():
    """Returns the absolute path to the project's root directory."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))