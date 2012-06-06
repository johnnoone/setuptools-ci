from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1'

install_requires = [
    'nose', 'nosexcover', 'setuptools-clonedigger', 'setuptools-flakes',
    'setuptools-lint', 'setuptools-sloccount',
]


setup(name='setuptools-ci',
    version=version,
    description="Adds everything for continuous integration",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        "Topic :: Documentation",
        "Framework :: Setuptools Plugin",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: BSD License',
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='continuous-integration setuptools command',
    author='Xavier Barbosa',
    author_email='',
    url='https://github.com/johnnoone/setuptools-ci',
    license='BSD',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        "distutils.commands": [
            "ci = setuptools_continuousintegration.setuptools_command:ContinuousIntegrationCommand",
        ]
    }
)
