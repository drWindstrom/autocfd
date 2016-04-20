"""Defines classes to hold a FLOWer setup."""

from sqlalchemy import (Column, Integer, Float, String, ForeignKey, Boolean, inspect)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class FlowerSetup(Base):
    """Bla."""

    __tablename__ = 'flower_setup'

    idx = Column(Integer(), primary_key=True)
    setup_name = Column(String(255))
    dimension = relationship('Dimension', uselist=False, back_populates='flower_setup')
    general_control = relationship('GeneralControl', uselist=False,
                                   back_populates='flower_setup')


class Dimension(Base):
    """Bla."""

    __tablename__ = 'dimension'

    idx = Column(Integer(), primary_key=True)
    imaxwork = Column(Integer())
    maxwork = Column(Integer())
    maxiter = Column(Integer())
    flower_setup_idx = Column(Integer(), ForeignKey('flower_setup.idx'))
    flower_setup = relationship('FlowerSetup', back_populates='dimension')


class GeneralControl(Base):
    """Bla."""

    __tablename__ = 'general_control'

    idx = Column(Integer(), primary_key=True)
    string = Column(String(255))
    i2d3d = Column(Integer())
    iaxisym = Column(Integer())
    axiangle = Column(Float())
    isweep = Column(Integer())
    sweepangle = Column(Float())
    ivisall = Column(Integer())
    itlns = Column(Integer())
    ifluxvis = Column(Integer())
    walldist = Column(Integer())
    itranstn = Column(Integer())
    itransition = Column(Integer())
    ih0zero = Column(Integer())
    normresi = Column(Float())
    restol = Column(Float())
    fotol = Column(Float())
    smallvol = Column(Float())
    nsave = Column(Integer())
    iprint = Column(Integer())
    istepout = Column(Integer())
    flower_setup_idx = Column(Integer(), ForeignKey('flower_setup.idx'))
    flower_setup = relationship('FlowerSetup', back_populates='general_control')
