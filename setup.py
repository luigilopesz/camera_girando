from setuptools import setup, find_packages


setup(
  name="camera_girando",
  version="0.1.0",
  packages=find_packages(),
  install_requires=["opencv-python", "numpy"],
  author="Luigi Lopes",
  author_email="luigilopes09@gmail.com",
  description="...",
  long_description=open('README.md').read(),
  long_description_content_type="text/markdown",
  url="https://github.com/luigilopesz/camera_girando",
  entry_points={
    'console_scripts': [
      'teste=camera_girando.main:main',
    ],
  },
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)