from setuptools import find_packages, setup

setup(
    name="transfermarkt_pipeline",
    packages=find_packages(exclude=["transfermarkt_pipeline_tests"]),
    install_requires=[
        "dagster",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
