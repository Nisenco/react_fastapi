from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, SmallInteger, DateTime, \
    text, func, Date, UniqueConstraint
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


class HistoryPassword(Base, MyMixin):
    __tablename__ = "history_password"
    user_id = Column(Integer, nullable=False, comment='用户id')
    hashed_password = Column(String(64), comment='密码')

    __table_args__ = (
        UniqueConstraint('user_id', 'hashed_password', name='user_password_uk'),
    )


class Level(Base, MyMixin):
    __tablename__ = "level"
    name = Column(String(255), unique=True, nullable=False, comment='级别名称')


class Group(Base, MyMixin):
    __tablename__ = "group"
    name = Column(String(255), unique=True, nullable=False, comment='小组名称')


class Position(Base, MyMixin):
    __tablename__ = "position"
    name = Column(String(255), unique=True, nullable=False, comment='职位名称')


class Project(Base, MyMixin):
    __tablename__ = "project"

    name = Column(String(255), nullable=False, unique=True, comment='项目名称')
    manager_id = Column(Integer, nullable=True, comment='项目经理id')
    manager_name = Column(String(255), nullable=True, comment='项目经理姓名')
    total = Column(Integer, nullable=False, default=0, comment='项目总工时')
    used = Column(Integer, nullable=False, default=0, comment='已分配工时')
    status = Column(SmallInteger, nullable=False, default=0, comment='0-申请中，1-申请通过，2-申请未通过')
    type = Column(SmallInteger, nullable=False, default=0, comment='0-组内日常工作，1-公共事项，2-项目')
    start_time = Column(Date, default=datetime.datetime.now, comment='项目开始时间')
    end_time = Column(Date, default=datetime.datetime.now, comment='项目结束时间')


class Participant(Base, MyMixin):
    __tablename__ = "participant"

    user_id = Column(Integer, nullable=False, comment="用户id")
    project_id = Column(Integer, nullable=False, comment="项目id")
    type = Column(SmallInteger, nullable=False, comment='人员参与类型 0参与者 1 助理  2 manager 3supervisor')
    flexible_hour = Column(Integer, nullable=False, default=0, comment='可用灵活工时')

    __table_args__ = (
        UniqueConstraint('user_id', 'project_id', name='user_project_uk'),
    )


class ManHour(Base, MyMixin):
    __tablename__ = "man_hour"
    # daily_report_id = Column(Integer, nullable=True, comment="daily_report id")
    event_id = Column(Integer, nullable=False, comment="项目外键")
    event_name = Column(String(255), nullable=False, comment="项目名称")
    user_id = Column(Integer, nullable=False, comment="user id")
    date = Column(Date, comment="分配日期")
    type = Column(SmallInteger, comment="0-组内，1-公共事项，2-项目灵活，3-项目预约")
    status = Column(SmallInteger, nullable=False, default=0, comment='0-待审核  1-审核通过 2-拒绝')
    normal_hour_approved = Column(Integer, default=0, server_default=text("0"), comment="审批通过正常工时数")
    normal_hour_submitted = Column(Integer, default=0, server_default=text("0"), comment="申报正常工时数")
    ot_hour_approved = Column(Integer, default=0, server_default=text("0"), comment="审批通过加班工时数")
    ot_hour_submitted = Column(Integer, default=0, server_default=text("0"), comment="申报加班工时数")
    score = Column(SmallInteger, default=0, server_default=text("0"), comment="日报评分")
    # 项目预约 项目 灵活 组内工时


class ManHourDetail(Base, MyMixin):
    __tablename__ = "man_hour_detail"
    man_hour_id = Column(Integer, unique=True, comment="man_hour id")
    report = Column(String(2048), comment="工时日报详情")


class DailyReport(Base, MyMixin):
    __tablename__ = "daily_report"
    user_id = Column(Integer, nullable=False, comment="user id")
    date = Column(Date, nullable=False, comment="日报日期")
    location = Column(SmallInteger, nullable=False, comment="工作地点 0-在台 1-在家 2-其他")
    shift = Column(SmallInteger, nullable=False, comment="排班 0-7:00到15:00 1-9:30到18:30 2-15:00到23:00 3-23:00到7:00")
    report = Column(String(2048), nullable=False, comment="工作总结")
    plan = Column(String(2048), nullable=False, comment="明日计划")

    __table_args__ = (
        UniqueConstraint('user_id', 'date', name='user_date_uk'),
    )


class PositionHour(Base, MyMixin):
    __tablename__ = "position_hour"
    position_id = Column(Integer, nullable=False, comment="position id")
    application_id = Column(Integer, nullable=False, comment="application id")
    hour = Column(Integer, nullable=False, comment="预约工时数")

    __table_args__ = (
        UniqueConstraint('position_id', 'application_id', name='pos_app_uk'),
    )


class Application(Base, MyMixin):
    __tablename__ = "application"
    project_id = Column(Integer, nullable=False, comment="项目id")
    type = Column(SmallInteger, nullable=False, comment='0-新建 1-延期')
    status = Column(SmallInteger, nullable=False, comment='0-申请中，1-申请通过，2-申请未通过')
    hour = Column(Integer, nullable=False, default=0, comment='申请工时数')
    detail = Column(String(2048), nullable=False, comment='申请详情描述')


class ApplicationImage(Base, MyMixin):
    __tablename__ = "application_image"
    application_id = Column(Integer, nullable=False, comment="application id")
    url = Column(String(255), nullable=False, comment="图片url")
