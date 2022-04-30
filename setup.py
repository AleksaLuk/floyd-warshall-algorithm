from setuptools import setup
import os


about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "floyd_warshall", "__init__.py"), "r") as f:
    exec(f.read(), about)

with open("README.md", "r") as f:
    readme = f.read()

with open("requirements.txt") as f:
    requires = f.readlines()

with open("requirements-test.txt") as f:
    test_requirements = f.readlines()

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=["floyd_warshall"],
    #package_data={"": ["LICENSE", "NOTICE"]},
    package_dir={"requests": "requests"},
    include_package_data=True,
    python_requires=">=3.7, <4",
    install_requires=requires,
    license=about["__license__"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Local Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries",
    ],
    tests_require=test_requirements,
    project_urls={
        "Documentation": "Coming soon",
        "Source": "github",
    },
)