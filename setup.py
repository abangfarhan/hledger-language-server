from setuptools import setup

setup(
    name='hledger-language-server',
    version='0.1',
    description='Language server for hledger file',
    author='Abang Farhan',
    author_email='abangfarhan31@gmail.com',
    license='MIT',
    install_requires=[
        'pygls'
    ],
    packages=['hledger_ls'],
    zip_safe=False,
    entry_points={
        'console_scripts': ['hledger-language-server=hledger_ls:main']
    },
)
