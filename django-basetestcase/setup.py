import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-basetestcase',
    version='1.0.3',
    author='Carl Brubaker',
    author_email='spleeding@juno.com',
    description='A collection of cheater methods for the Django TestCase.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/spleeding1/django-basetestcase',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)