from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='HeavyBuilder',
    version='1.0',
    description='Set of functions to predict the structure of immune receptor proteins',
    license='BSD 3-clause license',
    maintainer='Joao Gervasio',
    long_description=long_description,
    long_description_content_type='text/markdown',
    maintainer_email='joao-diniz@oist.jp',
    include_package_data=True,
    packages=find_packages(include=('HeavyBuilder', 'HeavyBuilder.*')),
    entry_points={'console_scripts': [
        'HeavyBuilder2=HeavyBuilder.HeavyBuilder2:command_line_interface',
        ]},
    install_requires=[
        'numpy',
        'scipy>=1.6',
        'einops>=0.3',
        'torch>=1.8',
        'requests'
    ],
)
