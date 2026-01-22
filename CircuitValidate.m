function []=CircuitValidate(Circuit,Icoil)

Schematic=Circuit.Schematic;
nCircuitNodes=Circuit.nCircuitNodes;
NodeCurrent=zeros(nCircuitNodes+1,1);
BranchCurrents=Circuit.BranchCurrents;
Icoil_branchlist=Circuit.Icoil_branchlist;

for i=1:length(Icoil)
    icoil=BranchCurrents(Icoil_branchlist(i));
    Err=icoil-Icoil(i);
    if abs(Err)>10^-6
        error('CircuitValidate: solution is not consistent');
    end
end

% for nBranch=1:length(Schematic)
%     Branch=Schematic{nBranch,1};
%     startnode=Branch.startnode+1;
%     endnode=Branch.endnode+1;
%     NodeCurrent(startnode,1)=NodeCurrent(startnode,1)+BranchCurrents(nBranch);
%     NodeCurrent(endnode,1)=NodeCurrent(endnode,1)-BranchCurrents(nBranch);
% end
% 
% for i=1:length(NodeCurrent)
%     if abs(NodeCurrent(i,1))>10^-4
%         error('CircuitValidate: at least one node current is not zero');
%     end
% end





