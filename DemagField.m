function [DemagH_max, DemagHpercent_max] = DemagField(A,cell_p,cell_t,cell_BBr,cell_Nu,Subdomains,MaterialProperties,nSlices)
% DemagH_max - max. demagnetizing field
% DemagHpercent_max - max. demagnetizing field in percentage of intrinsic coercivity Hcj
DemagH_max=0;
DemagHpercent_max=0;
[cell_Bx, cell_By]=GetFluxDensity(A,cell_p,cell_t,nSlices);

for i=1:nSlices
    t=cell_t{i,1};
    Nu=cell_Nu{i,1};
    Br=cell_BBr{i,1};
    Brx=Br(1,:);
    Bry=Br(2,:);
    Bnmx=cell_Bx{i,1}-Brx;
    Bnmy=cell_By{i,1}-Bry;
%     Bx=cell_Bx{i,1};
%     By=cell_By{i,1}; 
    Hdemag=zeros(size(Bnmx));
    Hdemag_percent=zeros(size(Bnmx));
    for i_sdm=1:length(Subdomains)
        if strcmp(Subdomains(i_sdm).type,'magnet')
            it_sdm=find(t(4,:)==i_sdm);
            material=MaterialProperties(Subdomains(i_sdm).material_index);
            Hcj=material.PM_Hcj;
            bnmpj=(Bnmx(it_sdm).*Brx(it_sdm)+Bnmy(it_sdm).*Bry(it_sdm))./sqrt(Brx(it_sdm).^2+Bry(it_sdm).^2);  % projection of Bnm on Br
            Hdemag(it_sdm)=-bnmpj.*Nu(it_sdm);
            if ~isempty(Hcj)
                Hdemag_percent(it_sdm)=-bnmpj.*Nu(it_sdm)*100/Hcj;
            end
        end
    end
    DemagH_max=max([DemagH_max max(Hdemag)]);
    DemagHpercent_max=max([DemagHpercent_max max(Hdemag_percent)]);
end

