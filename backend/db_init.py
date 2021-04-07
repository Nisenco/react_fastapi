from app.db import models,orm

if __name__ == '__main__':
    orm.Base.metadata.create_all(orm.engine)