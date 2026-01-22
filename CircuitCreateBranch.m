function Branch = CircuitCreateBranch(startnode,endnode,circuittype)
% Construct circuit branch object
Branch.startnode=startnode; 
Branch.endnode=endnode; 
Branch.Components=cell(0,1);
if exist('circuittype','var')
    Branch.circuittype=circuittype;
else
    Branch.circuittype='statorcircuit';      % by default the branch belongs to the stator
end