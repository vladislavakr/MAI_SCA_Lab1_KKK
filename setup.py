#!/usr/bin/env python3
"""
Setup script для Hello World приложения
"""

from setuptools import setup, find_packages

setup(
    name="hello-world-sca-demo",
    version="1.0.0",
    description="Hello World приложение для демонстрации композиционного анализа ПО",
    author="MAI Student",
    author_email="student@mai.ru",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "click>=8.1.7",
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "hello-world=app:main",
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)