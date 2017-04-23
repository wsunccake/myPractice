from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('python.pycharm')


name = "view_form"
default_task = "publish"


@init
def set_properties(project):
    project.version = '0.1'
    project.depends_on('flask')
    project.depends_on('flask-script')
    project.depends_on('flask-sqlalchemy')
    project.depends_on('Flask-Migrate')
#    project.depends_on('PyMySQL')    # mysql driver
#    project.depends_on('psycopg2')   # postgre driver
#    project.depends_on('pyobdc')     # mssql driver
#    project.depends_on('cx_Oracle')  # oracle driver
    project.depends_on('Flask-WTF')
    project.depends_on('requests')

