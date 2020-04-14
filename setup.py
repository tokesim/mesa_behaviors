import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("mesa_behaviors/__init__.py", "r") as file:
    regex_version = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'
    version = re.search(regex_version, file.read(), re.MULTILINE).group(1)

#with open("README.rst", "rb") as file:
#    readme = file.read().decode("utf-8")

setup(
    name="loguru",
    version=version,
    packages=["loguru"],
    package_data={"loguru": ["__init__.pyi", "py.typed"]},
    description="Python logging made (stupidly) simple",
    author="Zane",
    author_email="zcstarr@gmail.com",
    url="https://github.com/tokesim/mesa_behaviors",
    download_url="https://github.com/tokesim/mesa_behaviors/archive/{}.tar.gz".format(version),
    project_urls={
        "Changelog": "https://github.com/tokesim/mesa_behaviors/blob/master/CHANGELOG.rst",
        "Documentation": "https://mesa_behaviors.readthedocs.io/en/stable/index.html",
    },
    keywords=["simulation", "mixed-games", "mesa", "agent-based modeling"],
    license="MIT license",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Simulation :: Agent-Based Modeling",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    install_requires=[
        "Mesa>=0.8.6",
        "bitarray>=1.2.1",
        "mypy>=0.770",
        "mypy-extensions>=0.4.3"
        "typing-extensions>=3.7.4.2"
    ],
    extras_require={
        "dev": [
            "black>=19.10b0",
            "codecov>=2.0.22",
            "flake8>=3.7.9",
            "isort>=4.3.21",
            "tox>=3.14.6",
            "pytest>=5.4.1",
            "docformatter>=1.3.1",
            "pytest-cov>=2.8.1"
        ]
    },
    python_requires=">=3.7",
)