
from setuptools import setup

VERSION = '0.0.1'
DESCRIPTION = 'S3 convert object url to S3 uri'
LONG_DESCRIPTION = 'A package that allows you to convert AWS S3 object url to S3 uri.'

# Setting up
setup(
    name="s3-uri2url",
    version=VERSION,
    author="myselfdesai (Amar Desai)",
    author_email="<amardesai.bgm@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    # long_description=long_description,
    install_requires=[],
    package_dir={'':'src'},
    keywords=['python', 's3', 'aws', 's3 uri to url', 'uri to url', 'uri2url'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)