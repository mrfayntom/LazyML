from setuptools import setup, find_packages

setup(
    name="lazyml",
    version="0.1.0",
    author="Mr. Phantom",
    description="lazyml: Because training ML models shouldn’t need more energy than your morning coffee.",
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
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.7',
    license="MIT"
)
