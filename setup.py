from setuptools import setup

setup(
  name='preparepack',
  author='Cargo',
  version='1.1.0',
  packages=['prepack'],
  license='MIT',
  install_requires=['click'],
  entry_points='''
  [console_script]
  prepack=prepack:prepack,
  buildpack=prepack:build
  '''
)
