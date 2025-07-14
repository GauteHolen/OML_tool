from setuptools import setup, find_packages
setup(
   name='OML_tool',
   version='0.1',
   packages=find_packages(),
   license='MIT',
   author='Gaute Holen',
   author_email='gaute.ah@gmail.com',
   long_description=open('README.md').read(),
   url='https://github.com/GauteHolen/OML_tool',
   install_requires=[
       'numpy']
)