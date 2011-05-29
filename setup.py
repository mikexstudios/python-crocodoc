from setuptools import setup, find_packages

setup(
    name = 'python-crocodoc',
    packages = find_packages(),
    version = '0.9.0',
    description = "Simple wrapper around Crocodoc's API",
    author = 'Michael Huynh',
    author_email = 'mike@mikexstudios.com',
    url = 'http://github.com/mikexstudios/python-crocodoc',
    install_requires = ['bolacha==dev'], #force checkout of my github fork
    dependency_links = ['http://github.com/mikexstudios/bolacha/tarball/master#egg=bolacha-dev'], 
    classifiers = [
        'Programming Language :: Python', 
        'License :: OSI Approved :: BSD License',
    ]
)

