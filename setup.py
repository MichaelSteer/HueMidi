from setuptools import setup


def readme():
    with open('README.MD') as rd:
        return rd.read()


setup(name='MidiHue',
      version='0.0',
      description='Phillips Hue MIDI Control Library',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Audio Interfacing :: MIDI',
      ],
      keywords='MIDI Hue Phillips Audio Performance Lighting',
      url='https://github.com/MichaelSteer/HueMidi',
      author='Michael Steer',
      author_email='steer@ualberta.ca',
      license='MIT',
      packages=['HueMidi'],
      install_requires=[
          'markdown',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={},
      include_package_data=True,
      zip_safe=False)
