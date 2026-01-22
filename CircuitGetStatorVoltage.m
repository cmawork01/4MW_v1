function [vsa, vsb, vsc] = CircuitGetStatorVoltage(Circuit,delta_t)

Schematic=Circuit.Schematic;
BranchCurrents0=Circuit.BranchCurrents0;
BranchCurrents=Circuit.BranchCurrents;
iNaNBranchCurrents=isnan(BranchCurrents);
iNaNBranchCurrents=find(diff([0; iNaNBranchCurrents])==1);
iBranchCurrents=find(~isnan(BranchCurrents));
iBranchCurrents=sort([iBranchCurrents; iNaNBranchCurrents]);
BranchCurrents=BranchCurrents(iBranchCurrents);
BranchCurrents0=BranchCurrents0(iBranchCurrents);
for nBranch=1:length(Schematic)
    Branch=Schematic{nBranch,1};
    if strcmp(Branch.circuittype,'statorcircuit')
        Components=Branch.Components;
        for i=1:length(Components)
            component=Components{i,1};
            if strcmp(component.type,'coil')
                npath=component.value.npath;
                if strcmp(component.value.phase,'a')
                    vsa(npath,1)=BranchCurrents(nBranch)*component.value.R+(BranchCurrents(nBranch)-BranchCurrents0(nBranch))*component.value.Lsew/delta_t-component.EMFM;
                elseif strcmp(component.value.phase,'b')
                    vsb(npath,1)=BranchCurrents(nBranch)*component.value.R+(BranchCurrents(nBranch)-BranchCurrents0(nBranch))*component.value.Lsew/delta_t-component.EMFM;
                elseif strcmp(component.value.phase,'c')
                    vsc(npath,1)=BranchCurrents(nBranch)*component.value.R+(BranchCurrents(nBranch)-BranchCurrents0(nBranch))*component.value.Lsew/delta_t-component.EMFM;
                end
            end
        end
    end
end
