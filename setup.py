from setuptools import setup, find_packages

setup(
    name="lazytrainer",
    version="0.1.0",
    author="Mr. Phantom",
    author_email="mrfayntom@gmail.com",
    description="lazyml: Because training ML models shouldn’t need more energy than your morning coffee.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mrfayntom/LazyML", 
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib",
        "joblib",
        "tqdm"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7',
)
