import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="ebp",
  version="1.0.2",
  author="Yuhao Cheng",
  author_email="chengyuhao_work@outlook.com",
  description="a small tool to build the project",
#   long_description=long_description,
#   long_description_content_type="text/markdown",
  url="https://github.com/YuhaoCheng/EasyBuildProject",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
  entry_points={
    'console_scripts':[
      'ebp = EasyBuildProject.ebp:main'
    ]
  },
  # scripts=['ebp.py'],
)