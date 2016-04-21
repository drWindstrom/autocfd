"""Defines classes to hold a FLOWer setup."""

from sqlalchemy import Column, Integer, Float, String, ForeignKey, Boolean, inspect
from sqlalchemy.orm import relationship
from base import Base




class FlowerSetup(Base):
    """Bla."""

    __tablename__ = 'flower_setup'

    idx = Column(Integer(), primary_key=True)

    simulation_idx = Column(Integer, ForeignKey('simulation.idx'))
    simulation = relationship('Simulation', back_populates='cfd_setup')

    dimension = relationship('Dimension', uselist=False, back_populates='flower_setup')
    general_control = relationship("GeneralControl", uselist=False,
                                   back_populates='flower_setup')

    setup_name = Column(String(255))
    alpha = Column(Integer())


class Dimension(Base):
    """Bla."""

    __tablename__ = 'dimension'

    idx = Column(Integer(), primary_key=True)

    flower_setup_idx = Column(Integer(), ForeignKey('flower_setup.idx'))
    flower_setup = relationship("FlowerSetup", back_populates='dimension')

    imaxwork = Column(Integer())
    maxwork = Column(Integer())
    maxiter = Column(Integer())


class GeneralControl(Base):
    """Bla."""

    __tablename__ = 'general_control'

    idx = Column(Integer(), primary_key=True)

    flower_setup_idx = Column(Integer(), ForeignKey('flower_setup.idx'))
    flower_setup = relationship("FlowerSetup", back_populates='general_control')

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
