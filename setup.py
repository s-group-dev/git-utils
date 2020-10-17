from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='guts',
    version='0.1.0',
    description='A toolbox for code janitors handle git operations '
    + 'withing world of git',
    long_description=readme,
    author='Niko Kivelä',
    author_email='niko@tovrleaf.com',
    url='https://github.com/tovrleaf/git-utils',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'click==7.1.2'
    ],
    entry_points={
        'console_scripts': [
            'guts=guts:cli'
        ]
    }
)
