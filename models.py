from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer, DateTime
from db import Base
from db import engine

Base = declarative_base()

class DadoCLPVent(Base):
    __tablename__ = 'dadoclpvent'

    id = Column(Integer,primary_key = True)
    timestamp = Column(DateTime)#/10
    temp_e_r = Column(Integer)# /10
    temp_e_s = Column(Integer)# /10
    temp_e_t = Column(Integer) #float
    temp_c = Column(Integer) #float
    freq_mot_rpm = Column(Integer)# float
    torq_vent_r = Column(Integer)# float
    freq_rot_vent_a = Column(Integer)#float
    torq_vent_a = Column(Integer) #float
    vaz_a = Column(Integer)# float
    vel_a = Column(Integer)# float
    temp_a = Column(Integer)#float
    temp_tb_a = Column(Integer)# /10
    temp_tb_v = Column(Integer)# /10
    troc_com_pm = Column(Integer)
    lip_mot = Column(Integer)

    Base.metadata.create_all(engine)