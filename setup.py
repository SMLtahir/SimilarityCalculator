from distutils.core import setup, Command
from codecs import open

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys
        import subprocess
        errno = subprocess.call([sys.executable, 'SimilarityCalculator/test/unit_tests_load_neighbors.py'])
        raise SystemExit(errno)

setup(
    name='SimilarityCalculator',
    packages=['SimilarityCalculator'],
    version='0.1',
    description='Python package that computes similarity between two items based on their tag relevance scores and '
                'writes to file the list of items along with their corresponding top item neighbors',
    long_description=long_description,
    author='Tahir Sousa',
    author_email='tahirsousa@gmail.com',
    url='https://github.com/SMLtahir/SimilarityCalculator',
    download_url='https://github.com/SMLtahir/SimilarityCalculator/tarball/0.1',
    maintainer='Tahir Sousa',
    maintainer_email='tahirsousa@gmail.com',
    license='GNU General Public License',
    keywords=['similarity', 'neighbor', 'neighborhood'],
    cmdclass={'test': PyTest},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: Public Domain",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering",
    ],
)
