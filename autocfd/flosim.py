"""Defines the FLOWer Simulation class."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class Simulation(Base):
    """Bla."""

    __tablename__ = 'simulation'

    idx = Column(Integer(), primary_key=True)

    airfoil_idx = Column(Integer(), ForeignKey('airfoil.idx'))
    airfoil = relationship('Airfoil', back_populates='simulations')
    solver_setup = relationship('SolverSetup', uselist=False, back_populates='simulation')

    simulation_name = Column(String(255))
    job_state = Column(String(80))
    convergence_state = Column(String(80))
    # TODO cluster_setup and convergence details
