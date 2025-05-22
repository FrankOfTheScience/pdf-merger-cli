from setuptools import setup, find_packages

setup(
    name="pdf-merger-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyPDF2"
    ],
    entry_points={
        "console_scripts": [
            "pdfmerge=pdf_merger_cli.__main__:app",
        ],
    },
    author="Francesco Dell'Ascenza",
    description="Merge multiple PDF files into a single PDF file in a command line interface.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
