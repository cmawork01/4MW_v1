function [it_core, it_core_rotor, it_core_stator] = getitcore(t,Subdomains)
% indices of iron core triangles
it_core=[];
it_core_rotor=[];
it_core_stator=[];
for i_sdm=1:length(Subdomains)
    if strcmp(Subdomains(i_sdm).type,'core')
        it_sdm=find(t(4,:)==i_sdm);
        it_core=[it_core it_sdm];
        if strcmp(Subdomains(i_sdm).position,'rotor')
            it_core_rotor=it_sdm;
        elseif strcmp(Subdomains(i_sdm).position,'stator')
            it_core_stator=it_sdm;
        end
    end
end
