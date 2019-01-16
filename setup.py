from setuptools import setup, find_packages
setup(
    name='syncwerk-server-python-django-registration',
    version='20181227',
    author='Syncwerk GmbH',
    author_email='support@syncwerk.com',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    url='https://www.syncwerk.com',
    license='BSD 3-Clause',
    description='Django Registration',
    long_description='An extensible user-registration app for Django',
    platforms=['any'],
    include_package_data=True,
)
