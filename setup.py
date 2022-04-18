import setuptools
from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='cw_download_chess_com_games',
    version='0.1',
    url='',
    license='http://creativecommons.org/licenses/by-nc-nd/4.0',
    author='Cezary K. Wagner',
    author_email='',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: End Users/Desktop',
        'License :: Free for non-commercial use',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Topic :: Games/Entertainment',
        'Topic :: Games/Entertainment :: Board Games',
        'Topic :: Education',
    ],
    description='Download all your chess games from chess.com.',
    long_description=long_description,
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'cw_download_chess_com_games = cw_download_chess_com_games:main'
        ]
    }
)
