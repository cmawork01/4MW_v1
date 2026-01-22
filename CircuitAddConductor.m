function Branch = CircuitAddConductor(Branch,name,Subdomains,MaterialProperties,p,t,l,skew,nsubdomain,Cper,FEinclude)
% Add solid conductor with skin effect to the branch
% Do not call this function after calling CircuitCreate
component.name=name;
component.type='conductor';
component.value=conductor(Subdomains,MaterialProperties,p,t,l,skew,nsubdomain,Cper,FEinclude);
component.power=0;
Branch.Components=celladd(Branch.Components,component);