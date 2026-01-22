# Auto-generated from CircuitGetVoltage.m
# NOTE: This is a placeholder stub. Manual translation required.

from __future__ import annotations

"""
Original MATLAB source:

function V = CircuitGetVoltage(Circuit,node1,node2)
% return voltage between node1 and node2

Phi=Circuit.Phi;
if node1==0
    V=-Phi(node2);
elseif node2==0
    V=Phi(node1);
else
    V=Phi(node1)-Phi(node2);
end
"""

def CircuitGetVoltage(*args, **kwargs):
    """Placeholder for translated MATLAB function."""
    raise NotImplementedError(
        "This function requires manual translation from MATLAB."
    )
