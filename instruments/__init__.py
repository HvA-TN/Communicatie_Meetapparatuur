"""
Publieke interface voor instrument-drivers.

Exporteert de belangrijkste klassen en biedt een simpele factory
op basis van *IDN?* zodat gebruikers niet hoeven te weten welk
concrete driver-class bij een instrument hoort.
"""

from .rigol_dg1022 import RigolDG1022
from .rigol_dm3058e import RigolDM3058E

__all__ = ["RigolDG1022", "RigolDM3058E", "open_instrument"]
