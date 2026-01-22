function [cell_Nu_lin Kst]=getNu_lin(t,Subdomains,MaterialProperties,Nt,nSlices)
% Linear reluctivity

mu0 = 4*pi*(10.^(-7));                      % permeability of free space
nt=size(t,2);
Nu_lin=(1/mu0)*ones(1,nt);
Kst=ones(1,nt);                             % stacking factor, triangle distribution
for i=1:length(Subdomains)
    subdomain=Subdomains(i);
    material_index=subdomain.material_index;
    mu=MaterialProperties(material_index).mu;
    kst=subdomain.kst;
    it_sdm=find(t(4,:)==i);
    Nu_lin(it_sdm)=Nu_lin(it_sdm)/(kst*mu+1-kst);
    Kst(it_sdm)=kst;
end
cell_Nu_lin=cell(nSlices,1);
for i=1:nSlices
    cell_Nu_lin{i}=[Nu_lin (1/mu0)*ones(1,Nt-nt)];
end