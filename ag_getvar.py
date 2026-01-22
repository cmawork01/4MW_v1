# Auto-generated from ag_getvar.m
# NOTE: This is a placeholder stub. Manual translation required.

from __future__ import annotations

"""
Original MATLAB source:

function [phi, y]=ag_getvar(A,cell_p,cell_t,l,nt_,ShaftPosition,iSlice,var,method,nper,periodicity)

p=cell_p{iSlice,1};
t=cell_t{iSlice,1};
mu0 = 4*pi*(10.^(-7));     % permeability of free space
xShaftPosition=ShaftPosition(1); yShaftPosition=ShaftPosition(2);

nt=size(t,2);
Np_slice=0;
for n=1:iSlice
    np_slice=size(cell_p{n},2);
    Np_slice=Np_slice+np_slice;
end
A_slice=A(Np_slice-np_slice+1:Np_slice);   % magnetic vector potential of iSlice
[Ax,Ay]=gradA(p,t,A_slice);
Bx=Ay;
By=-Ax;
itAirGapSlidingLayer=nt_+1:nt;     % indices of the air gap sliding layer triangles

% Air gap sliding layer flux density
Bx=Bx(:,itAirGapSlidingLayer);
By=By(:,itAirGapSlidingLayer);
% midpoint coordinates of the air gap sliding layer triangles
xm=p(1,t(1,itAirGapSlidingLayer))+((p(1,t(2,itAirGapSlidingLayer))+...
    p(1,t(3,itAirGapSlidingLayer)))/2-p(1,t(1,itAirGapSlidingLayer)))*2/3;
ym=p(2,t(1,itAirGapSlidingLayer))+((p(2,t(2,itAirGapSlidingLayer))+...
    p(2,t(3,itAirGapSlidingLayer)))/2-p(2,t(1,itAirGapSlidingLayer)))*2/3;
% midpoints radius vector
Rm=sqrt((xm-xShaftPosition/2).^2+(ym-yShaftPosition/2).^2); Rm=Rm';
% calculation by inner and outer integration paths
it_inner=1:(nt-nt_)/2;        % indices of the air gap sliding layer triangles belonging to the inner integration path
it_outer=(nt-nt_)/2+1:length(itAirGapSlidingLayer);

if nper>1       % if there are periodic/antiperiodic boundaries
    % tangential unit-vector:
    tx=ym([it_inner it_outer])./Rm([it_inner it_outer])';
    ty=-xm([it_inner it_outer])./Rm([it_inner it_outer])';
else
    xm_inner=xm(it_inner);
    dxm_inner=diff([xm_inner xm_inner(1)]);
    xm_outer=xm(it_outer);
    dxm_outer=diff([xm_outer xm_outer(1)]);
    ym_inner=ym(it_inner);
    dym_inner=diff([ym_inner ym_inner(1)]);
    ym_outer=ym(it_outer);
    dym_outer=diff([ym_outer ym_outer(1)]);
    dxm_inner_=[dxm_inner(end) dxm_inner]; dxm_inner_(end)=[];
    dxm_inner=(dxm_inner+dxm_inner_)/2;
    dxm_outer_=[dxm_outer(end) dxm_outer]; dxm_outer_(end)=[];
    dxm_outer=(dxm_outer+dxm_outer_)/2;
    dxm=[dxm_inner dxm_outer];
    dym_inner_=[dym_inner(end) dym_inner]; dym_inner_(end)=[];
    dym_inner=(dym_inner+dym_inner_)/2;
    dym_outer_=[dym_outer(end) dym_outer]; dym_outer_(end)=[];
    dym_outer=(dym_outer+dym_outer_)/2;
    dym=[dym_inner dym_outer];
    % tangential unit-vector:
    tx=dxm./sqrt(dxm.^2+dym.^2);
    ty=dym./sqrt(dxm.^2+dym.^2);
end
% normal unit-vector:
nx=-ty;
ny=tx;
% % normal unit-vector:
% nx=(xm-xShaftPosition/2)./Rm;
% ny=(ym-yShaftPosition/2)./Rm;
% % tangential unit-vector:
% tx=ny;
% ty=-nx;

% outer integration path:
phi_outer=atan2(ym(it_outer)-yShaftPosition/2,xm(it_outer)-xShaftPosition/2);
phi_outer_inds=[phi_outer' it_outer'];
phi_outer_inds=sortrows(phi_outer_inds,1);
phi_outer=phi_outer_inds(:,1);
it_outer=phi_outer_inds(:,2);
if nper>1       % if there are periodic/antiperiodic boundaries
    dphi_outer=abs(diff(phi_outer));
    dphi_outer=[dphi_outer; dphi_outer(1)];
else
    dphi_outer=abs(diff([phi_outer; phi_outer(1,:)]));
end
dphi_outer=abs(dphi_outer-sparse(find(dphi_outer>pi),1,ones(length(find(dphi_outer>pi)),1)*2*pi,length(dphi_outer),1));
% inner integration path:
phi_inner=atan2(ym(it_inner)-yShaftPosition/2,xm(it_inner)-xShaftPosition/2);
phi_inner_inds=[phi_inner' it_inner'];
phi_inner_inds=sortrows(phi_inner_inds,1);
phi_inner=phi_inner_inds(:,1);
it_inner=phi_inner_inds(:,2);
if nper>1       % if there are periodic/antiperiodic boundaries
    dphi_inner=abs(diff(phi_inner));
    dphi_inner=[dphi_inner; dphi_inner(1)];
else
    dphi_inner=abs(diff([phi_inner; phi_inner(1,:)]));
end
dphi_inner=abs(dphi_inner-sparse(find(dphi_inner>pi),1,ones(length(find(dphi_inner>pi)),1)*2*pi,length(dphi_inner),1));

if abs(max([dphi_outer; dphi_inner])/min([dphi_outer; dphi_inner]))>10
    if nper>1       % if there are periodic/antiperiodic boundaries
        RM=[cos(-2*pi/nper) sin(-2*pi/nper);
            -sin(-2*pi/nper) cos(-2*pi/nper)];      % clockwise rotation matrix
        cell_p{iSlice,1}=RM'*p;
        A=periodicity*A;
        [phi, y]=ag_getvar(A,cell_p,cell_t,l,nt_,ShaftPosition,iSlice,var,method,nper,periodicity);
        return
    end
end

% components of B
Bn=Bx.*nx+By.*ny; Bn=Bn';  % normal component of B in the air gap sliding layer
Bt=Bx.*tx+By.*ty; Bt=Bt';  % tangential component of B in the air gap sliding layer
switch var
    case 'Bm'
        % air gap flux density magnitude distribution
        [phi, y]=Beval(phi_inner,phi_outer,Bn(it_inner),Bn(it_outer),Bt(it_inner),Bt(it_outer),method,nper,periodicity);
    case 'Bn'
        % air gap flux density normal component distribution
        [phi, y]=Bneval(phi_inner,phi_outer,Bn(it_inner),Bn(it_outer),method,nper,periodicity);
    case 'Bt'
        % air gap flux density tangential component distribution
        [phi, y]=Bteval(phi_inner,phi_outer,Bt(it_inner),Bt(it_outer),method,nper,periodicity);        
    case 'flux'
        % air gap magnetic flux distribution evaluation
        [phi, y]=fluxeval(phi_inner,phi_outer,dphi_inner,dphi_outer,Bn(it_inner),Bn(it_outer),Rm(it_inner),Rm(it_outer),l,method,nper,periodicity);
    case 'mmf'
        % air gap magnetomotive force distribution
        [phi, y]=mmfeval(phi_inner,phi_outer,dphi_inner,dphi_outer,Bt(it_inner),Bt(it_outer),Rm(it_inner),Rm(it_outer),method,nper,periodicity);
    case 'Fn'
        % air gap normal (radial) force distribution
        [phi, y]=Fneval(phi_inner,phi_outer,dphi_inner,dphi_outer,Bn(it_inner),Bn(it_outer),Bt(it_inner),Bt(it_outer),Rm(it_inner),Rm(it_outer),l,method,nper,periodicity);
end


function [phi, mmf]=mmfeval(phi_inner,phi_outer,dphi_inner,dphi_outer,Bt_inner,Bt_outer,Rm_inner,Rm_outer,method,nper,periodicity)
% air gap magnetomotive force distribution evaluation

mu0 = 4*pi*(10.^(-7));     % permeability of free space
mmf_outer=Bt_outer.*Rm_outer.*dphi_outer/mu0;
mmf_inner=Bt_inner.*Rm_inner.*dphi_inner/mu0;
sum_mmf_outer=sum(mmf_outer);              % must be zero
sum_mmf_inner=sum(mmf_inner);              % must be zero
[phi, mmf] = averagecurve(phi_inner,phi_outer,mmf_inner,mmf_outer,method,nper,periodicity);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


function [phi, flux]=fluxeval(phi_inner,phi_outer,dphi_inner,dphi_outer,Bn_inner,Bn_outer,Rm_inner,Rm_outer,l,method,nper,periodicity)
% air gap magnetic flux distribution evaluation

dphi_inner_=[dphi_inner(end); dphi_inner];    
dphi_inner_(end)=[];
dphi_inner=(dphi_inner+dphi_inner_)/2;

dphi_outer_=[dphi_outer(end); dphi_outer];    
dphi_outer_(end)=[];
dphi_outer=(dphi_outer+dphi_outer_)/2;

flux_inner=l*Bn_inner.*Rm_inner.*dphi_inner;
flux_outer=l*Bn_outer.*Rm_outer.*dphi_outer;
sum_flux_inner=sum(flux_inner);              % must be zero
sum_flux_outer=sum(flux_outer);              % must be zero
[phi, flux] = averagecurve(phi_inner,phi_outer,flux_inner,flux_outer,method,nper,periodicity);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


function [phi, B]=Beval(phi_inner,phi_outer,Bn_inner,Bn_outer,Bt_inner,Bt_outer,method,nper,periodicity)
% air gap flux density magnitude distribution evaluation

[phi, Bn] = averagecurve(phi_inner,phi_outer,Bn_inner,Bn_outer,method,nper,periodicity);
[phi, Bt] = averagecurve(phi_inner,phi_outer,Bt_inner,Bt_outer,method,nper,periodicity);
B=sqrt(Bn.^2+Bt.^2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


function [phi, Bn]=Bneval(phi_inner,phi_outer,Bn_inner,Bn_outer,method,nper,periodicity)
% air gap flux density normal component distribution evaluation

[phi, Bn] = averagecurve(phi_inner,phi_outer,Bn_inner,Bn_outer,method,nper,periodicity);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


function [phi, Bt]=Bteval(phi_inner,phi_outer,Bt_inner,Bt_outer,method,nper,periodicity)
% air gap flux density tangential component distribution evaluation

[phi, Bt] = averagecurve(phi_inner,phi_outer,Bt_inner,Bt_outer,method,nper,periodicity);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


function [phi, Fn]=Fneval(phi_inner,phi_outer,dphi_inner,dphi_outer,Bn_inner,Bn_outer,Bt_inner,Bt_outer,Rm_inner,Rm_outer,l,method,nper,periodicity)
% air gap normal (radial) force distribution evaluation

mu0 = 4*pi*(10.^(-7));     % permeability of free space
% Fn_inner=l*(Bn_inner.^2-Bt_inner.^2).*Rm_inner.*dphi_inner/(2*mu0);
% Fn_outer=l*(Bn_outer.^2-Bt_outer.^2).*Rm_outer.*dphi_outer/(2*mu0);
% [phi, Fn_test] = averagecurve(phi_inner,phi_outer,Fn_inner,Fn_outer,method,nper,periodicity);

[~, Rm_dphi] = averagecurve(phi_inner,phi_outer,Rm_inner.*dphi_inner,Rm_outer.*dphi_outer,method,nper,periodicity);
[~, Bn] = averagecurve(phi_inner,phi_outer,Bn_inner,Bn_outer,method,nper,periodicity);
[phi, Bt] = averagecurve(phi_inner,phi_outer,Bt_inner,Bt_outer,method,nper,periodicity);
Fn=l*(Bn.^2-Bt.^2).*abs(Rm_dphi)/(2*mu0);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


function [phi, y] = averagecurve(phi_inner,phi_outer,y_inner,y_outer,method,nper,periodicity)
if nper>1       % if there are periodic/antiperiodic boundaries
    dphi_inner=diff(phi_inner); dphi_inner=dphi_inner(1);
    dphi_outer=diff(phi_outer); dphi_outer=dphi_outer(1);    
    y_inner=full(y_inner);
    y_outer=full(y_outer);
    if strcmp(method,'Linear')
        yint_inner = interp1([phi_inner(1)-dphi_inner; phi_inner; phi_inner(end)+dphi_inner],[periodicity*y_inner(end); y_inner; periodicity*y_inner(1)],phi_outer);
        yint_outer = interp1([phi_outer(1)-dphi_outer; phi_outer; phi_outer(end)+dphi_outer],[periodicity*y_outer(end); y_outer; periodicity*y_outer(1)],phi_inner);
    elseif strcmp(method,'Spline')
        yint_inner = Spline([phi_inner(1)-dphi_inner; phi_inner; phi_inner(end)+dphi_inner],[periodicity*y_inner(end); y_inner; periodicity*y_inner(1)],phi_outer);
        yint_outer = Spline([phi_outer(1)-dphi_outer; phi_outer; phi_outer(end)+dphi_outer],[periodicity*y_outer(end); y_outer; periodicity*y_outer(1)],phi_inner);
    else
        error('Undefined interpolation method');
    end    
else
    if strcmp(method,'Linear')
        yint_inner = interp1([phi_inner(end)-2*pi; phi_inner; phi_inner(1)+2*pi],[y_inner(end); y_inner; y_inner(1)],phi_outer);
        yint_outer = interp1([phi_outer(end)-2*pi; phi_outer; phi_outer(1)+2*pi],[y_outer(end); y_outer; y_outer(1)],phi_inner);
    elseif strcmp(method,'Spline')
        yint_inner = Spline([phi_inner(end)-2*pi; phi_inner; phi_inner(1)+2*pi],[y_inner(end); y_inner; y_inner(1)],phi_outer);
        yint_outer = Spline([phi_outer(end)-2*pi; phi_outer; phi_outer(1)+2*pi],[y_outer(end); y_outer; y_outer(1)],phi_inner);
    else
        error('Undefined interpolation method');
    end
end
y1=(y_inner+yint_outer)/2;
y2=(y_outer+yint_inner)/2;

y_phi=[y1 phi_inner;
       y2 phi_outer];
y_phi=sortrows(y_phi,2);
y=y_phi(:,1);
phi=y_phi(:,2);
if nper>1       % if there are periodic/antiperiodic boundaries
    y_full=y;
    phi_full=phi;
    iter=1;
    while 1
        phi_full=[phi-iter*2*pi/nper; phi_full];
        y_full=[(periodicity^iter)*y; y_full];
        if phi_full(1)<-pi
            ind=find(phi_full<-pi,1,'last');
            phi_full(1:ind)=[];
            y_full(1:ind)=[];
            break;
        end
        iter=iter+1;
    end
    iter=1;
    while 1
        phi_full=[phi_full; phi+iter*2*pi/nper];
        y_full=[y_full; (periodicity^iter)*y];
        if phi_full(end)>pi
            ind=find(phi_full>pi,1,'first');
            phi_full(ind:end)=[];
            y_full(ind:end)=[];
            break;
        end
        iter=iter+1;
    end
    y=y_full;
    phi=phi_full;
end

"""

def ag_getvar(*args, **kwargs):
    """Placeholder for translated MATLAB function."""
    raise NotImplementedError(
        "This function requires manual translation from MATLAB."
    )
