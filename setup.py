from distutils.core import setup

setup(
    name='SimilarityCalculator',
    packages=['SimilarityCalculator'],
    version='0.1',
    description='Python package that computes similarity between two items based on their tag relevance scores and '
                'writes to file the list of items along with their corresponding top item neighbors',
    author='Tahir Sousa',
    author_email='tahirsousa@gmail.com',
    url='https://github.com/SMLtahir/SimilarityCalculator',
    download_url='https://github.com/SMLtahir/SimilarityCalculator/tarball/0.1',
    keywords=['similarity', 'neighbor', 'neighborhood'],
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
