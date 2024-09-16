from setuptools import setup, find_packages
import os

setup(
  name="camera",  # Nome do seu pacote
  version="0.1",
  packages=find_packages(),  # Encontrar automaticamente todos os pacotes
  install_requires=[line.strip() for line in open("requirements.txt").readlines()],  # Adicione dependências aqui, se necessário
  entry_points={
      'console_scripts': [
        'camera_girando=camera_girando.main:main',  # Nome do comando CLI e função a ser chamada
      ],
  },

  # Metadados para o PyPI (Python Package Index)
  author="Luigi Carmona de Miranda Lopes",
  author_email="luigilopes09@gmail.com",
  description="camera do Luigi!",
  long_description=open("README.md").read() if os.path.exists("README.md") else "",
  long_description_content_type="text/markdown",
  url="https://github.com/luigilopesz/camera_girando",  # Substitua pelo URL do seu repositório, se houver
  classifiers=[
    "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',  # Requer Python 3.6 ou superior
)