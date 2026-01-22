function Branch = CircuitAddR(Branch,name,value)
% Add resistance to the branch
% Do not call this function after calling CircuitCreate
component.name=name; 
component.type='R';
component.value.actual=value;
component.power=0;
% component.V=0;
% component.Vprev=0;
Branch.Components=celladd(Branch.Components,component);