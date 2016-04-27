"""Holds the base table definitions."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base


class Blade(Base):
    """Bla."""

    __tablename__ = 'blade'

    idx = Column(Integer(), primary_key=True)
    airfoils = relationship('Airfoil', back_populates='blade')
    blade_name = Column(String(255))
