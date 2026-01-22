function Branch = CircuitAddE(Branch,name,data,Em,phi)
% Add voltage source to the branch
% Do not call this function after calling CircuitCreate
component.name=name; 
component.type='E';
component.power=0;
component.value.method='Supply'; 
component.value.data=data; 
component.value.actual=0;
component.value.actual_prev=0;
if nargin==5
    component.phasor.amplitude=Em;
    component.phasor.phase=phi;
else
    component.phasor.amplitude=[];
    component.phasor.phase=[];    
end
Branch.Components=celladd(Branch.Components,component);