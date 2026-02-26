from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="surenav",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Open-source web unblocker for AI agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/surenav",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=[
        "fastapi>=0.109.0",
        "uvicorn[standard]>=0.27.0",
        "playwright>=1.41.0",
        "playwright-stealth>=1.0.6",
        "beautifulsoup4>=4.12.3",
        "markdownify>=0.11.6",
        "aiohttp>=3.9.3",
        "aiofiles>=23.2.1",
        "fake-useragent>=1.4.0",
        "pydantic>=2.6.0",
        "pyyaml>=6.0.1",
        "httpx>=0.26.0",
    ],
    entry_points={
        "console_scripts": [
            "surenav-server=surenav.server:main",
        ],
    },
)
