
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Boolean, inspect
from sqlalchemy.orm import relationship
from base import Base


class Blade(Base):
    """Bla."""

    __tablename__ = 'blade'

    idx = Column(Integer(), primary_key=True)
    airfoils = relationship('Airfoil', back_populates='blade')
    blade_name = Column(String(255))


class Airfoil(Base):
    """Bla."""

    __tablename__ = 'airfoil'

    idx = Column(Integer(), primary_key=True)

    blade_idx = Column(Integer(), ForeignKey('blade.idx'))
    blade = relationship('Blade', back_populates='airfoils')
    simulations = relationship('Simulation', back_populates='airfoil')

    airfoil_name = Column(String(255))


class Simulation(Base):
    """Bla."""

    __tablename__ = 'simulation'

    idx = Column(Integer(), primary_key=True)

    airfoil_idx = Column(Integer(), ForeignKey('airfoil.idx'))
    airfoil = relationship('Airfoil', back_populates='simulations')
    cfd_setup = relationship('FlowerSetup', uselist=False, back_populates='simulation')

    simulation_name = Column(String(255))
    job_state = Column(String(80))
    convergence_state = Column(String(80))
    # TODO cluster_setup and convergence details
