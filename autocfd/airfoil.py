"""Holds the base table definitions."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class Airfoil(Base):
    """Bla."""

    __tablename__ = 'airfoil'

    idx = Column(Integer(), primary_key=True)

    blade_idx = Column(Integer(), ForeignKey('blade.idx'))
    blade = relationship('Blade', back_populates='airfoils')
    simulations = relationship('Simulation', back_populates='airfoil')

    airfoil_name = Column(String(255))
