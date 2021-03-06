import setuptools

setuptools.setup(name='tieronepointfive',
      version='0.1.0',
      description='Program meant to automatically reboot a cable modem and router when a network outage is detected',
      author='Kevin Barnes',
      author_email='kbarnes3@gmail.com',
      url='https://github.com/kbarnes3/TierOnePointFive',
      license='Other',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Topic :: Software Development',
          'License :: Other/Proprietary License',
          "Operating System :: OS Independent",
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          ],
      include_package_data=True,
      install_requires=['appdirs>=1.4.3', 'requests>=2.18.1', 'jsoncomment>=0.2.3', 'ouimeaux>=0.8'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest', 'requests_mock>=1.3.0'],
      packages=['tieronepointfive', 'tieronepointfive.evaluation_helpers'],
      entry_points={
          'console_scripts': [
              'tieronepointfive = tieronepointfive.console:run',
          ]
      },
      )
