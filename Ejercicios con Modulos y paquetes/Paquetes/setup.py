from setuptools import setup

setup(
    name="paquete",
    version="0.1",
    description="este es una paquete de ejemplo",
    author="Javier Ramos",
    author_email="jaramosperez85@gmail.com",
    scripts=[],
    packages=["paquete", "paquete.adios", "paquete.hola"]
)