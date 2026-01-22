# Auto-generated from simscript_spacevecpwm.m
# NOTE: This is a placeholder stub. Manual translation required.

from __future__ import annotations

"""
Original MATLAB source:

function [ShaftPosition, CircuitControl, Settings, Enforce, Userdata] = ...
          simscript_spacevecpwm(Outputs,Settings,Userdata,Circuit,Drive,Geometry,Mesh,Windings,A,cell_p,cell_t,cell_Nu,path)
% Simulation script file to be used with function InvertedCircuit.m
% Three phase space vector pulse width modulation

if isfield(Userdata,'FOC')
    FOC=Userdata.FOC;
    Kpc_d=FOC.Kpc_d;
    Kpc_q=FOC.Kpc_q;
    Kic=FOC.Kic;
    Ld_ffc=FOC.Ld_ffc;
    Lq_ffc=FOC.Lq_ffc;
    fluxlinkage_md_ffc=FOC.fluxlinkage_md_ffc;
    OPic_d=FOC.OPic_d;
    OPic_q=FOC.OPic_q;
    Vd_ref=FOC.Vd_ref;
    Vq_ref=FOC.Vq_ref;
    Vd_ref_=FOC.Vd_ref_;
    Vq_ref_=FOC.Vq_ref_;
else
    error('No field oriented control parameters found. Change drive type to ''Space vector PWM''')
end

Vdc=Drive.Vdc;
fspwm=Drive.fspwm;
if isempty(Outputs.Rotang)
    rotang=Userdata.rotang;
    Id=Userdata.Id;
    Iq=Userdata.Iq;
    speed=Userdata.speed;    
else
    rotang=Outputs.Rotang(end);
    Id=Outputs.Id(end);
    Iq=Outputs.Iq(end);
    speed=Outputs.Speed(end);
end
CurrentTime = Outputs.CurrentTime;
gamma0=Outputs.gamma0; 
nPolePairs=Outputs.nPolePairs;
CircuitControl.vdc=Vdc; 
Isrms=Settings.DF_Isrms;
delta_t=Settings.DF_timestep;
phi=rotang*nPolePairs-gamma0;
DQconvert=[-cos(phi) -cos(phi+2*pi/3) -cos(phi+4*pi/3); sin(phi) sin(phi+2*pi/3) sin(phi+4*pi/3)]*2/3;   
ma0=sqrt(3)/2;                                    % maximum modulation index
% Isrms - supply current
% Irms_phase - motor phase current
if strcmp(Windings.statorcircuit,'StarConnection')
    Vrms_phase_max=(2/3)*ma0*Vdc/sqrt(2);         % equals to max rms inverter phase voltage
    Irms_phase=Isrms;
elseif strcmp(Windings.statorcircuit,'DeltaConnection')
    Vrms_phase_max=(2/3)*ma0*Vdc/sqrt(2)*sqrt(3); % equals to max rms inverter line to line voltage
    Irms_phase=Isrms/sqrt(3);                     % supply current is line current
end

% field oriented control
gamma_ref=Settings.DF_Gamma*pi/180;
Ia_ref=Irms_phase*sqrt(2)*sin(rotang*nPolePairs-gamma0+gamma_ref);
Ib_ref=Irms_phase*sqrt(2)*sin(rotang*nPolePairs+2*pi/3-gamma0+gamma_ref);
Ic_ref=Irms_phase*sqrt(2)*sin(rotang*nPolePairs+4*pi/3-gamma0+gamma_ref);
idq_ref=DQconvert*[Ia_ref; Ib_ref; Ic_ref];
% Current reference
Id_ref=idq_ref(1); Iq_ref=idq_ref(2);
% Current errors:
Id_err=Id_ref-Id;
Iq_err=Iq_ref-Iq;
% Current integr. ouputs:
OPic_d=OPic_d+(Id_err+(Vd_ref-Vd_ref_)/Kpc_d)*delta_t;
OPic_q=OPic_q+(Iq_err+(Vq_ref-Vq_ref_)/Kpc_q)*delta_t;
% Feedforward voltage compensation:
Vd_ffc=-speed*Lq_ffc*Iq;
Vq_ffc=speed*(Ld_ffc*Id+fluxlinkage_md_ffc);
% Current PI reg. voltage outputs:
Vd_ref=OPic_d*Kic+Kpc_d*Id_err+Vd_ffc;
Vq_ref=OPic_q*Kic+Kpc_q*Iq_err+Vq_ffc;
Vd_ref_=Vd_ref; Vq_ref_=Vq_ref;
% Voltage limiter
if sqrt(Vd_ref^2+Vq_ref^2)/sqrt(2)>Vrms_phase_max
    Vd_ref=Vd_ref*sqrt(2*Vrms_phase_max^2/(Vd_ref_^2+Vq_ref_^2));
    Vq_ref=Vq_ref*sqrt(2*Vrms_phase_max^2/(Vd_ref_^2+Vq_ref_^2));
end
Vabc=[DQconvert; [1 1 1]]\[Vd_ref; Vq_ref; 0];
% Motor phase voltage reference:
Va_ref=Vabc(1); Vb_ref=Vabc(2); Vc_ref=Vabc(3);
% Inverter phase voltage reference:
if strcmp(Windings.statorcircuit,'StarConnection')
    % Motor phase voltage is inverter phase voltage
    Vai_ref=Va_ref; Vbi_ref=Vb_ref; Vci_ref=Vc_ref;
elseif strcmp(Windings.statorcircuit,'DeltaConnection')
    % Motor phase voltage is inverter line-to-line voltage
    Vai_ref=Va_ref/3-Vc_ref/3;
    Vbi_ref=Vb_ref/3-Va_ref/3;
    Vci_ref=Vc_ref/3-Vb_ref/3;
end
[sA,sB,sC] = spacevecpwm(Vai_ref,Vbi_ref,Vci_ref,fspwm,CurrentTime,Vdc);
if sA==1
    CircuitControl.switch_a1=1;
    CircuitControl.switch_a2=0;
else  % sA==-1
    CircuitControl.switch_a1=0;
    CircuitControl.switch_a2=1;  
end
if sB==1
    CircuitControl.switch_b1=1;
    CircuitControl.switch_b2=0; 
else  % sB==-1
    CircuitControl.switch_b1=0;
    CircuitControl.switch_b2=1;  
end
if sC==1
    CircuitControl.switch_c1=1;
    CircuitControl.switch_c2=0;  
else  % sC==-1
    CircuitControl.switch_c1=0;
    CircuitControl.switch_c2=1;   
end
FOC.OPic_d=OPic_d;
FOC.OPic_q=OPic_q;
FOC.Vd_ref=Vd_ref;
FOC.Vq_ref=Vq_ref;
FOC.Vd_ref_=Vd_ref_;
FOC.Vq_ref_=Vq_ref_;
Userdata.FOC=FOC;

ShaftPosition=[];
% keep the same speed settings
if strcmp(Settings.DF_SpeedDependency,'Fixed speed simulation')
    Enforce.speed=2*pi*Settings.DF_Speed/60;
elseif strcmp(Settings.DF_SpeedDependency,'Variable speed simulation')
    Enforce=[];
end


"""

def main():
    """Placeholder for translated MATLAB script."""
    raise NotImplementedError(
        "This script requires manual translation from MATLAB."
    )
