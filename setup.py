from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bakaweb-timetable",  
    version="1.0",  
    description="Nástroj pro extrahování rozvrhu z Timetable modulu Bakawebu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Lukáš S.",
    url="https://github.com/MortikCZ/Bakaweb-Timetable",
    packages=find_packages(),
    install_requires=[
        "requests>=2.0",
        "beautifulsoup4>=4.6"
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Natural Language :: Czech",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="bakaweb timetable rozvrh extractor",
    project_urls={  
        "Bug Tracker": "https://github.com/MortikCZ/Bakaweb-Timetable/issues",
        "Documentation": "https://github.com/MortikCZ/Bakaweb-Timetable#readme",
        "Source Code": "https://github.com/MortikCZ/Bakaweb-Timetable",
    },
)
