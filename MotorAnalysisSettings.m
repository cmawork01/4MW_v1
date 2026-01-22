function output = MotorAnalysisSettings(par)

% Nonlinear solver settings
substepmax = 40;                % Maximum number of Newton algorithm iterations
relaxmin = 10^(-8);             % Minimum relaxation factor
convreport = 'on';  %'off' | 'on'    % Display convergence information in Matlab Command Window
NonconvHnd = 2;                 % Nonconvergence handling
                                % 1 - ignore nonconvergence and continue simulation
                                % 2 - produce a dialog
                                % 3 - interrupt simulation and report an error 
                                
% Virtual work method                                
vd=10^-10;                      % virtual displacement (force calculation)                                
vad=10^-9;                      % virtual angular displacement (torque calculation)
                                % vad=[]; - disable Virtual work method torque calculation
                                
% D-Q analysis
fieldweakeningalg='most accurate';     % 'most accurate'  |  'fastest'
                                       % Algorithm used to determine field
                                       % weakening operation for both
                                       % const. output power and max.
                                       % torque control methods.
                                       % 'fastest' uses simplified
                                       % analytical approach (not recommended);
                                       % 'most accurate' uses iterative
                                       % search algorithm to best satisfy
                                       % the control constraints.
                                       
% Eddy current loss calculation settings
ECLnlayers=20;                                         % number of resistance layers in axial dimension 
                                                       % for calculation of 3D eddy current distribution
                                                       % this parameter is not changed after  simulation file
                                                       % initialization
                                                       
% Mesher preference
MesherPreference='Use PDE toolbox mesher';             % 1 - 'Use PDE toolbox mesher' | 2 - 'Use internal mesher'

                                       
if exist('profilePM.mat','file')
    load('profilePM.mat','profile');
    try
        substepmax=str2num(profile.substepmax);
        relaxmin=str2num(profile.relaxmin);
        convreportvalue=profile.convreport;
        if convreportvalue==1
            convreport = 'on';
        elseif convreportvalue==2
            convreport = 'off';
        end
        NonconvHnd=profile.NonconvHnd;
        vd=str2num(profile.vd);
        vad=str2num(profile.vad);
        ECLnlayers=str2num(profile.ECLnlayers);
        MesherPreferenceValue=profile.MesherPreference;
        if MesherPreferenceValue==1
            MesherPreference = 'Use PDE toolbox mesher';
        elseif MesherPreferenceValue==2
            MesherPreference = 'Use internal mesher';
        end
    end
end

output=eval(par);