from setuptools import setup, find_packages

setup(
    name='agent_scaffolder',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'scaffold-project = project_scaffolder.scaffolder:main',
        ],
    },
)

