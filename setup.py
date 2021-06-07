from setuptools import find_packages, setup

with open("README.rst") as f:
    readme = f.read()

setup(
    name="guts",
    version="0.0.3",
    author="Niko Kivela",
    author_email="niko@tovrleaf.com",
    description="A toolbox for code janitors handle git operations "
    + "withing world of git",
    long_description=readme,
    url="https://github.com/tovrleaf/git-utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "click==8.0.1",
    ],
    entry_points={"console_scripts": ["guts=gutscli.guts:main"]},
    include_package_data=True,
)
