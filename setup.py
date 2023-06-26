from setuptools import setup, find_packages

setup(
    name='text-summarizer',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'transformers',
        'torch',
    ],
    entry_points={
        'console_scripts': [
            'text-summarizer = app:main',
        ],
    },
)
