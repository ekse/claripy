from distutils.core import setup

setup(
    name='claripy',
    version='4.6.2.25',
    packages=['claripy', 'claripy.backends', 'claripy.frontends', 'claripy.vsa', 'claripy.ast'],
    install_requires=[
        'ana',
        'angr-only-z3-custom',
    ],
    description='An abstraction layer for constraint solvers',
    url='https://github.com/angr/claripy',
)
