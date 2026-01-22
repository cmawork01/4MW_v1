function [PowerInput, Ps, Pr] = CircuitGetPower(Circuit)

PowerInput=0;
Ps=0;
Pr=0;
Schematic=Circuit.Schematic;
for nBranch=1:length(Schematic)
    Branch=Schematic{nBranch,1};
    Components=Branch.Components;
    P=0;
    for i=1:length(Components)
        component=Components{i,1};
        if strcmp(component.type,'E')
            PowerInput=PowerInput+component.power;
        elseif strcmp(component.type,'J')
            PowerInput=PowerInput+component.power;            
        elseif strcmp(component.type,'R')
            P=P+component.power;
        elseif strcmp(component.type,'L') 
            P=P+component.power;
        elseif strcmp(component.type,'C')
            P=P+component.power;
        elseif strcmp(component.type,'coil')
            P=P+component.power_R+component.power_Lsew;
        elseif strcmp(component.type,'conductor')
            P=P+component.power;
        elseif strcmp(component.type,'Switch')
            P=P+component.power;
        elseif strcmp(component.type,'Diode')
            P=P+component.power;
        else
            error('Undefined circuit component type')    
        end
    end 
    if strcmp(Branch.circuittype,'statorcircuit')
        Ps=Ps+P;
    elseif strcmp(Branch.circuittype,'rotorcircuit')
        Pr=Pr+P;
    end
end


