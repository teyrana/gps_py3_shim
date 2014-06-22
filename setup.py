from setuptools import setup, find_packages

setup(
    name = "gpsdpy3",
    version = "0.3.2",
    packages=find_packages(),
    author = "Daniel Williams",
    author_email = "equipoise@gmail.com",
    description = ("gpsd client library (python3 port)"),
    license = "BSD License (3-Clause)",
    keywords = 'gps ais gpsd python3',
    url = "https://github.com/teyrana/gpsd-python3",
    install_requires=[],

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Other Audience',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: BSD License',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Operating System :: POSIX',
                 'Operating System :: POSIX :: Linux',
                 # should work on any python3 version, but has only been tested on 3.5
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.5',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Scientific/Engineering :: GIS'
    ],
)