from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['lang_evo'],
    scripts=['scripts/run_world.py', 'scripts/run_agent.py'],
    package_dir={'': 'src'}
)

setup(**d)