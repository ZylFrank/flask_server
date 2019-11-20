#!/usr/bin/env python
import os
from dotenv import load_dotenv

from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

load_dotenv()

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)
migrate = Migrate(app)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


# shell脚本
manager.add_command('shell', Shell(make_context=make_shell_context))
# 数据库迁移
manager.add_command('db', MigrateCommand)


# 测试用例
@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


# 初始化数据库表: python manage.py init_db
@manager.command
def init_db():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()
