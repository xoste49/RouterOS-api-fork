from setuptools import find_packages
from setuptools import setup


def get_long_description():
    with open('README.md') as readme_file:
        return readme_file.read()


setup(
    name="RouterOS-api-fork",
    version='0.18.2.dev0',
    description='Python API to RouterBoard devices produced by MikroTik.',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    author='Pavel Korchagin',
    author_email='xoste49@gmail.com',
    url='https://github.com/xoste49/RouterOS-api-fork',
    packages=find_packages(),
    test_suite="tests",
    license="MIT",
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)
