from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
clinic = Table('clinic', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('education', VARCHAR(length=300)),
    Column('expertise', VARCHAR(length=300)),
    Column('experience', INTEGER),
    Column('description', VARCHAR(length=500)),
    Column('area', VARCHAR(length=100)),
    Column('city', VARCHAR(length=100)),
    Column('country', VARCHAR(length=100)),
    Column('completeaddress', VARCHAR(length=300)),
    Column('fee', INTEGER),
    Column('expertise_field', VARCHAR(length=100)),
    Column('consult_start_day', INTEGER),
    Column('consult_end_day', INTEGER),
    Column('consult_start_time_hour', INTEGER),
    Column('consult_end_time_hour', INTEGER),
    Column('consult_start_time_minute', INTEGER),
    Column('consult_end_time_minute', INTEGER),
    Column('phone_number', VARCHAR(length=10)),
    Column('dial_extension', VARCHAR(length=5)),
    Column('specialization', VARCHAR(length=50)),
    Column('sponsored', BOOLEAN),
    Column('recommended', INTEGER),
)

doctor = Table('doctor', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('education', VARCHAR(length=300)),
    Column('expertise', VARCHAR(length=300)),
    Column('experience', INTEGER),
    Column('description', VARCHAR(length=500)),
    Column('area', VARCHAR(length=100)),
    Column('city', VARCHAR(length=100)),
    Column('country', VARCHAR(length=100)),
    Column('completeaddress', VARCHAR(length=300)),
    Column('fee', INTEGER),
    Column('expertise_field', VARCHAR(length=100)),
    Column('consult_start_day', INTEGER),
    Column('consult_end_day', INTEGER),
    Column('consult_start_time_hour', INTEGER),
    Column('consult_end_time_hour', INTEGER),
    Column('consult_start_time_minute', INTEGER),
    Column('consult_end_time_minute', INTEGER),
    Column('phone_number', VARCHAR(length=10)),
    Column('dial_extension', VARCHAR(length=5)),
    Column('specialization', VARCHAR(length=50)),
    Column('sponsored', BOOLEAN),
    Column('recommended', INTEGER),
)

doctor = Table('doctor', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('education', String(length=300)),
    Column('expertise', String(length=300)),
    Column('experience', Integer),
    Column('email', String(length=100)),
    Column('description', String(length=500)),
    Column('specialization', String(length=50)),
    Column('area', String(length=100)),
    Column('city', String(length=100)),
    Column('country', String(length=100)),
    Column('completeaddress', String(length=300)),
    Column('fee', Integer),
    Column('timings', String(length=300)),
    Column('phone_number', String(length=10)),
    Column('dial_extension', String(length=5)),
    Column('sponsored', Boolean, default=ColumnDefault(True)),
    Column('recommended', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['clinic'].drop()
    pre_meta.tables['doctor'].columns['consult_end_day'].drop()
    pre_meta.tables['doctor'].columns['consult_end_time_hour'].drop()
    pre_meta.tables['doctor'].columns['consult_end_time_minute'].drop()
    pre_meta.tables['doctor'].columns['consult_start_day'].drop()
    pre_meta.tables['doctor'].columns['consult_start_time_hour'].drop()
    pre_meta.tables['doctor'].columns['consult_start_time_minute'].drop()
    pre_meta.tables['doctor'].columns['expertise_field'].drop()
    post_meta.tables['doctor'].columns['email'].create()
    post_meta.tables['doctor'].columns['timings'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['clinic'].create()
    pre_meta.tables['doctor'].columns['consult_end_day'].create()
    pre_meta.tables['doctor'].columns['consult_end_time_hour'].create()
    pre_meta.tables['doctor'].columns['consult_end_time_minute'].create()
    pre_meta.tables['doctor'].columns['consult_start_day'].create()
    pre_meta.tables['doctor'].columns['consult_start_time_hour'].create()
    pre_meta.tables['doctor'].columns['consult_start_time_minute'].create()
    pre_meta.tables['doctor'].columns['expertise_field'].create()
    post_meta.tables['doctor'].columns['email'].drop()
    post_meta.tables['doctor'].columns['timings'].drop()
