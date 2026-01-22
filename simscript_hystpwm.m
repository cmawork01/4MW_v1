function [ShaftPosition, CircuitControl, Settings, Enforce, Userdata] = ...
          simscript_hystpwm(Outputs,Settings,Userdata,Circuit,Drive,Geometry,Mesh,Windings,A,cell_p,cell_t,cell_Nu,path)
% Simulation script file to be used with function InvertedCircuit.m
% Current hysteresis PWM

Isrms=Settings.DF_Isrms;
Vdc=Drive.Vdc;
Is_hyst=Isrms*Drive.Is_hyst_perc/100;
% Ia, Ib, Ic - motor phase currents
if isempty(Outputs.Rotang)
    rotang=Userdata.rotang;
    Ia=Userdata.Ia;
    Ib=Userdata.Ib;
    Ic=Userdata.Ic;
else
    rotang=Outputs.Rotang(end);
    Ia=sum(Outputs.Ia(:,end));
    Ib=sum(Outputs.Ib(:,end));
    Ic=sum(Outputs.Ic(:,end));
end
gamma0=Outputs.gamma0; 
nPolePairs=Outputs.nPolePairs;
if isfield(Userdata,'CircuitControl')
    CircuitControl=Userdata.CircuitControl;
else
    % Supply (line) currents:
    if strcmp(Windings.statorcircuit,'StarConnection')
        Iasupply=Ia;
        Ibsupply=Ib;
        Icsupply=Ic;
    elseif strcmp(Windings.statorcircuit,'DeltaConnection')
        Iasupply=Ia-Ic;
        Ibsupply=Ib-Ia;
        Icsupply=Ic-Ib;
    end
    % initial state
    if Iasupply>0
        CircuitControl.switch_a1=1;
        CircuitControl.switch_a2=0;
    else
        CircuitControl.switch_a1=0;
        CircuitControl.switch_a2=1;
    end
    if Ibsupply>0
        CircuitControl.switch_b1=1;
        CircuitControl.switch_b2=0;
    else
        CircuitControl.switch_b1=0;
        CircuitControl.switch_b2=1;
    end
    if Icsupply>0
        CircuitControl.switch_c1=1;
        CircuitControl.switch_c2=0;
    else
        CircuitControl.switch_c1=0;
        CircuitControl.switch_c2=1;
    end
end
CircuitControl.vdc=Vdc; 

% Isrms - supply current
% Irms_phase - motor phase current
if strcmp(Windings.statorcircuit,'StarConnection')
    Irms_phase=Isrms;
elseif strcmp(Windings.statorcircuit,'DeltaConnection')
    Irms_phase=Isrms/sqrt(3);   % supply current is line current
end
gamma_ref=Settings.DF_Gamma*pi/180;
% Motor phase current reference:
Ia_ref=Irms_phase*sqrt(2)*sin(rotang*nPolePairs-gamma0+gamma_ref);
Ib_ref=Irms_phase*sqrt(2)*sin(rotang*nPolePairs+2*pi/3-gamma0+gamma_ref);
Ic_ref=Irms_phase*sqrt(2)*sin(rotang*nPolePairs+4*pi/3-gamma0+gamma_ref);
% Inverter current (supply current) reference:
if strcmp(Windings.statorcircuit,'StarConnection')
    Iai_ref=Ia_ref;
    Ibi_ref=Ib_ref;
    Ici_ref=Ic_ref;
elseif strcmp(Windings.statorcircuit,'DeltaConnection')
    % Inverter current is line current
    Iai_ref=Ia_ref-Ic_ref;
    Ibi_ref=Ib_ref-Ia_ref;
    Ici_ref=Ic_ref-Ib_ref;
end
Iai_ref_upper=Iai_ref+Is_hyst/2;
Iai_ref_lower=Iai_ref-Is_hyst/2;
Ibi_ref_upper=Ibi_ref+Is_hyst/2;
Ibi_ref_lower=Ibi_ref-Is_hyst/2;
Ici_ref_upper=Ici_ref+Is_hyst/2;
Ici_ref_lower=Ici_ref-Is_hyst/2;
% Supply currents:
if strcmp(Windings.statorcircuit,'StarConnection')
    Iasupply=Ia;
    Ibsupply=Ib;
    Icsupply=Ic;
elseif strcmp(Windings.statorcircuit,'DeltaConnection')
    Iasupply=Ia-Ic;
    Ibsupply=Ib-Ia;
    Icsupply=Ic-Ib;
end
if Iasupply<=Iai_ref_lower
    CircuitControl.switch_a1=1;
    CircuitControl.switch_a2=0;
elseif Iasupply>=Iai_ref_upper
    CircuitControl.switch_a1=0;
    CircuitControl.switch_a2=1; 
end
if Ibsupply<=Ibi_ref_lower
    CircuitControl.switch_b1=1;
    CircuitControl.switch_b2=0; 
elseif Ibsupply>=Ibi_ref_upper
    CircuitControl.switch_b1=0;
    CircuitControl.switch_b2=1;  
end
if Icsupply<=Ici_ref_lower
    CircuitControl.switch_c1=1;
    CircuitControl.switch_c2=0; 
elseif Icsupply>=Ici_ref_upper
    CircuitControl.switch_c1=0;
    CircuitControl.switch_c2=1;  
end
Userdata.CircuitControl=CircuitControl;

ShaftPosition=[];
% keep the same speed settings
if strcmp(Settings.DF_SpeedDependency,'Fixed speed simulation')
    Enforce.speed=2*pi*Settings.DF_Speed/60;
elseif strcmp(Settings.DF_SpeedDependency,'Variable speed simulation')
    Enforce=[];
end

