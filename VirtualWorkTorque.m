function [Torque Torque_slice]=VirtualWorkTorque(vad,cell_p,cell_t,cell_b,cell_Nu,X,ip_rotor,l,nper,nSlices,ShaftPosition,motortype)
% Electromagnetic torque calculation using Virtual work method 
% vad - virtual angular displacement
xShaftPosition=ShaftPosition(1); yShaftPosition=ShaftPosition(2);
Torque_slice=[];
for i=1:nSlices
    p=cell_p{i,1};
    t=cell_t{i,1};
    b=cell_b{i,1};
    Nu=cell_Nu{i,1};
    np=size(p,2);    
    A_slice=X(1:np);
    X(1:np)=[];
    it1=t(1,:); it2=t(2,:); it3=t(3,:);
    [ar,g1x,g1y,g2x,g2y,g3x,g3y]=trgdata(p,t);
    K1=asmkk(it1,it2,it3,np,ar,g1x,g1y,g2x,g2y,g3x,g3y,Nu);    % stiffness matrix
    % rotor virtual rotation
    pp=p;
    p_rotor=p(:,ip_rotor);
%     RM=[cos(-vad) sin(-vad);
%         -sin(-vad) cos(-vad)];   
    % rotation matrix
    RM=[cos(vad)+(1-cos(vad))*xShaftPosition^2               (1-cos(vad))*xShaftPosition*yShaftPosition-sin(vad);
        (1-cos(vad))*xShaftPosition*yShaftPosition+sin(vad)  cos(vad)+(1-cos(vad))*yShaftPosition^2];
    p_rotor=RM'*p_rotor;
    pp(:,ip_rotor)=p_rotor; 
    % calculation of the electromagnetic torque
    [ar,g1x,g1y,g2x,g2y,g3x,g3y]=trgdata(pp,t);
    K2=asmkk(it1,it2,it3,np,ar,g1x,g1y,g2x,g2y,g3x,g3y,Nu);    % stiffness matrix
    dWv=0.5*nper*(l/nSlices)*A_slice'*(K2-K1)*A_slice;    % virtual energy difference
    Tvw=-dWv/vad;
    Torque_slice=[Torque_slice; Tvw];
end
if strcmp(motortype,'Outer rotor') || strcmp(motortype,'outerrotor')
    Torque_slice=-Torque_slice;
end
Torque=sum(Torque_slice);
