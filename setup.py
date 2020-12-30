from setuptools import setup

setup(
    name='GL-DevOps-ProCamp-Entry-Task-Metrics',
    version='0.0.1',
    packages=[
        'metrics'
    ],
    install_requires=[
        'psutil==5.8.0',
        'tabulate==0.8.7',
    ],
    entry_points='''
        [console_scripts]
        GL-DevOps-ProCamp-Entry-Task-Metrics=metrics.metrics:main
    ''',
)
