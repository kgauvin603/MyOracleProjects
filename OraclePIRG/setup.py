
from setuptools import setup, find_packages

setup(
    name="OraclePIRG",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
        "langchain",
        "langchain-community",
        "gradio",
        "matplotlib",
        "transformers",
        "torch",
        "graphviz",
        "networkx",
        "scikit-learn",
        "beautifulsoup4",
        "reportlab",
        "fpdf2"
    ],
    author="Oracle PIRG Team",
    description="Oracle Personalized Investment Report Generator",
    python_requires=">=3.8"
)
