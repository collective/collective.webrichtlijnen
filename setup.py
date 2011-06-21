from setuptools import setup, find_packages
import os

version = '1.1-SNAPSHOT'

setup(name='collective.webrichtlijnen',
      version=version,
      description="A theme product for the Dutch web guidelines.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "INSTALL.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone theme dutch web guidelines webrichtlijnen',
      author='Kim Chee Leong',
      author_email='leong@gw20e.com',
      url='http://pypi.python.org/pypi/collective.webrichtlijnen/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone > 4.0a',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      """,
      setup_requires=["PasteScript"],

      paster_plugins = ["ZopeSkel"],
      )
