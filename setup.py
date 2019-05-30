import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="export_yaml",
    version="0.0.1",
    author="Example Author",
    author_email="d.anggrianto@gmail.com",
    description="Export environment variable from YAML file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danggrianto/export_yaml/",
    packages=setuptools.find_packages(),
    scripts=['export_yaml/export_yaml'],
    install_requires=['pyyaml'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
