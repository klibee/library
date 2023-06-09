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
                'klibee/dates',
                'klibee/dates/timestamp',
                'klibee/environment',
                'klibee/exceptions',
                'klibee/exceptions/common',
                'klibee/exceptions/files',
                'klibee/exceptions/env',
                'klibee/exceptions/redis',
                'klibee/exceptions/telegram',
                'klibee/files',
                'klibee/files/common',
                'klibee/files/write',
                'klibee/hasher',
                'klibee/logger',
                'klibee/logger/constants',
                'klibee/logger/error',
                'klibee/logger/format',
                'klibee/logger/info',
                'klibee/logger/success',
                'klibee/random',
                'klibee/random/persons',
                'klibee/random/products',
                'klibee/redis',
                'klibee/redis/channel',
                'klibee/redis/connection',
                'klibee/redis/constructor',
                'klibee/redis/keys',
                'klibee/redis/read',
                'klibee/redis/write',
                'klibee/tasks',
                'klibee/tasks/read',
                'klibee/tasks/write',
                'klibee/telegram',
                'klibee/telegram/connection',
                'klibee/telegram/constructor',
                'klibee/telegram/conversations',
                'klibee/telegram/messages',
                'klibee/unique',
                'klibee/unique/id',
            ], 
    include_package_data=True,
    install_requires=[
                      'mysql-connector-python',
                      'python-dotenv',
                      'pandas',
                      'redis',
                      'telethon',
                      ],

    classifiers=[
        'License :: OSI Approved :: Apache 2.0',  
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)