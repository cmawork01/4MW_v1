function [cell_Bx cell_By]=GetFluxDensity(X,cell_p,cell_t,nSlices)
% flux density vector components for every slice
cell_Bx=cell(nSlices,1);
cell_By=cell(nSlices,1);
for i=1:nSlices
    p_slice=cell_p{i,1};
    t_slice=cell_t{i,1};
    np=size(p_slice,2);
    if ~isempty(X)
        A_slice=X(1:np);
        X(1:np)=[];
    else
        A_slice=zeros(np,1);
    end
    [Ax Ay]=gradA(p_slice,t_slice,A_slice);
    cell_Bx{i,1}=Ay;
    cell_By{i,1}=-Ax;
end