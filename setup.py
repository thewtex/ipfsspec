import setuptools
import versioneer


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ipfsspec",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Tobias Kölling",
    author_email="tobias.koelling@physik.uni-muenchen.de",
    description="readonly implementation of fsspec for IPFS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fsspec/ipfsspec",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    install_requires=[
        "fsspec>=0.9.0",
        "requests",
        "protobuf>=3.15.8",
        "py-cid",
    ],
    entry_points={
        'fsspec.specs': [
            'ipfs=ipfsspec.IPFSFileSystem',
        ],
    },
)
