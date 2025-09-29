from setuptools import setup, find_packages

setup(
    name="mlproject",  # Package name
    version="0.1.0",   # Start with 0.1.0 and increment as you release
    author="Shweta Joshi",
    author_email="joshis@ussilica.com",
    description="A sample machine learning project - Python Foundations Food Hub",
    long_description=open("README.md").read(),  # falls back to README.md
    long_description_content_type="text/markdown",
    url="https://github.com/joshisaiml/PythonFoundation",
    packages=find_packages(),   # Automatically finds packages in your folder
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Or the license you prefer
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[          # Dependencies go here
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
    ],
)
