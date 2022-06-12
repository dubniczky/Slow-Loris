from setuptools import setup, find_packages
from os import getenv

version = getenv('CI_COMMIT_TAG', 'v0.1')[1:]
# Try to fall back to version file
if version == '0.1':
    try:
        with open('version.txt', 'r') as f:
            version= f.read()
    except:
        pass
else:
    with open('version.txt', 'w') as f:
            f.write(version)

description = None
with open('readme.md', 'r') as f:
    description = f.read()

setup(
    name = "sloris",
    version = version,
    author = "Richard Antal Nagy",
    author_email="nagy.richard.antal@gmail.com",
    description="Slow Loris denial of service attack",
    license = "MIT",
    keywords = [ "sloris", "dos", "security", "hacking", "denial of service" ],
    url = "https://gitlab.com/richardnagy/security/sloris",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'sloris = sloris.main:main'
        ]
    },
    python_requires='>=3.8',
    long_description_content_type='text/markdown',
    long_description=description
)