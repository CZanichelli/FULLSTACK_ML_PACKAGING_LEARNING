from setuptools import setup, find_packages

setup(
    name ="taxipred",
    version="0.01",
    description="This package contains texipred app wich will predict taxi prices",
    author="Casper",
    author_email="CasperZanichelli98@gmail.com",
    install_requires=["streamlit", "pandas", "fastapi", "scikit-learn", "uvicorn"],
    package_dir={"": "src"},
    package_data={"taxipred": ["data/*.csv"]},
    packages=find_packages()
)