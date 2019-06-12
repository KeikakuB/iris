from setuptools import setup, find_packages
setup(
    name="iris",
    version="1.0",
    py_modules=['iris'],
    packages=find_packages(),
    python_requires='>=3',
    install_requires=['click', 'newspaper3k'],
    entry_points='''
        [console_scripts]
        iris=iris:cli
    ''',
)
