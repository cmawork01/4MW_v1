# Auto-generated from CircuitAddSwitch.m
# NOTE: This is a placeholder stub. Manual translation required.

from __future__ import annotations

"""
Original MATLAB source:

function Branch = CircuitAddSwitch(Branch,name,data,Roff,Ron)
% Add switch to the branch
% Do not call this function after calling CircuitCreate
component.name=name; 
component.type='Switch';
component.power=0;
component.value.method='Switch'; 
component.value.data=data; 
component.value.actual=Roff;
% component.value.actual_prev=0;
component.value.Roff=Roff;
component.value.Ron=Ron;
Branch.Components=celladd(Branch.Components,component);
"""

def CircuitAddSwitch(*args, **kwargs):
    """Placeholder for translated MATLAB function."""
    raise NotImplementedError(
        "This function requires manual translation from MATLAB."
    )
