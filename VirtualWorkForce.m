function [Fx_slice, Fy_slice]=VirtualWorkForce(vd,cell_p,cell_t,cell_Nu,X,ip_rotor,l,nper,nSlices,motortype)

% Electromagnetic force calculation using Virtual work method 
% vd - virtual displacement    
Fx_slice=[];
Fy_slice=[];
if nper>1
    Fx_slice=zeros(nSlices,1);
    Fy_slice=zeros(nSlices,1);
    return;
end
for i=1:nSlices
    p=cell_p{i,1};
    t=cell_t{i,1};
    Nu=cell_Nu{i,1};
    np=size(p,2);    
    A_slice=X(1:np);
    X(1:np)=[];
    it1=t(1,:); it2=t(2,:); it3=t(3,:);
    [ar,g1x,g1y,g2x,g2y,g3x,g3y]=trgdata(p,t);
    K1=asmkk(it1,it2,it3,np,ar,g1x,g1y,g2x,g2y,g3x,g3y,Nu);    % stiffness matrix
    % rotor virtual displacement along axis x
    pp=p;
    px_rotor=p(1,ip_rotor);
    px_rotor=px_rotor+vd;
    pp(1,ip_rotor)=px_rotor;
%     for j=1:(AirGapSlidingLayer-1)
%         pp(1,ipSlidingLayerStator(j,:))=pp(1,ipSlidingLayerStator(j,:))+(j/nAirGapLayers)*vd*ones(1,size(ipSlidingLayerStator,2));
%     end
%     for j=1:(nAirGapLayers-AirGapSlidingLayer)
%         pp(1,ipSlidingLayerRotor(j,:))=pp(1,ipSlidingLayerRotor(j,:))-(j/nAirGapLayers)*vd*ones(1,size(ipSlidingLayerRotor,2));
%     end
    % calculation of the electromagnetic force along x-axis
    [ar,g1x,g1y,g2x,g2y,g3x,g3y]=trgdata(pp,t);
    K2x=asmkk(it1,it2,it3,np,ar,g1x,g1y,g2x,g2y,g3x,g3y,Nu);    % stiffness matrix
    dWx=0.5*(l/nSlices)*A_slice'*(K2x-K1)*A_slice;
    Fx_slice=[Fx_slice; -dWx/vd];
    % rotor virtual displacement along y-axis 
    pp=p;
    py_rotor=p(2,ip_rotor);
    py_rotor=py_rotor+vd;
    pp(2,ip_rotor)=py_rotor;
%     for j=1:(AirGapSlidingLayer-1)
%         pp(2,ipSlidingLayerStator(j,:))=pp(2,ipSlidingLayerStator(j,:))+(j/nAirGapLayers)*vd*ones(1,size(ipSlidingLayerStator,2));
%     end
%     for j=1:(nAirGapLayers-AirGapSlidingLayer)
%         pp(2,ipSlidingLayerRotor(j,:))=pp(2,ipSlidingLayerRotor(j,:))-(j/nAirGapLayers)*vd*ones(1,size(ipSlidingLayerRotor,2));
%     end
    % calculation of the electromagnetic force along axis y
    [ar,g1x,g1y,g2x,g2y,g3x,g3y]=trgdata(pp,t);
    K2y=asmkk(it1,it2,it3,np,ar,g1x,g1y,g2x,g2y,g3x,g3y,Nu);    % stiffness matrix
    dWy=0.5*(l/nSlices)*A_slice'*(K2y-K1)*A_slice;
    Fy_slice=[Fy_slice; -dWy/vd];
end
if strcmp(motortype,'Outer rotor') || strcmp(motortype,'outerrotor')
    Fx_slice=-Fx_slice;
    Fy_slice=-Fy_slice;
end





