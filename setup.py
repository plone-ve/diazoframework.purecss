from setuptools import setup, find_packages
import os

version = '1.1.dev0'

setup(name='diazoframework.purecss',
      version=version,
      description="A Diazo framework implementation for Pure CSS",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: Theme",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme diazo pure css framework',
      author='Thijs Jonkman',
      author_email='t.jonkman@gmail.com',
      maintainer='Leonardo Caballero',
      maintainer_email='leonardocaballero@gmail.com',
      url='https://github.com/TH-code/diazoframework.purecss',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['diazoframework'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'diazoframework.plone',
          'diazotheme.purecss',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
