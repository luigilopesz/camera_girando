from setuptools import setup, find_packages

setup(
  name="camera_girando",
  version="0.1",
  author="Luigi Lopes",
  author_email="luigilopes09@gmail.com",
  description="Projeto para acessar a câmera e realizar manipulações",
  url="https://github.com/luigilopesz/camera_girando",
  packages=find_packages(),
  install_requires=[
    "click==8.1.7",
    "colorama==0.4.6",
    "markdown-it-py==3.0.0",
    "mdurl==0.1.2",
    "numpy==2.1.1",
    "opencv-python==4.10.0.84",
    "pandas==2.2.2",
    "Pygments==2.18.0",
    "python-dateutil==2.9.0.post0",
    "pytz==2024.1",
    "rich==13.8.0",
    "shellingham==1.5.4",
    "six==1.16.0",
    "typer==0.12.5",
    "typing_extensions==4.12.2",
    "tzdata==2024.1",
  ],
  entry_points={
    'console_scripts': [
      'camera_girando=camera_girando.main:main',
    ],
  },
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.7',
)
