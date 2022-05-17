from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="gif",
    version="4.0",
    description="The matplotlib Animation Extension",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Multimedia :: Graphics",
    ],
    keywords=[
        "gif",
        "gifs",
        "animation",
        "PIL",
        "pillow",
        "matplotlib",
    ],
    url="https://github.com/maxhumber/gif",
    author="Max Humber",
    author_email="max.humber@gmail.com",
    license="MIT",
    py_modules=["gif"],
    install_requires=["matplotlib>=3.5.2", "Pillow>=9.1.0"],
    extras_require={
        "test": [
            "black>=22.3.0",
            "matplotlib>=3.5.2",
            "pandas>=1.4.2",
            "pytest>=7.1.2"
        ],
    },
    python_requires=">=3.9",
    setup_requires=["setuptools>=62.1.0"],
)
