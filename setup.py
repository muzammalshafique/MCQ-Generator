from setuptools import find_packages, setup
setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Muzammil Shafique",
    author_email="muzammalsha632@gmail.com",
    install_requirs = ['openai', 'langchain', 'streamlit', 'python-dotenv', 'PyPDF2'],
    packages=find_packages()
)