# -*- coding: utf-8 -*-
import io
import setuptools
import rpsl

try:
    from Cython.Build import cythonize
except ImportError:
    CYTHON = False
else:
    CYTHON = True

setuptools.setup(
    zip_safe=False,
    name='rpsl',
    version=rpsl.__version__,
    url='http://github.com/job/py-rpsl',
    author='Job Snijders',
    author_email='job@instituut.net',
    description='Python implementation of RPSL-VIA',
    license='BSD License',
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'rpsllint = rpsl.cli:main'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Text Processing :: General'
    ],
    extras_require={
        'future-regex': ['regex']
    },
    ext_modules=cythonize(
        "rpsl/**/*.py",
        exclude=[
            'rpsl/__main__.py',
            'rpsl/__init__.py',
            'rpsl/codegen/__init__.py',
            'rpsl/test/__main__.py',
            'rpsl/test/*.py'
        ]
    ) if CYTHON else [],
)
