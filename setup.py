from setuptools import setup


setup(
    name='klibee',
    version='0.0.1',    
    description='Klibee Library',
    url='git@github.com:klibee/library.git',
    author='Klibee',
    author_email='gonzaloaizpun@gmail.com',
    license='Apache',
    packages=[  'klibee',
                'klibee/environment',
                'klibee/exceptions',
                'klibee/logger',
                'klibee/redis',
                'klibee/redis/channel',
                'klibee/redis/connection',
            ], 
    include_package_data=True,
    install_requires=[
                      'mysql-connector-python',
                      'python-dotenv',
                      'redis',
                      ],

    classifiers=[
        'License :: OSI Approved :: Apache 2.0',  
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)