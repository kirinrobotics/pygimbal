import os
import setuptools
from pygimbal import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    LongDescription = f.read()

setuptools.setup(
    name='pygimbal',
    zip_safe=True,
    version=__version__,
    description='Python sample control gimbal via Mavlink.',
    long_description_content_type="text/markdown",
    long_description=LongDescription,
    url='https://github.com/winter2897/pygimbal',
    author='winter2897',
    install_requires=[
        'pymavlink>=2.2.20',
    ],
    author_email='haiquantran2897@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
    ],
    license='LGPLv3',
    packages=setuptools.find_packages()
)
