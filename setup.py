from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="password-generator",      
    version="0.1.0",                     
    author="xiazaiyong",
    author_email="your@email.com",
    description="一个随机密码生成器",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xiazaiyong/RandomPasswordGenerator",
    packages=find_packages(),            
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[   
    ],
    entry_points={                       
        "console_scripts": [
            "pwdgen=password_generator.cli:main",
        ],
    },
)
