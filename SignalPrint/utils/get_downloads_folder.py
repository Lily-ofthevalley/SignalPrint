import os


def get_downloads_folder():
    if os.name == 'nt':
        downloads_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    else:
        downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    return downloads_folder