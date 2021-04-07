from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, SmallInteger, DateTime, \
    text, func
from .orm import Base
from sqlalchemy.orm import relationship
import datetime


class MyMixin(object):
    __table_args__ = {'mysql_engine': 'InnoDB'}
    __mapper_args__ = {'always_refresh': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(DateTime, default=datetime.datetime.now,
                         server_default=text("CURRENT_TIMESTAMP"), comment="条目创建")
    update_time = Column(DateTime, default=datetime.datetime.now, nullable=False,
                         server_default=func.now(), onupdate=func.now(),
                         # server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), onupdate=True,
                         comment="条目更新")

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    @classmethod
    def get_all_table_cloumns(cls):
        return [c.name for c in cls.__table__.columns]


class User(Base, MyMixin):
    __tablename__ = "user"

    account = Column(String(255), unique=True, nullable=False, comment='用户邮箱')
    hashed_password = Column(String(64), comment='密码')
    name = Column(String(255), nullable=False, comment='用户姓名')
    employee_id = Column(String(255), unique=True, nullable=True, comment='工号')
    role = Column(SmallInteger, nullable=False, comment='0-管理员，1-主管，2-员工')
    status = Column(SmallInteger, nullable=False, default=0, comment='0-在职，1-离职 2-账号被锁定')
    is_manager = Column(Boolean, nullable=False, comment='能否创建项目：false-不能，true-可以')
    passwd_update_time = Column(DateTime, comment='密码更新时间')
    group_id = Column(Integer, nullable=False, comment='group表id')
    level_id = Column(Integer, nullable=False, comment='level表id')
    position_id = Column(Integer, nullable=False, comment='position表id')


# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     # username = Column(String)
#     # create_time = Column(String,nullable=False)
#     # loginTime = Column(String,nullable=False)
#     hashed_password = Column(String, nullable=True)
#     is_active = Column(Boolean, nullable=True)
#     # is_superuser = Column(Boolean, nullable=True)
#
#     items = relationship('Item', back_populates='owner')
