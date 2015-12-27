# -*- coding: utf-8 -*-
import io
import setuptools
import rpsl_via

try:
    from Cython.Build import cythonize
except ImportError:
    CYTHON = False
else:
    CYTHON = True

setuptools.setup(
    zip_safe=False,
    name='rpsl_via',
    version=rpsl_via.__version__,
    url='http://github.com/job/py-rpsl_via',
    author='Job Snijders',
    author_email='job@instituut.net',
    description='Python implementation of RPSL-VIA',
    license='BSD License',
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'rpsl_via_check = rpsl_via:main'
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
        "rpsl_via/**/*.py",
        exclude=[
            'rpsl_via/__main__.py',
            'rpsl_via/__init__.py',
            'rpsl_via/codegen/__init__.py',
            'rpsl_via/test/__main__.py',
            'rpsl_via/test/*.py'
        ]
    ) if CYTHON else [],
)
