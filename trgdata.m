function [ar,g1x,g1y,g2x,g2y,g3x,g3y]=trgdata(p,t)
% Mesh triangles geometry data.

% Triangle sides
r23x=p(1,t(3,:))-p(1,t(2,:));
r23y=p(2,t(3,:))-p(2,t(2,:));
r31x=p(1,t(1,:))-p(1,t(3,:));
r31y=p(2,t(1,:))-p(2,t(3,:));
r12x=p(1,t(2,:))-p(1,t(1,:));
r12y=p(2,t(2,:))-p(2,t(1,:));

% Triangle areas
ar=abs(r31x.*r23y-r31y.*r23x)/2;

if nargout>1,
    g1x=-0.5*r23y./ar;
    g1y=0.5*r23x./ar;
    g2x=-0.5*r31y./ar;
    g2y=0.5*r31x./ar;
    g3x=-0.5*r12y./ar;
    g3y=0.5*r12x./ar;
else
    g1x=[];
    g1y=[];
    g2x=[];
    g2y=[];
    g3x=[];
    g3y=[];  
end
