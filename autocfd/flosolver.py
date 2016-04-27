"""Defines classes to hold a FLOWer setup."""
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class SolverSetup(Base):
    """Bla."""

    __tablename__ = 'solver_setup'

    idx = Column(Integer(), primary_key=True)

    simulation_idx = Column(Integer, ForeignKey('simulation.idx'))
    simulation = relationship('Simulation', back_populates='solver_setup')

    dimension = relationship('Dimension', uselist=False, back_populates='solver_setup')
    general_control = relationship('GeneralControl', uselist=False,
                                   back_populates='solver_setup')
    flow_conditions = relationship('FlowConditions', uselist=False,
                                   back_populates='solver_setup')
    geometrical_scaling = relationship('GeometricalScaling', uselist=False,
                                       back_populates='solver_setup')
    # SpaceTimeDiscretization space_time_discretization
    # SlipCuspUpwind slip_cusp_upwind
    # BoundaryTreatment boundary_treatment
    # TurbulenceModels turbulence_models
    # ReynoldsStressModels reynolds_stress_models
    # MultigridControl multigrid_control
    # RungeKuttaControl runge_kutta_control

    setup_name = Column(String(255))
    alpha = Column(Integer())


class Dimension(Base):
    """Bla."""

    __tablename__ = 'dimension'

    idx = Column(Integer(), primary_key=True)

    solver_setup_idx = Column(Integer(), ForeignKey('solver_setup.idx'))
    solver_setup = relationship("SolverSetup", back_populates='dimension')

    imaxwork = Column(Integer())
    maxwork = Column(Integer())
    maxiter = Column(Integer())


class GeneralControl(Base):
    """Bla."""

    __tablename__ = 'general_control'

    idx = Column(Integer(), primary_key=True)

    solver_setup_idx = Column(Integer(), ForeignKey('solver_setup.idx'))
    solver_setup = relationship("SolverSetup", back_populates='general_control')

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


class FlowConditions(Base):
    """Bla."""

    __tablename__ = 'flow_conditions'

    idx = Column(Integer(), primary_key=True)

    solver_setup_idx = Column(Integer(), ForeignKey('solver_setup.idx'))
    solver_setup = relationship("SolverSetup", back_populates='flow_conditions')

    mach = Column(Float())
    machref = Column(Float())
    alpha = Column(Float())
    yawangle = Column(Float())
    reno = Column(Float())
    relen = Column(Float())
    prno = Column(Float())
    prnot = Column(Float())
    gamma = Column(Float())
    pinf = Column(Float())
    rhoinf = Column(Float())
    tinf = Column(Float())
    ptotinf = Column(Float())
    ttotinf = Column(Float())


class GeometricalScaling(Base):
    """Bla."""

    __tablename__ = 'geometrical_scaling'

    idx = Column(Integer(), primary_key=True)

    solver_setup_idx = Column(Integer(), ForeignKey('solver_setup.idx'))
    solver_setup = relationship("SolverSetup", back_populates='geometrical_scaling')

    gridscale = Column(Float())
    aref = Column(Float())
    cref = Column(Float())
    sref = Column(Float())
    xyzref = Column(String(255))
    iperaxis = Column(Integer())


class SpaceTimeDiscretization(Base):
    """Bla."""

    __tablename__ = 'space_time_discretization'

    idx = Column(Integer(), primary_key=True)

    solver_setup_idx = Column(Integer(), ForeignKey('solver_setup.idx'))
    solver_setup = relationship("SolverSetup", back_populates='space_time_discretization')

    idistype = Column(Integer())
    mespace = Column(Integer())
    tuspace = Column(Integer())
    ischeme = Column(Integer())
    tuscheme = Column(Integer())


class SlipCuspUpwind(Base):
    """Bla."""

    __tablename__ = 'slip_cusp_upwind'

    idx = Column(Integer(), primary_key=True)

    solver_setup_idx = Column(Integer(), ForeignKey('solver_setup.idx'))
    solver_setup = relationship("SolverSetup", back_populates='slip_cusp_upwind')

    slipvisa = Column(Float())
    cuspfma = Column(Integer())
    musclord = Column(Integer())
    muscllim = Column(Integer())
    muscldel = Column(Float())
    musclka1 = Column(Float())
    musclka2 = Column(Float())
    ausmfps = Column(Float())
    ausmdvk = Column(Float())
    ldsdelta = Column(Float())


class BoundaryTreatment(Base):
    """Bla."""

    __tablename__ = 'boundary_treatment'

    idx = Column(Integer(), primary_key=True)

    solver_setup_idx = Column(Integer(), ForeignKey('solver_setup.idx'))
    solver_setup = relationship("SolverSetup", back_populates='boundary_treatment')

    bcv = Column(Integer())
    ifarfeul = Column(Integer())
    farfsmo = Column(Float())
    bcwall = Column(Integer())
    twall = Column(Float())
    iswall = Column(Integer())
    ihangcon = Column(Integer())
    iadheli = Column(Integer())
    iengine = Column(Integer())
    tolcut = Column(Float())
    ghostcut = Column(Integer())
    isingu = Column(Integer())


