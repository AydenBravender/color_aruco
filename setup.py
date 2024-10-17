# setup.py
from setuptools import setup, find_packages

setup(
    name="color_aruco",  # Package name
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "opencv-python",  # Dependency for OpenCV
        "numpy"           # Dependency for NumPy
    ],
    author="Ayden Bravender",
    author_email="Aydenbravender@gmail.com",
    description="A package to detect colored ArUco markers.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/AydenBravender/color_aruco.git",  # Link to your GitHub repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
