from setuptools import setup

setup(
    name="crypto-listed-detector",
    version="1.0.0",
    description="The Docker Image detects that a crypto currency has been listed.",
    install_requires=[
        "pytest",
    ],
    author="aoki-h-jp",
    author_email="aoki.hirotaka.biz@gmail.com",
    license="MIT",
    packages=["crypto_listed_detector"],
)
