function Branch = CircuitAddCoil(Branch,name,phase,Subdomains,R,Lsew,npath,Npp,coilorientation,p,t,l,nper)
% Add coil to the branch
% Do not call this function after calling CircuitCreate
component.name=name;
component.type='coil';
component.value=coil(phase,Subdomains,R,Lsew,npath,Npp,coilorientation,p,t,l,nper);
component.power_R=0;
component.power_Lsew=0;
component.EMFM=0;
Branch.Components=celladd(Branch.Components,component);