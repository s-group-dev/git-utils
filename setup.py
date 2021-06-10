from setuptools import find_packages, setup

with open("README.rst") as f:
    readme = f.read()

with open("src/version.yml") as f:
    __version__ = f.read().split()[1]

setup(
    name="gtsh",
    version=__version__,
    author="Niko Kivela",
    author_email="niko@tovrleaf.com",
    description="A toolbox for code janitors handle git operations "
    + "withing world of git",
    long_description=readme,
    url="https://github.com/tovrleaf/git-utils",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Version Control :: Git",
    ],
    keywords="git development source",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "click==8.0.1",
    ],
    entry_points={"console_scripts": ["gtsh=gtshcli.gtsh:main"]},
    include_package_data=True,
)