class TurbulenceModels(Base):
    """Bla."""

    __tablename__ = 'turbulence_models'

    idx = Column(Integer(), primary_key=True)

    solver_setup_idx = Column(Integer(), ForeignKey('solver_setup.idx'))
    solver_setup = relationship("SolverSetup", back_populates='turbulence_models')

    iturb = Column(Integer())
    oldturb = Column(Integer())
    itukwset = Column(Integer())
    walldist = Column(Integer())
    cwake = Column(Float())
    aplus = Column(Float())
    tusoundf = Column(Float())
    kinflu = Column(Integer())
    rltu = Column(Float())
    kprdlim = Column(Float())
    rtulf = Column(Float())
    srelax = Column(Float())
    itu1vort = Column(Integer())
    cb1 = Column(Float())
    cb2 = Column(Float())
    cv1 = Column(Float())
    sigspa = Column(Float())
    cw2 = Column(Float())
    cw3 = Column(Float())
    kappa = Column(Float())
    rltini = Column(Float())
    tu0 = Column(Float())
    tu0ini = Column(Float())
    bcturbkw = Column(Integer())
    bcturud = Column(Float())
    krplus = Column(Float())
    cmpcor = Column(Integer())
    ilimwk = Column(Integer())
    ituslim = Column(Integer())
    itu2vort = Column(Integer())
    itu27lin = Column(Integer())
    itu27dim = Column(Integer())
    pitimstp = Column(Integer())
    ituprof = Column(Integer())
    kicmax = Column(Float())
    sigka = Column(Float())
    sigka2 = Column(Float())
    sigep = Column(Float())
    sigep2 = Column(Float())
    cep1 = Column(Float())
    cep12 = Column(Float())
    cep2 = Column(Float())
    cep22 = Column(Float())
    cmutur = Column(Float())


class ReynoldsStressModels(Base):
    """Bla."""

    __tablename__ = 'reynolds_stress_models'

    idx = Column(Integer(), primary_key=True)

    solver_setup_idx = Column(Integer(), ForeignKey('solver_setup.idx'))
    solver_setup = relationship("SolverSetup", back_populates='reynolds_stress_models')

    irsmeq7 = Column(Integer())
    oldeq7 = Column(Integer())
    idifrsm = Column(Integer())
    idiflen = Column(Integer())
    irsmbcep = Column(Integer())
    irsmbcom = Column(Integer())
    cmursm = Column(Float())
    c10rsm = Column(Float())
    c11rsm = Column(Float())
    c2rsm = Column(Float())
    c3rsm = Column(Float())
    c4rsm = Column(Float())
    c1nlrsm = Column(Float())
    c2nlrsm = Column(Float())
    c1llr = Column(Float())
    c2llr = Column(Float())
    cdifrsm1 = Column(Float())
    cdifrsm2 = Column(Float())
    cdiflen1 = Column(Float())
    cdiflen2 = Column(Float())
    cep1rsm = Column(Float())
    cep12rsm = Column(Float())
    cep2rsm = Column(Float())
    cep22rsm = Column(Float())
    sigdrsm1 = Column(Float())
    sigdrsm2 = Column(Float())


class MultigridControl(Base):
    """Bla."""

    __tablename__ = 'multigrid_control'

    idx = Column(Integer(), primary_key=True)

    solver_setup_idx = Column(Integer(), ForeignKey('solver_setup.idx'))
    solver_setup = relationship("SolverSetup", back_populates='multigrid_control')

    level = Column(Integer())
    ngit = Column(String(255))
    istart = Column(Integer())
    maxlev = Column(Integer())
    maxlevtu = Column(Integer())
    itypc = Column(Integer())
    nend = Column(String(255))
    nstep = Column(String(255))
    epsc = Column(Float())
    iprolong = Column(Integer())
    dtvi = Column(Integer())
    ndum = Column(String(255))
    fcfl = Column(Float())
    ncycred = Column(Integer())


class RungeKuttaControl(Base):
    """Bla."""

    __tablename__ = 'runge_kutta_control'

    idx = Column(Integer(), primary_key=True)

    solver_setup_idx = Column(Integer(), ForeignKey('solver_setup.idx'))
    solver_setup = relationship("SolverSetup", back_populates='runge_kutta_control')
    grid_levels = relationship('GridLevelControl', back_populates='runge_kutta_control')

    levpar = Column(Integer())


class GridLevelControl(Base):
    """Bla."""

    __tablename__ = 'grid_level_control'

    idx = Column(Integer(), primary_key=True)

    runge_kutta_control_idx = Column(Integer(), ForeignKey('runge_kutta_control.idx'))
    runge_kutta_control = relationship("RungeKuttaControl", back_populates='grid_levels')
    # TODO Control these types
    cfl = Column(Float())
    cfltu = Column(Float())
    cfld = Column(Float())
    cfls = Column(Float())
    rvis2 = Column(Float())
    rvis4 = Column(Float())
    rvis0 = Column(Float())
    zeta = Column(Float())
    filtype = Column(Integer())
    hm = Column(Float())
    ismoo = Column(Integer())
    epsxyz = Column(String(255))
    epsmax = Column(Float())
    epsvcn = Column(String(255))
    egvlim = Column(String(255))
    nsrk = Column(Integer())
    ark = Column(String(255))
    qfils = Column(String(255))
    beta = Column(String(255))
    sms = Column(String(255))
