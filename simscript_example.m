function [ShaftPosition, CircuitControl, Settings, Enforce, Userdata] = ...
          simscript_example(Outputs,Settings,Userdata,Circuit,Drive,Geometry,Mesh,Windings,A,cell_p,cell_t,cell_Nu,path)
% Example of simulation script function (should be used with circuit function InvertedCircuit.m)

% call default simulation script function for space vector PWM
[ShaftPosition, CircuitControl, Settings, Enforce, Userdata] = ...
          simscript_spacevecpwm(Outputs,Settings,Userdata,Circuit,Drive,Geometry,Mesh,Windings,A,cell_p,cell_t,cell_Nu,path);

% Current simulation time
if isempty(Outputs.time)
    CurrentTime = 0;
else
    CurrentTime = Outputs.time(end);
end
% Change time step if simulation time reaches 0.1 sec
if CurrentTime>0.1
    Settings.DF_timestep=10^-6;
else
    Settings.DF_timestep=10^-5;
end

% Save switching function for each phase in Userdata structure
if ~isfield(Userdata,'Switch_a')
    % Create fields 'Switch_a', 'Switch_b', 'Switch_c' in Userdata when 
    % simscript_example is called for the first time
    Userdata.Switch_a=[];
    Userdata.Switch_b=[];
    Userdata.Switch_c=[]; 
else
    % CircuitControl.switch_x1 - upper switch state
    if CircuitControl.switch_a1==1
        sA=1;
    else
        sA=-1;
    end
    if CircuitControl.switch_b1==1
        sB=1;
    else
        sB=-1;
    end
    if CircuitControl.switch_c1==1
        sC=1;
    else
        sC=-1;
    end
    % Collect switching function values for each time step
    Userdata.Switch_a=[Userdata.Switch_a sA];
    Userdata.Switch_b=[Userdata.Switch_b sB];
    Userdata.Switch_c=[Userdata.Switch_c sC]; 
end
