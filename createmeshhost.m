function [p,e,t] = createmeshhost(g,Geometry,lag,nAirGapLayers,agmeshqlt,Hgrad)

save('meshdata.mat','g','Geometry','lag','nAirGapLayers','agmeshqlt','Hgrad');
!createmesh.exe
load('meshdata.mat','p','e','t');
delete('meshdata.mat');