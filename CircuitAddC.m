function Branch = CircuitAddC(Branch,name,value,Vinit)
% Add capacity to the branch
% Do not call this function after calling CircuitCreate
% Uinit - initial capacitor voltage
if nargin==3, Vinit=0; end
component.name=name; 
component.type='C';
component.value.actual=value;
component.power=0;
component.V=Vinit;
% component.Vprev=0;
Branch.Components=celladd(Branch.Components,component);