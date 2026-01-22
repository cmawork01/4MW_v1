function [ShaftPosition, CircuitControl, Settings, Enforce, Userdata] = ...
          simscript_generic(Outputs,Settings,Userdata,Circuit,Drive,Geometry,Mesh,Windings,A,cell_p,cell_t,cell_Nu,path)
% Empty simulation script file

CircuitControl=[];
ShaftPosition=[];
% keep the same speed settings
if strcmp(Settings.DF_SpeedDependency,'Fixed speed simulation')
    Enforce.speed=2*pi*Settings.DF_Speed/60;
elseif strcmp(Settings.DF_SpeedDependency,'Variable speed simulation')
    Enforce=[];
end

