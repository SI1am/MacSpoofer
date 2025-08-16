from setuptools import setup, find_packages

setup(
    name='CrackMac',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'crackmac = crackmac.crackmac:main',
        ],
    },
    author='Anonymous',
    description='CrackMac - A CLI MAC address spoofing tool for Linux systems.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.6',
)
