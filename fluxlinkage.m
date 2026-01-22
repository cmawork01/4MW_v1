function FluxLinkage = fluxlinkage(phase,cell_p,cell_t,A,Geometry,Windings,Mesh,Circuit)
% stator winding fluxlinkage

Ns=Geometry.Ns;            % number of stator slots
l=Geometry.l*10^-3;        % lamination length
Npp=Windings.Npp;          % number of parallel paths
Ws=Windings.W;             % number of conductors per slot
nSlices=Mesh.nSlices;      % number of slices
nper = VerifyPerBndCnd(Ns,Mesh.nPolePairs,Mesh.perbndcnd);

nt=size(cell_t{1,1},2);
di=zeros(nt,1);
mtx_EMFMt_coil=zeros(1,nt);
if strcmp(phase,'a') || strcmp(phase,'b') || strcmp(phase,'c')
    Schematic=Circuit.Schematic;
    for nBranch=1:length(Schematic)
        Branch=Schematic{nBranch,1};
        Components=Branch.Components;
        for i=1:length(Components)
            component=Components{i,1};
            if strcmp(component.type,'coil')
                if strcmp(component.value.phase,phase)
                    di_=component.value.di;
                    inds=find(di_);
                    di(inds)=di_(inds);                    
                    mtx_EMFMt_coil_=component.value.mtx_EMFMt_coil;
                    inds=find(mtx_EMFMt_coil_);
                    mtx_EMFMt_coil(inds)=mtx_EMFMt_coil_(inds);
                end        
            end
        end
    end
else
    error('Phase must be one of ''a''|''b''|''c''')
end
    
% average fluxlinkage over all slices
FluxLinkage=0;
Np=0;
for iSlice=1:nSlices
    p=cell_p{iSlice,1};
    t=cell_t{iSlice,1};
    np=size(p,2);
    Ap=A(Np+1:Np+np);
    At=intrp(p,t,Ap);
    ar=trgdata(p,t);
    Np=Np+np;
    FluxLinkage=FluxLinkage+At.*di'*ar';
end
FluxLinkage=FluxLinkage/nSlices;

it_phase=find(di);
Sss=3*sum(ar(it_phase))/(Ns/nper);                        % stator slot area

FluxLinkage=(l*Ws/Sss)*FluxLinkage;
FluxLinkage=FluxLinkage*nper/Npp;
FluxLinkage_test=mtx_EMFMt_coil*At';


function ut=intrp(p,t,un)

np=size(p,2);
nt=size(t,2);

if size(un,2)==1
  N=size(un,1)/np;
  un=reshape(un,np,N);
end

A=sparse(ones(3,1)*(1:nt),t(1:3,:),1,nt,np);
B=sparse(1:nt,1:nt,1./sum(A.'),nt,nt);
ut=(B*A*un).';











