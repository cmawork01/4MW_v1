function Branch = CircuitAddDiode(Branch,name,Roff,Ron,direction)
% Add ideal diode to the branch
% Do not call this function after calling CircuitCreate
% Ron, Roff - forward and backward resistance
% direction=1 - forward direction of the diode corresponds to positive current
% direction=-1 - backward direction of the diode corresponds to negative current

component.name=name; 
component.type='Diode';
component.power=0;
component.value.method='Diode'; 
component.value.data=0;      % state is off
component.value.actual=Roff;
% component.value.actual_prev=0;
component.value.Roff=Roff;
component.value.Ron=Ron;
component.value.direction=direction;       
Branch.Components=celladd(Branch.Components,component);