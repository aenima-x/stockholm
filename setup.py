from distutils.core import setup

setup(
    name='stockholm',
    version='0.1',
    packages=['stockholm', 'stockholm.cdr', 'stockholm.cdr.modules', 'stockholm.asn1'],
    url='https://github.com/aenima-x/stockholm',
    license='',
    author='Nicolas Rebagliati',
    author_email='nicolas.rebagliati@aenima-x.com.ar',
    description='Module to decode Ericsson Call Data Records'
)
