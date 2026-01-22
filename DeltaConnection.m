function Schematic = DeltaConnection(p,t,Subdomains,Circuit,l,nper,PowerSupplyType,AC_RMSSupplyValue)
% Construct electrical circuit with delta connected stator winding

Npp=Circuit.Npp;      % number of parallel paths
Rs=Circuit.Rs;
Rs = Npp*Rs;          % parallel path phase resistance
Lsew=Circuit.Lsew;
Lsew = Npp*Lsew;      % parallel path end winding inductance
layout = Circuit.layout;
if exist('AC_RMSSupplyValue','var')
    Em=sqrt(2)*AC_RMSSupplyValue; Im=sqrt(2)*AC_RMSSupplyValue;
else
    Em=[]; Im=[];
end

[ok_layout ok_Npp] = ValidateLayout(layout,Npp);
if ~ok_layout
    disp('ValidateLayout: desequencing of parallel path numbering');
    error(' ');
end
if ~ok_Npp
    disp('ValidateLayout: number of parallel paths is not consistent with winding layout table');
    error(' ');
end

Schematic = CircuitCreateSchematic();
if strcmp(PowerSupplyType,'3-phase voltage source')
    Branch = CircuitCreateBranch(0,1);
    Branch = CircuitAddE(Branch,'Ea','CircuitControl.va');
    Schematic = CircuitAddBranch(Schematic,Branch);

    Branch = CircuitCreateBranch(0,2);
    Branch = CircuitAddE(Branch,'Eb','CircuitControl.vb');
    Schematic = CircuitAddBranch(Schematic,Branch);

    Branch = CircuitCreateBranch(0,3);
    Branch = CircuitAddE(Branch,'Ec','CircuitControl.vc');
    Schematic = CircuitAddBranch(Schematic,Branch);

    for i=1:Npp
        Branch = CircuitCreateBranch(1,2);
        Branch = CircuitAddCoil(Branch,['coil_a' num2str(i)],'a',Subdomains,Rs,Lsew,i,Npp,1,p,t,l,nper);
        Schematic = CircuitAddBranch(Schematic,Branch);

        Branch = CircuitCreateBranch(2,3);
        Branch = CircuitAddCoil(Branch,['coil_b' num2str(i)],'b',Subdomains,Rs,Lsew,i,Npp,1,p,t,l,nper);
        Schematic = CircuitAddBranch(Schematic,Branch);

        Branch = CircuitCreateBranch(3,1);
        Branch = CircuitAddCoil(Branch,['coil_c' num2str(i)],'c',Subdomains,Rs,Lsew,i,Npp,1,p,t,l,nper);
        Schematic = CircuitAddBranch(Schematic,Branch);
    end
elseif strcmp(PowerSupplyType,'3-phase current source')
    Branch = CircuitCreateBranch(0,1);
    Branch = CircuitAddJ(Branch,'Ja','CircuitControl.ia');
    Schematic = CircuitAddBranch(Schematic,Branch);

    Branch = CircuitCreateBranch(0,2);
    Branch = CircuitAddJ(Branch,'Jb','CircuitControl.ib');
    Schematic = CircuitAddBranch(Schematic,Branch);

    Branch = CircuitCreateBranch(0,3);
    Branch = CircuitAddJ(Branch,'Jc','CircuitControl.ic');
    Schematic = CircuitAddBranch(Schematic,Branch);
   
    Branch = CircuitCreateBranch(0,1);
    Branch = CircuitAddR(Branch,'Rja',10^7);
    Schematic = CircuitAddBranch(Schematic,Branch);
    
    Branch = CircuitCreateBranch(0,2);
    Branch = CircuitAddR(Branch,'Rjb',10^7);
    Schematic = CircuitAddBranch(Schematic,Branch);
    
    Branch = CircuitCreateBranch(0,3);
    Branch = CircuitAddR(Branch,'Rjc',10^7);
    Schematic = CircuitAddBranch(Schematic,Branch);
    
    for i=1:Npp
        Branch = CircuitCreateBranch(1,2);
        Branch = CircuitAddCoil(Branch,['coil_a' num2str(i)],'a',Subdomains,Rs,Lsew,i,Npp,1,p,t,l,nper);
        Schematic = CircuitAddBranch(Schematic,Branch);

        Branch = CircuitCreateBranch(2,3);
        Branch = CircuitAddCoil(Branch,['coil_b' num2str(i)],'b',Subdomains,Rs,Lsew,i,Npp,1,p,t,l,nper);
        Schematic = CircuitAddBranch(Schematic,Branch);

        Branch = CircuitCreateBranch(3,1);
        Branch = CircuitAddCoil(Branch,['coil_c' num2str(i)],'c',Subdomains,Rs,Lsew,i,Npp,1,p,t,l,nper);
        Schematic = CircuitAddBranch(Schematic,Branch);
    end
else
    error(' ');
end