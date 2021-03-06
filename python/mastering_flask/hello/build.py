from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('python.pycharm')


name = "hello"
default_task = "publish"


@init
def set_properties(project):
    project.version = '0.1'
    project.depends_on('flask')
    project.depends_on('flask-script')
