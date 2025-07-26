#!/usr/bin/env python3
"""
Setup script for Nutrio Bot
A comprehensive nutrition assistant for Indian users
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Nutrio Bot - AI Nutrition Assistant"

# Read requirements
def read_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="nutrio-bot",
    version="1.0.0",
    author="Nutrio Team",
    author_email="support@nutrio-bot.com",
    description="AI-powered nutrition assistant Telegram bot for Indian cuisine",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/nutrio",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Communications :: Chat",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Framework :: Telegram Bot",
    ],
    python_requires=">=3.10",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
        "docker": [
            "docker>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "nutrio-bot=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.json", "*.txt", "*.md"],
    },
    keywords=[
        "telegram",
        "bot",
        "nutrition",
        "health",
        "indian-cuisine",
        "meal-planning",
        "ai",
        "firebase",
    ],
    project_urls={
        "Bug Reports": "https://github.com/yourusername/nutrio/issues",
        "Source": "https://github.com/yourusername/nutrio",
        "Documentation": "https://github.com/yourusername/nutrio/blob/main/DEPLOYMENT.md",
        "Changelog": "https://github.com/yourusername/nutrio/blob/main/CHANGELOG.md",
    },
    zip_safe=False,
) 