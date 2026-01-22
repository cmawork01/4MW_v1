# Auto-generated from plotwizard.m
# NOTE: This is a placeholder stub. Manual translation required.

from __future__ import annotations

"""
Original MATLAB source:

function varargout = plotwizard(varargin)
% PLOTWIZARD M-file for PlotWizard.fig
%      PLOTWIZARD, by itself, creates a new PLOTWIZARD or raises the existing
%      singleton*.
%
%      H = PLOTWIZARD returns the handle to a new PLOTWIZARD or the handle to
%      the existing singleton*.
%
%      PLOTWIZARD('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in PLOTWIZARD.M with the given input arguments.
%
%      PLOTWIZARD('Property','Value',...) creates a new PLOTWIZARD or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before PlotWizard_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to PlotWizard_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help PlotWizard

% Last Modified by GUIDE v2.5 22-Sep-2017 18:00:14

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @PlotWizard_OpeningFcn, ...
                   'gui_OutputFcn',  @PlotWizard_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before PlotWizard is made visible.
function PlotWizard_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to PlotWizard (see VARARGIN)

% Choose default command line output for PlotWizard
handles.output = hObject;

motoranalysisInput = find(strcmp(varargin, 'motoranalysis'));
if ~isempty(motoranalysisInput)
   handles.motoranalysis = varargin{motoranalysisInput+1};
end

handles.tm_nsubplots=[];
handles.ag_nsubplots=[];
handles.cs_nfigures=[];

SA.speedaccuracy_setup='Fastest';
SA.speedaccuracy_solvertype='Linear';
SA.speedaccuracy_Ndt_sv='30';
SA.speedaccuracy_Ndt_ch='3';
SA.speedaccuracy_Itol='2%';
SA.speedaccuracy_timestepselection='Automatic';
SA.speedaccuracy_timestep='';
handles.DQPWMSpeedAccuracy=SA;  

Position_panel_tm_plot=get(handles.panel_tm_plot,'Position');
set(handles.panel_tm_plot,'UserData',Position_panel_tm_plot);

Tooltip=sprintf('Specifies the quantity along the X-axis of the plot. It can be \nthe rotor speed in RPM, the supply current in Amperes or \nthe advance angle in electrical degrees.');
set(handles.text_xaxisquantity,'TooltipString',Tooltip);
set(handles.pup_dq_xaxisquantity,'TooltipString',Tooltip);
Tooltip='The rotor speed value(s) in RPM';
set(handles.text_dq_speedvalues,'TooltipString',Tooltip);
Tooltip=sprintf('The RMS supply current value(s) in amperes. For the star connected \nstator winding the supply current is equal to the phase \ncurrent; for the delta connected stator winding the supply \ncurrent is equal to the phase current multiplied by sqrt(3).');
set(handles.text_dq_currentvalues,'TooltipString',Tooltip);
Tooltip='The advance angle value(s) in electrical degrees';
set(handles.text_dq_gammavalues,'TooltipString',Tooltip);
Tooltip=sprintf('Enter value or list of values separated by space, comma or semicolon.\nUse statement ''start:step:stop'' to enter linearly spaced values \nbetween ''start'' and ''stop''.');
set(handles.edit_dq_speedvalues,'TooltipString',Tooltip);
set(handles.edit_dq_currentvalues,'TooltipString',Tooltip);
set(handles.edit_dq_gammavalues,'TooltipString',Tooltip);
tooltip1='Specifies how ''Max. RMS phase voltage'' is defined. \n''unlimited voltage'' - the phase voltage can be infinitely high. \n''by Vdc and PWM method'' - ''Max. RMS phase voltage'' is computed';
tooltip2='\nbased on stator winding connection, DC supply voltage and PWM \nmethod specified in ''Drive Settings''. \n''specified by user'' - ''Max. RMS phase voltage'' should be entered \nmanually by the user.';
Tooltip=sprintf([tooltip1 tooltip2]);
set(handles.pup_dq_voltageselection,'TooltipString',Tooltip);
set(handles.text_dq_voltageselection,'TooltipString',Tooltip);
Tooltip='Maximum RMS phase voltage available from the inverter.';
set(handles.edit_dq_Vsrms_max,'TooltipString',Tooltip);
set(handles.text_dq_Vsrms_max,'TooltipString',Tooltip);
Tooltip=sprintf('Specifies whether the separated y-axis will be used for each \nplotted quantity. Uncheck if plotted quantities have the same \nunits.');
set(handles.checkbox_dq_multipleyaxes,'TooltipString',Tooltip);
tooltip1='Specifies the model used to calculate the result. \n''D-Q with sinusoidal supply'' - result is interpolated using \nthe D-Q model built in the D-Q Analysis window.'; 
tooltip2='\n''D-Q with PWM supply'' - result is obtained with dynamic \nD-Q simulation and drive type specified in ''Drive Settings''.';
tooltip3='\n''FEA based'' - the same as ''D-Q with sinusoidal supply'' but \nthe result is determined directly from FEA solution; \nbuilding of D-Q model is not required.';
Tooltip=sprintf([tooltip1 tooltip2 tooltip3]);
set(handles.text_dq_modeltype,'TooltipString',Tooltip);
set(handles.pup_dq_modeltype,'TooltipString',Tooltip);
Tooltip=sprintf('Specifies how the parameters of the D-Q model are \ninterpolated.');
set(handles.text_dq_interpmethod,'TooltipString',Tooltip);
set(handles.pup_dq_interpmethod,'TooltipString',Tooltip);
tooltip1='The RMS phase current in amperes. For the star connected \nstator winding the phase current is equal to the supply \ncurrent (line current); for the delta connected stator winding';
tooltip2='\nthe phase current is equal to the supply current divided by \nsqrt(3).';
Tooltip=sprintf([tooltip1 tooltip2]);
set(handles.checkbox_Is,'TooltipString',Tooltip);
Tooltip=sprintf('The input active electrical power in watts. \nNegative for the generator mode.');
set(handles.checkbox_Pinput,'TooltipString',Tooltip);
Tooltip=sprintf('The output mechanical power in watts. \nNegative for the generator mode.');
set(handles.checkbox_Pmech,'TooltipString',Tooltip);
Tooltip=sprintf('The reactive electrical power in vars.');
set(handles.checkbox_Preact,'TooltipString',Tooltip);
Tooltip=sprintf('The d-axis magnet flux linkage measured with zero stator \ncurrent.');
set(handles.checkbox_fluxlinkage_md,'TooltipString',Tooltip);
Tooltip=sprintf('The q-axis magnet flux linkage caused by the cross- \nsaturation and measured with zero stator current.');
set(handles.checkbox_fluxlinkage_mqd,'TooltipString',Tooltip);

% Tooltip=sprintf('Range of advance angle values the maximum efficiency is \nsearched for. Use statement ''start:step:stop'' to enter linearly \nspaced values between ''start'' and ''stop''.');
Tooltip=sprintf('Range of advance angle values the maximum efficiency is \nsearched for. Advance angle values should be in format ''min:step:max''.');
set(handles.edit_em_gammavalues,'TooltipString',Tooltip);
set(handles.text_em_gammavalues,'TooltipString',Tooltip);
Tooltip=sprintf('Maximum RMS phase voltage available from the inverter. \nFor generator mode: maximum RMS phase voltage available \nfrom the generator.');
set(handles.edit_em_Vphasemax,'TooltipString',Tooltip);
set(handles.text_em_Vphasemax,'TooltipString',Tooltip);
Tooltip=sprintf('Maximum RMS phase current available from the inverter. \nFor generator mode: maximum RMS phase current available \nfrom the generator.');
set(handles.edit_em_Iphasemax,'TooltipString',Tooltip);
set(handles.text_em_Iphasemax,'TooltipString',Tooltip);
tooltip1='Maximum input electrical power available from the inverter. \nFor generator mode: maximum electrical power available \nfrom the generator. If left empty the power limit is defined';
tooltip2='\nonly by voltage and current limits.';
Tooltip=sprintf([tooltip1 tooltip2]);
set(handles.edit_em_Pinputmax,'TooltipString',Tooltip);
set(handles.text_em_Pinputmax,'TooltipString',Tooltip);
Tooltip=sprintf('Maximum rotor speed for which the efficiency map is computed.');
set(handles.edit_em_speedmax,'TooltipString',Tooltip);
set(handles.text_em_speedmax,'TooltipString',Tooltip);
Tooltip=sprintf('Determines the sequence of torque values for which the efficiency \nmap is computed.');
set(handles.edit_em_torquestep,'TooltipString',Tooltip);
set(handles.text_em_torquestep,'TooltipString',Tooltip);
Tooltip=sprintf('Determines the sequence of speed values for which the efficiency \nmap is computed.');
set(handles.edit_em_speedstep,'TooltipString',Tooltip);
set(handles.text_em_speedstep,'TooltipString',Tooltip);
tooltip1='Specifies the model used to compute efficiency map. \n''D-Q with sinusoidal supply'' - result is interpolated using \nthe D-Q model built in the D-Q Analysis window.';
tooltip2='\n''FEA based'' - result is determined directly from FEA solution; \nbuilding of D-Q model is not required.';Tooltip=sprintf([tooltip1 tooltip2]);
set(handles.text_em_modeltype,'TooltipString',Tooltip);
set(handles.pup_em_modeltype,'TooltipString',Tooltip);
Tooltip=sprintf('Specifies how the parameters of the D-Q model are \ninterpolated.');
set(handles.text_em_interpmethod,'TooltipString',Tooltip);
set(handles.pup_em_interpmethod,'TooltipString',Tooltip);
handles.StopPlotting = 0;
% publish function UpdatePlotWizard
handles.UpdatePlotWizard = @UpdatePlotWizard;
% publish function SavePlotWizardProfile
handles.SavePlotWizardProfile = @SavePlotWizardProfile;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes PlotWizard wait for user response (see UIRESUME)
% uiwait(handles.PlotWizard);


% --- Outputs from this function are returned to the command line.
function varargout = PlotWizard_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes during object deletion, before destroying properties.
function PlotWizard_DeleteFcn(hObject, eventdata, handles)
% hObject    handle to PlotWizard (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
SavePlotWizardProfile(handles);


% --- Executes when user attempts to close PlotWizard.
function PlotWizard_CloseRequestFcn(hObject, eventdata, handles)
% Don't close this figure. It must be deleted from motoranalysis
% Make it invisible then user tries to close it
OuterPosition=get(handles.PlotWizard,'OuterPosition');
if strcmp(get(handles.pushbutton_showplottedquantities,'String'),'Plotted quantities  <<')
    OuterPosition(3) = OuterPosition(3)*2/3;
    set(handles.PlotWizard,'OuterPosition',OuterPosition);
    set(handles.pushbutton_showplottedquantities,'String','Plotted quantities  >>');
    set(handles.pushbutton_showplottedquantities,'TooltipString','Click to show plotted quantities.');
end
set(hObject,'Visible','off');
motoranalysishandles = guidata(handles.motoranalysis);
set(motoranalysishandles.menuPlotWizard,'Checked','off');
% SavePlotWizardProfile(handles);


function LoadPlotWizardProfile(handles,FileName)
if ~isempty(FileName)
    load(FileName);
    if exist('PlotWizard','var')
        try
            set(handles.checkbox_Is,'Value',PlotWizard.checkbox_Is);
            set(handles.checkbox_Vs,'Value',PlotWizard.checkbox_Vs);
            set(handles.checkbox_Id,'Value',PlotWizard.checkbox_Id);
            set(handles.checkbox_Iq,'Value',PlotWizard.checkbox_Iq);
            set(handles.checkbox_Vd,'Value',PlotWizard.checkbox_Vd);
            set(handles.checkbox_Vq,'Value',PlotWizard.checkbox_Vq);
            set(handles.checkbox_Gamma,'Value',PlotWizard.checkbox_Gamma);
            set(handles.checkbox_Torque,'Value',PlotWizard.checkbox_Torque);
            set(handles.checkbox_MagnetTorque,'Value',PlotWizard.checkbox_MagnetTorque);
            set(handles.checkbox_ReluctanceTorque,'Value',PlotWizard.checkbox_ReluctanceTorque);
            set(handles.checkbox_Pinput,'Value',PlotWizard.checkbox_Pinput);
            set(handles.checkbox_Pmech,'Value',PlotWizard.checkbox_Pmech);
            set(handles.checkbox_Efficiency,'Value',PlotWizard.checkbox_Efficiency);
            set(handles.checkbox_PowerFactor,'Value',PlotWizard.checkbox_PowerFactor);
            set(handles.checkbox_Ps,'Value',PlotWizard.checkbox_Ps);
            set(handles.checkbox_backEMF,'Value',PlotWizard.checkbox_backEMF);
            set(handles.checkbox_Ld,'Value',PlotWizard.checkbox_Ld);
            set(handles.checkbox_Lq,'Value',PlotWizard.checkbox_Lq);
            set(handles.checkbox_Ldq,'Value',PlotWizard.checkbox_Ldq);
            set(handles.checkbox_fluxlinkage_md,'Value',PlotWizard.checkbox_fluxlinkage_md);
            set(handles.checkbox_fluxlinkage_mqd,'Value',PlotWizard.checkbox_fluxlinkage_mqd);
            set(handles.pup_dq_xaxisquantity,'Value',PlotWizard.pup_dq_xaxisquantity);
            set(handles.edit_dq_speedvalues,'String',PlotWizard.edit_dq_speedvalues);
            set(handles.edit_dq_currentvalues,'String',PlotWizard.edit_dq_currentvalues);
            set(handles.edit_dq_gammavalues,'String',PlotWizard.edit_dq_gammavalues);
            set(handles.edit_dq_Vsrms_max,'String',PlotWizard.edit_dq_Vsrms_max);
            set(handles.checkbox_dq_multipleyaxes,'Value',PlotWizard.checkbox_dq_multipleyaxes);
            set(handles.pup_dq_modeltype,'Value',PlotWizard.pup_dq_modeltype);
            set(handles.pup_dq_interpmethod,'Value',PlotWizard.pup_dq_interpmethod);
            set(handles.edit_em_gammavalues,'String',PlotWizard.edit_em_gammavalues);
            set(handles.edit_em_Vphasemax,'String',PlotWizard.edit_em_Vphasemax);
            set(handles.edit_em_Iphasemax,'String',PlotWizard.edit_em_Iphasemax);
            set(handles.edit_em_Pinputmax,'String',PlotWizard.edit_em_Pinputmax);
            set(handles.edit_em_speedmax,'String',PlotWizard.edit_em_speedmax);
            set(handles.edit_em_Kmechloss,'String',PlotWizard.edit_em_Kmechloss);
            set(handles.edit_em_torquestep,'String',PlotWizard.edit_em_torquestep);
            set(handles.edit_em_speedstep,'String',PlotWizard.edit_em_speedstep);
            set(handles.pup_em_modeltype,'Value',PlotWizard.pup_em_modeltype);
            set(handles.pup_em_interpmethod,'Value',PlotWizard.pup_em_interpmethod);
            set(handles.checkbox_Preact,'Value',PlotWizard.checkbox_Preact);
            set(handles.pup_dq_fieldweakeningcontrol,'Value',PlotWizard.pup_dq_fieldweakeningcontrol);
            handles.DQPWMSpeedAccuracy=PlotWizard.DQPWMSpeedAccuracy;
            set(handles.pup_dq_voltageselection,'Value',PlotWizard.pup_dq_voltageselection);
            guidata(handles.PlotWizard, handles);
        catch
            disp('Failed to load PlotWizard configuration');
        end
    end
end


function SavePlotWizardProfile(handles)
motoranalysishandles = guidata(handles.motoranalysis);
if ~isempty(motoranalysishandles.File)
    load(motoranalysishandles.File);
    PlotWizard=[];
    PlotWizard.checkbox_Is=get(handles.checkbox_Is,'Value');
    PlotWizard.checkbox_Vs=get(handles.checkbox_Vs,'Value');
    PlotWizard.checkbox_Id=get(handles.checkbox_Id,'Value');
    PlotWizard.checkbox_Iq=get(handles.checkbox_Iq,'Value');
    PlotWizard.checkbox_Vd=get(handles.checkbox_Vd,'Value');
    PlotWizard.checkbox_Vq=get(handles.checkbox_Vq,'Value');
    PlotWizard.checkbox_Gamma=get(handles.checkbox_Gamma,'Value');
    PlotWizard.checkbox_Torque=get(handles.checkbox_Torque,'Value');
    PlotWizard.checkbox_MagnetTorque=get(handles.checkbox_MagnetTorque,'Value');
    PlotWizard.checkbox_ReluctanceTorque=get(handles.checkbox_ReluctanceTorque,'Value');
    PlotWizard.checkbox_Pinput=get(handles.checkbox_Pinput,'Value');
    PlotWizard.checkbox_Pmech=get(handles.checkbox_Pmech,'Value');
    PlotWizard.checkbox_Preact=get(handles.checkbox_Preact,'Value');
    PlotWizard.checkbox_Efficiency=get(handles.checkbox_Efficiency,'Value');
    PlotWizard.checkbox_PowerFactor=get(handles.checkbox_PowerFactor,'Value');
    PlotWizard.checkbox_Ps=get(handles.checkbox_Ps,'Value');
    PlotWizard.checkbox_backEMF=get(handles.checkbox_backEMF,'Value');
    PlotWizard.checkbox_Ld=get(handles.checkbox_Ld,'Value');
    PlotWizard.checkbox_Lq=get(handles.checkbox_Lq,'Value');
    PlotWizard.checkbox_Ldq=get(handles.checkbox_Ldq,'Value');
    PlotWizard.checkbox_fluxlinkage_md=get(handles.checkbox_fluxlinkage_md,'Value');
    PlotWizard.checkbox_fluxlinkage_mqd=get(handles.checkbox_fluxlinkage_mqd,'Value');
    PlotWizard.pup_dq_xaxisquantity=get(handles.pup_dq_xaxisquantity,'Value');
    PlotWizard.edit_dq_speedvalues=get(handles.edit_dq_speedvalues,'String');
    PlotWizard.edit_dq_currentvalues=get(handles.edit_dq_currentvalues,'String');
    PlotWizard.edit_dq_gammavalues=get(handles.edit_dq_gammavalues,'String');
    PlotWizard.edit_dq_Vsrms_max=get(handles.edit_dq_Vsrms_max,'String');
    PlotWizard.checkbox_dq_multipleyaxes=get(handles.checkbox_dq_multipleyaxes,'Value');
    PlotWizard.pup_dq_modeltype=get(handles.pup_dq_modeltype,'Value');
    PlotWizard.pup_dq_interpmethod=get(handles.pup_dq_interpmethod,'Value');
    PlotWizard.edit_em_gammavalues=get(handles.edit_em_gammavalues,'String');
    PlotWizard.edit_em_Vphasemax=get(handles.edit_em_Vphasemax,'String');
    PlotWizard.edit_em_Iphasemax=get(handles.edit_em_Iphasemax,'String');
    PlotWizard.edit_em_Pinputmax=get(handles.edit_em_Pinputmax,'String');
    PlotWizard.edit_em_speedmax=get(handles.edit_em_speedmax,'String');
    PlotWizard.edit_em_Kmechloss=get(handles.edit_em_Kmechloss,'String');
    PlotWizard.edit_em_torquestep=get(handles.edit_em_torquestep,'String');
    PlotWizard.edit_em_speedstep=get(handles.edit_em_speedstep,'String');
    PlotWizard.pup_em_modeltype=get(handles.pup_em_modeltype,'Value');
    PlotWizard.pup_em_interpmethod=get(handles.pup_em_interpmethod,'Value');
    PlotWizard.pup_dq_fieldweakeningcontrol=get(handles.pup_dq_fieldweakeningcontrol,'Value');
    PlotWizard.DQPWMSpeedAccuracy=handles.DQPWMSpeedAccuracy;
    PlotWizard.pup_dq_voltageselection=get(handles.pup_dq_voltageselection,'Value');
    save(motoranalysishandles.File,'Simulation','PlotWizard');
end


function UpdatePlotWizard(hObject,FileName)
% if FileName is not empty - load new simulation file
handles = guidata(hObject);
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
if get(motoranalysishandles.togglebutton_dynamicFEA,'Value')      % dynamicFEA
    folder = Simulation.Settings.DynamicFEA.DF_saveeachsolutionfolder;
    timestep = Simulation.Settings.DynamicFEA.DF_timestep;
    if isempty(Simulation.DynamicFEA.time)
        CurrentTime=0;
    else
        CurrentTime=Simulation.DynamicFEA.time(end)-Simulation.DynamicFEA.time(1);
    end
    % CurrentTime = Simulation.DynamicFEA.CurrentTime;
    % CurrentTime = CurrentTime-timestep;
    srt_time=time2str(CurrentTime,timestep,CurrentTime);
    set(handles.edit_an_time_start,'String',time2str(timestep,timestep,CurrentTime));
elseif get(motoranalysishandles.togglebutton_MS,'Value')          % magnetostatic
    folder = Simulation.Settings.Magnetostatic.MS_saveeachsolutionfolder;
    if ~isempty(Simulation.Magnetostatic.Timesteppingdata) && length(Simulation.Magnetostatic.Timesteppingdata.time)>1
        CurrentTime = Simulation.Magnetostatic.Timesteppingdata.time(end);
        timestep = Simulation.Magnetostatic.Timesteppingdata.time(2)-Simulation.Magnetostatic.Timesteppingdata.time(1);
    else
        CurrentTime = 0;
        timestep = 0;
    end
    srt_time=0;
    set(handles.edit_an_time_start,'String','0');
end

nSlices = Simulation.Mesh.nSlices;
strSlices=cell(nSlices,1);
for i=1:nSlices
    strSlices{i,1}=num2str(i);
end

if ~isempty(FileName)   % if load simulation file
    LoadPlotWizardProfile(handles,FileName);
    handles=guidata(hObject);
end

if get(motoranalysishandles.togglebutton_dynamicFEA,'Value') || get(motoranalysishandles.togglebutton_MS,'Value')
    for i=1:5
        set(getfield(handles,['edit_ag_time' num2str(i)]),'String',srt_time);
        set(getfield(handles,['edit_cs_time' num2str(i)]),'String',srt_time);
        set(getfield(handles,['pup_ag_slice' num2str(i)]),'String',strSlices);
        set(getfield(handles,['pup_cs_slice' num2str(i)]),'String',strSlices);
        set(getfield(handles,['pup_ag_slice' num2str(i)]),'Value',1);
        set(getfield(handles,['pup_cs_slice' num2str(i)]),'Value',1);
    end
%     set(handles.edit_an_time_start,'String',srt_time);
    
    set(handles.edit_an_time_stop,'String',time2str(CurrentTime,timestep,CurrentTime));
    set(handles.edit_nfluxlevels,'String',num2str(20));
    SetSourceFolder(handles,folder);
elseif get(motoranalysishandles.togglebutton_DQ,'Value')
    % D-Q analysis plot panel
    index = get(handles.pup_dq_xaxisquantity,'Value');
    strlist = get(handles.pup_dq_xaxisquantity,'String');
    xaxisquantity = strlist{index,1};
    index = get(handles.pup_dq_modeltype,'Value');
    strlist = get(handles.pup_dq_modeltype,'String');
    modeltype = strlist{index,1};    
    if strcmp(modeltype,'D-Q with PWM supply')
        set(handles.pup_dq_voltageselection,'Value',2);    % Phase voltage selection: 'Based on Vdc and PWM method'
        set(handles.pup_dq_voltageselection,'Visible','on');
        set(handles.edit_dq_Vsrms_max,'Visible','on');
        set(handles.text_dq_Vsrms_max,'Visible','on');
        set(handles.text_dq_Vsrms_max_unit,'Visible','on');
        set(handles.pushbutton_dq_how,'Visible','on');
        set(handles.pup_dq_voltageselection,'Enable','off');
        set(handles.edit_dq_Vsrms_max,'Enable','off');
        if strcmp(xaxisquantity,'Speed')
            set(handles.pup_dq_fieldweakeningcontrol,'Visible','on');
            set(handles.text_dq_fieldweakeningcontrol,'Visible','on');
        else
            set(handles.pup_dq_fieldweakeningcontrol,'Visible','off');
            set(handles.text_dq_fieldweakeningcontrol,'Visible','off');
        end    
        if ~isempty(handles.DQPWMSpeedAccuracy)
            SpeedAccuracySetup=handles.DQPWMSpeedAccuracy.speedaccuracy_setup;
            set(handles.pushbutton_DQspeedaccuracy,'String',[SpeedAccuracySetup{1} ' (click to change)']);
        else
            set(handles.pushbutton_DQspeedaccuracy,'String','Fastest (click to change)');
        end
        set(handles.pushbutton_DQspeedaccuracy,'Visible','on');
        set(handles.text_DQspeedaccuracy,'Visible','on');
    else
        set(handles.pushbutton_DQspeedaccuracy,'Visible','off');
        set(handles.text_DQspeedaccuracy,'Visible','off');
        set(handles.pup_dq_voltageselection,'Visible','on');
        if strcmp(xaxisquantity,'Speed')
            set(handles.pup_dq_voltageselection,'Enable','on');
            if get(handles.pup_dq_voltageselection,'Value')==2 || ...   % 'Based on Vdc and PWM method'
               get(handles.pup_dq_voltageselection,'Value')==3          %  or 'Specified by user'
                set(handles.edit_dq_Vsrms_max,'Visible','on');
                set(handles.text_dq_Vsrms_max,'Visible','on');
                set(handles.text_dq_Vsrms_max_unit,'Visible','on');
                set(handles.pushbutton_dq_how,'Visible','on');
                set(handles.pup_dq_fieldweakeningcontrol,'Visible','on');
                set(handles.text_dq_fieldweakeningcontrol,'Visible','on');
                if get(handles.pup_dq_voltageselection,'Value')==2    % 'Based on Vdc and PWM method'
                    set(handles.edit_dq_Vsrms_max,'Enable','off');
                else                                                  % 'Specified by user'
                    set(handles.edit_dq_Vsrms_max,'Enable','on');
                end
            else                                                      % Phase voltage selection: 'Unlimited voltage'
                set(handles.edit_dq_Vsrms_max,'Visible','off');
                set(handles.text_dq_Vsrms_max,'Visible','off');
                set(handles.text_dq_Vsrms_max_unit,'Visible','off');
                set(handles.pushbutton_dq_how,'Visible','off');
                set(handles.pup_dq_fieldweakeningcontrol,'Visible','off');
                set(handles.text_dq_fieldweakeningcontrol,'Visible','off');
            end
        elseif strcmp(xaxisquantity,'Supply current') || strcmp(xaxisquantity,'Advance angle')
            set(handles.pup_dq_voltageselection,'Value',1);     % 'Unlimited voltage'
            set(handles.pup_dq_voltageselection,'Enable','off');
            set(handles.edit_dq_Vsrms_max,'Visible','off');
            set(handles.text_dq_Vsrms_max,'Visible','off');
            set(handles.text_dq_Vsrms_max_unit,'Visible','off');
            set(handles.pushbutton_dq_how,'Visible','off');
            set(handles.pup_dq_fieldweakeningcontrol,'Visible','off');
            set(handles.text_dq_fieldweakeningcontrol,'Visible','off');
        end
    end
    if get(handles.pup_dq_voltageselection,'Value')==2    % Phase voltage selection: 'Based on Vdc and PWM method'
        SetDQPhaseVoltage(hObject);
        set(handles.pushbutton_dq_how,'Enable','on');
    else
        set(handles.pushbutton_dq_how,'Enable','off');
    end
    if strcmp(modeltype,'FEA based')
        set(handles.pup_dq_interpmethod,'Enable','off');
        set(handles.pup_dq_interpmethod,'Value',2);    % Nonlinear
    elseif strcmp(modeltype,'D-Q with sinusoidal supply')
        set(handles.pup_dq_interpmethod,'Enable','on');
    elseif strcmp(modeltype,'D-Q with PWM supply')
        set(handles.pup_dq_interpmethod,'Enable','off');
        if ~isempty(handles.DQPWMSpeedAccuracy)
            SpeedAccuracySolverType=handles.DQPWMSpeedAccuracy.speedaccuracy_solvertype;
            if strcmp(SpeedAccuracySolverType,'Nonlinear')
                set(handles.pup_dq_interpmethod,'Value',2);    % Nonlinear
            else
                set(handles.pup_dq_interpmethod,'Value',1);    % Linearized
            end
        end
    end
    % Efficiency map panel
    index = get(handles.pup_em_modeltype,'Value');
    strlist = get(handles.pup_em_modeltype,'String');
    modeltype = strlist{index,1};
    if strcmp(modeltype,'FEA based')
        set(handles.pup_em_interpmethod,'Enable','off');
        set(handles.pup_em_interpmethod,'Value',2);    % Nonlinear
    elseif strcmp(modeltype,'D-Q with sinusoidal supply')
        set(handles.pup_em_interpmethod,'Enable','on');
    end

    Kmechloss=get(handles.edit_em_Kmechloss,'String');
    Kmechloss=checkKmechloss(Kmechloss);
    tooltip1='The mechanical loss equation coefficients of descending powers';
    tooltip2='\nof rotor speed in rpm. Coefficients can be separated by space,';
    tooltip3='\ncomma or semicolon. If left empty no mechanical losses applied.';
    Tooltip=[tooltip1 tooltip2 tooltip3];
    if length(Kmechloss)==1 && (isnan(Kmechloss) || Kmechloss==0)
        tooltip1='\nExample: for mechanical loss coefficients [a b c] the mechanical';
        tooltip2='\nlosses are as follows: a*(rpm)^2+b*(rpm)+c.';
    else
        tooltip1='\nFor coefficients entered the mechanical losses are as follows:';
        tooltip2='\n';
        for i=1:length(Kmechloss)
            if i==length(Kmechloss)
                tooltip2=[tooltip2 num2str(Kmechloss(i)) '.'];
            elseif i==length(Kmechloss)-1
                tooltip2=[tooltip2 num2str(Kmechloss(i)) '*(rpm)+'];
            else
                tooltip2=[tooltip2 num2str(Kmechloss(i)) '*(rpm)^' num2str(length(Kmechloss)-i) '+'];
            end
        end
    end
    Tooltip=sprintf([Tooltip tooltip1 tooltip2]);
    set(handles.edit_em_Kmechloss,'TooltipString',Tooltip);
    set(handles.text_em_Kmechloss,'TooltipString',Tooltip);

    EfficiencyMap = Simulation.EfficiencyMap;
    if ~isempty(EfficiencyMap)
        tooltip1='Efficiency map details: ';
        tooltip2=['\nAdvance angle values (el.deg.): ' EfficiencyMap.strGamma];
        tooltip3=['\nMaximum RMS phase voltage (V): ' num2str(EfficiencyMap.Vmax)];
        tooltip4=['\nMaximum RMS phase current (A): ' num2str(EfficiencyMap.Ismax)];
        tooltip5=['\nMaximum speed (RPM): ' num2str(EfficiencyMap.speedmax)];
        tooltip6=['\nTorque step (N*m): ' num2str(EfficiencyMap.torquestep)];
        tooltip7=['\nSpeed step (RPM): ' num2str(EfficiencyMap.speedstep)];
        tooltip8=['\nInterpolation method: ' EfficiencyMap.interpmethod];
        Tooltip=sprintf([tooltip1 tooltip2 tooltip3 tooltip4 tooltip5 tooltip6 tooltip7 tooltip8]);
        set(handles.pushbutton_plotmap,'TooltipString',Tooltip);
        set(handles.pushbutton_plotmap,'Enable','on');
        set(handles.pushbutton_mapopts,'Enable','on');
    else
        set(handles.pushbutton_plotmap,'TooltipString','');
        set(handles.pushbutton_plotmap,'Enable','off');
        set(handles.pushbutton_mapopts,'Enable','off');
    end
    guidata(hObject, handles);
end


function checkbox_tm_subplot_Callback(hObject, eventdata, handles)
Tag = get(hObject,'Tag');
if strcmp(Tag(1:19),'checkbox_tm_subplot')
    ind=str2num(Tag(20:end));
    if get(hObject,'Value')     % activate subplot
        set(getfield(handles,['edit_tm_plotexp' num2str(ind)]),'Enable','on');
        set(getfield(handles,['pushbutton_tm_changeplot' num2str(ind)]),'Enable','on');
        set(hObject,'TooltipString','Click to deactivate subplot');
        nsubplots=numbersubplots(handles,'checkbox_tm_subplot');
    else                        % deactivate subplot
        set(getfield(handles,['edit_tm_plotexp' num2str(ind)]),'Enable','off');
        set(getfield(handles,['pushbutton_tm_changeplot' num2str(ind)]),'Enable','off');
        set(hObject,'TooltipString','Click to activate subplot');
        nsubplots=numbersubplots(handles,'checkbox_tm_subplot');
    end
    handles.tm_nsubplots = nsubplots;
end
guidata(hObject, handles);


function checkbox_ag_subplot_Callback(hObject, eventdata, handles)
% hObject    handle to checkbox_ag_subplot (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Tag = get(hObject,'Tag');
if strcmp(Tag(1:19),'checkbox_ag_subplot')
    ind=str2num(Tag(20:end));
    if get(hObject,'Value')     % activate subplot
        set(getfield(handles,['edit_ag_vars' num2str(ind)]),'Enable','on');
        set(getfield(handles,['pushbutton_ag_addvar' num2str(ind)]),'Enable','on');
        set(hObject,'TooltipString','Click to deactivate subplot');
        nsubplots=numbersubplots(handles,'checkbox_ag_subplot');
    else                        % deactivate subplot
        set(getfield(handles,['edit_ag_vars' num2str(ind)]),'Enable','off');
        set(getfield(handles,['pushbutton_ag_addvar' num2str(ind)]),'Enable','off');
        set(hObject,'TooltipString','Click to activate subplot');
        nsubplots=numbersubplots(handles,'checkbox_ag_subplot');
    end
    handles.ag_nsubplots = nsubplots;
end
guidata(hObject, handles);


function nsubplots=numbersubplots(handles,tag)
subplot_number=1;
nsubplots=[];
for i=1:5
    if get(getfield(handles,[tag num2str(i)]),'Value')   % if subplot is active
        set(getfield(handles,[tag num2str(i)]),'String',['  ' num2str(subplot_number)]);
        subplot_number=subplot_number+1;
        nsubplots=[nsubplots i];
    else
        set(getfield(handles,[tag num2str(i)]),'String','');
    end
end

function checkbox_cs_figure_Callback(hObject, eventdata, handles)
% hObject    handle to checkbox_cs_figure (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Tag = get(hObject,'Tag');
if strcmp(Tag(1:18),'checkbox_cs_figure')
    ind=str2num(Tag(19:end));
    if get(hObject,'Value')     % activate figure
        set(getfield(handles,['pup_cs_quantity' num2str(ind)]),'Enable','on');
        set(hObject,'TooltipString','Click to deactivate figure');
        nfigures=numberfigures(handles);
    else                        % deactivate figure
        set(getfield(handles,['pup_cs_quantity' num2str(ind)]),'Enable','off');
        set(hObject,'TooltipString','Click to activate figure');
        nfigures=numberfigures(handles);
    end
    handles.cs_nfigures = nfigures;
end
guidata(hObject, handles);


function nfigures=numberfigures(handles)
figure_number=1;
nfigures=[];
for i=1:5
    if get(getfield(handles,['checkbox_cs_figure' num2str(i)]),'Value')   % if figure is active
        set(getfield(handles,['checkbox_cs_figure' num2str(i)]),'String',['  ' num2str(figure_number)]);
        figure_number=figure_number+1;
        nfigures=[nfigures i];
    else
        set(getfield(handles,['checkbox_cs_figure' num2str(i)]),'String','');
    end
end


% --- Executes on button press in pushbutton_ag_addvar.
function pushbutton_ag_addvar_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_ag_addvar1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Tag = get(hObject,'Tag');
if strcmp(Tag(1:20),'pushbutton_ag_addvar')
    ind=str2num(Tag(21:end));
    varsstr=get(getfield(handles,['edit_ag_vars' num2str(ind)]),'String');
    varsstr=strtrim(varsstr);
    if ~isempty(varsstr)
        if strcmp(varsstr(end),',') || strcmp(varsstr(end),';')
            varsstr(end)=[];
        end
    end
    varslist=ag_addvariable();
    for i=1:length(varslist)
        if ~isempty(varsstr)
            varsstr=[varsstr ', ' varslist{i,1}];
        else
            varsstr=[varsstr varslist{i,1}];
        end
    end
    set(getfield(handles,['edit_ag_vars' num2str(ind)]),'String',varsstr);
    guidata(hObject, handles);
end


function ag_changetime_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_ag_timeup1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
if get(motoranalysishandles.togglebutton_dynamicFEA,'Value')      % dynamicFEA
    timestep = Simulation.Settings.DynamicFEA.DF_timestep;
    if isempty(Simulation.DynamicFEA.time)
        CurrentTime=0;
    else
        CurrentTime=Simulation.DynamicFEA.time(end)-Simulation.DynamicFEA.time(1);
    end
    % CurrentTime = Simulation.DynamicFEA.CurrentTime;
    % CurrentTime = CurrentTime-timestep;
elseif get(motoranalysishandles.togglebutton_MS,'Value')          % magnetostatic
    if ~isempty(Simulation.Magnetostatic.Timesteppingdata) && length(Simulation.Magnetostatic.Timesteppingdata.time)>1
        CurrentTime = Simulation.Magnetostatic.Timesteppingdata.time(end);
        timestep = Simulation.Magnetostatic.Timesteppingdata.time(2)-Simulation.Magnetostatic.Timesteppingdata.time(1);
    else
        CurrentTime = 0;
        timestep = 0;
    end
end
Tag = get(hObject,'Tag');
if strcmp(Tag(1:12),'edit_ag_time')
        ind=str2num(Tag(13:end));
        time=get(getfield(handles,['edit_ag_time' num2str(ind)]),'String');
        [time status]=str2num(time);
        if status
            srt_time=time2str(time,timestep,CurrentTime);
        else
            errordlg('Not a valid value.','PlotWizard Error','modal');
            srt_time=time2str(CurrentTime,timestep,CurrentTime);
        end
        set(getfield(handles,['edit_ag_time' num2str(ind)]),'String',srt_time);   
elseif strcmp(Tag(1:20),'pushbutton_ag_timeup')
    ind=str2num(Tag(21:end));
    srt_time=time2str(CurrentTime,timestep,CurrentTime);
    set(getfield(handles,['edit_ag_time' num2str(ind)]),'String',srt_time);
else
    if strcmp(Tag(1:20),'pushbutton_ag_timebw')
        ind=str2num(Tag(21:end));
        time=get(getfield(handles,['edit_ag_time' num2str(ind)]),'String');
        time=str2num(time);
        time=time-timestep;
        srt_time=time2str(time,timestep,CurrentTime);
        set(getfield(handles,['edit_ag_time' num2str(ind)]),'String',srt_time);   
    elseif strcmp(Tag(1:20),'pushbutton_ag_timefw')
        ind=str2num(Tag(21:end));
        time=get(getfield(handles,['edit_ag_time' num2str(ind)]),'String');
        time=str2num(time);
        time=time+timestep;
        srt_time=time2str(time,timestep,CurrentTime);
        set(getfield(handles,['edit_ag_time' num2str(ind)]),'String',srt_time);        
    end
end
guidata(hObject, handles);


function cs_changetime_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_ag_timeup1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
if get(motoranalysishandles.togglebutton_dynamicFEA,'Value')      % dynamicFEA
    timestep = Simulation.Settings.DynamicFEA.DF_timestep;
    if isempty(Simulation.DynamicFEA.time)
        CurrentTime=0;
    else
        CurrentTime=Simulation.DynamicFEA.time(end)-Simulation.DynamicFEA.time(1);
    end
    % CurrentTime = Simulation.DynamicFEA.CurrentTime;
    % CurrentTime = CurrentTime-timestep;
elseif get(motoranalysishandles.togglebutton_MS,'Value')          % magnetostatic
    if ~isempty(Simulation.Magnetostatic.Timesteppingdata) && length(Simulation.Magnetostatic.Timesteppingdata.time)>1
        CurrentTime = Simulation.Magnetostatic.Timesteppingdata.time(end);
        timestep = Simulation.Magnetostatic.Timesteppingdata.time(2)-Simulation.Magnetostatic.Timesteppingdata.time(1);
    else
        CurrentTime = 0;
        timestep = 0;
    end
end
Tag = get(hObject,'Tag');
if strcmp(Tag(1:12),'edit_cs_time')
        ind=str2num(Tag(13:end));
        time=get(getfield(handles,['edit_cs_time' num2str(ind)]),'String');
        [time status]=str2num(time);
        if status
            srt_time=time2str(time,timestep,CurrentTime);
        else
            errordlg('Not a valid value.','PlotWizard Error','modal');
            srt_time=time2str(CurrentTime,timestep,CurrentTime);
        end
        set(getfield(handles,['edit_cs_time' num2str(ind)]),'String',srt_time);   
elseif strcmp(Tag(1:20),'pushbutton_cs_timeup')
    ind=str2num(Tag(21:end));
    srt_time=time2str(CurrentTime,timestep,CurrentTime);
    set(getfield(handles,['edit_cs_time' num2str(ind)]),'String',srt_time);
else
    if strcmp(Tag(1:20),'pushbutton_cs_timebw')
        ind=str2num(Tag(21:end));
        time=get(getfield(handles,['edit_cs_time' num2str(ind)]),'String');
        time=str2num(time);
        time=time-timestep;
        srt_time=time2str(time,timestep,CurrentTime);
        set(getfield(handles,['edit_cs_time' num2str(ind)]),'String',srt_time);   
    elseif strcmp(Tag(1:20),'pushbutton_cs_timefw')
        ind=str2num(Tag(21:end));
        time=get(getfield(handles,['edit_cs_time' num2str(ind)]),'String');
        time=str2num(time);
        time=time+timestep;
        srt_time=time2str(time,timestep,CurrentTime);
        set(getfield(handles,['edit_cs_time' num2str(ind)]),'String',srt_time);        
    end
end
guidata(hObject, handles);

function an_changetime_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_ag_timeup1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
if get(motoranalysishandles.togglebutton_dynamicFEA,'Value')      % dynamicFEA
    timestep = Simulation.Settings.DynamicFEA.DF_timestep;
    if isempty(Simulation.DynamicFEA.time)
        CurrentTime=0;
    else
        CurrentTime=Simulation.DynamicFEA.time(end)-Simulation.DynamicFEA.time(1);
    end
    % CurrentTime = Simulation.DynamicFEA.CurrentTime;
    % CurrentTime = CurrentTime-timestep;
elseif get(motoranalysishandles.togglebutton_MS,'Value')          % magnetostatic
    if ~isempty(Simulation.Magnetostatic.Timesteppingdata) && length(Simulation.Magnetostatic.Timesteppingdata.time)>1
        CurrentTime = Simulation.Magnetostatic.Timesteppingdata.time(end);
        timestep = Simulation.Magnetostatic.Timesteppingdata.time(2)-Simulation.Magnetostatic.Timesteppingdata.time(1);
    else
        CurrentTime = 0;
        timestep = 0;
    end
end
Tag = get(hObject,'Tag');
time=get(hObject,'String');
[time status]=str2num(time);
if status
    srt_time=time2str(time,timestep,CurrentTime);
else
    errordlg('Not a valid value.','PlotWizard Error','modal');
    if strcmp(Tag,'edit_an_time_start')
        srt_time=time2str(0,timestep,CurrentTime);
    elseif strcmp(Tag,'edit_an_time_stop')
        srt_time=time2str(CurrentTime,timestep,CurrentTime);
    end
end
set(hObject,'String',srt_time);


function str_time = time2str(time,timestep,CurrentTime)
if CurrentTime==0
    str_time='0';
    return
end
time=round(time/timestep)*timestep;

if time>CurrentTime
    time=CurrentTime;
end
if time<timestep
    time=0;    
end
if time==0
    str_time='0';
    return
end
prec=1;
while 1
    temp=timestep*10^prec;
    if temp==round(temp) || prec==15, break, end
    prec=prec+1;
end
str_time=num2str(time,['%11.' num2str(prec) 'f']);


% --- Executes on button press in pushbutton_ag_plot.
function pushbutton_ag_plot_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_ag_plot (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
ag_plot(handles);


function [h_output]=ag_plot(handles,time,hide)
motoranalysishandles = guidata(handles.motoranalysis);
if get(motoranalysishandles.togglebutton_dynamicFEA,'Value')
    analysistype='dynamicFEA';
elseif get(motoranalysishandles.togglebutton_MS,'Value')
    analysistype='magnetostatic';
else
    return
end
if isempty(motoranalysishandles.File)
    errordlg('No simulation file opened.','PlotWizard Error','modal');
    h_output=-1;
    return;
end
Simulation = motoranalysishandles.Simulation;
if strcmp(analysistype,'dynamicFEA')
    if isempty(Simulation.DynamicFEA.time)
        errordlg('No simulation data to plot.','PlotWizard Error','modal');
        return;    
    end
elseif strcmp(analysistype,'magnetostatic')
    if isempty(Simulation.Magnetostatic.Timesteppingdata)
        errordlg('No simulation data to plot.','PlotWizard Error','modal');
        return; 
    end
end
SourceList = get(handles.pup_source,'String');
index = get(handles.pup_source,'Value');
datadir = SourceList{index,1};
l=Simulation.Geometry.l/1000;
if strcmp(analysistype,'dynamicFEA')
    timestep = Simulation.Settings.DynamicFEA.DF_timestep;
    if isempty(Simulation.DynamicFEA.time)
        CurrentTime=0;
    else
        CurrentTime=Simulation.DynamicFEA.time(end)-Simulation.DynamicFEA.time(1);
    end
    % CurrentTime = Simulation.DynamicFEA.CurrentTime;
    % CurrentTime = CurrentTime-timestep;
elseif strcmp(analysistype,'magnetostatic')
    if length(Simulation.Magnetostatic.Timesteppingdata.time)>1
        CurrentTime = Simulation.Magnetostatic.Timesteppingdata.time(end);
        timestep = Simulation.Magnetostatic.Timesteppingdata.time(2)-Simulation.Magnetostatic.Timesteppingdata.time(1);
    else
        CurrentTime = 0;
        timestep = 0;
    end
end
nt_=size(Simulation.Mesh.t,2);
nsubplots=handles.ag_nsubplots;
if isempty(nsubplots)
    h_output=-1;
    return
end
method=get(handles.pup_interpmethod,'String');
index=get(handles.pup_interpmethod,'Value');
method=method(index);
plotcolor='bgrcmyk';
h_output=figure('Name','Air gap distribution plot');
if exist('hide','var')
    set(h_output,'Visible','off');
end
time_='';
for i=1:length(nsubplots)
    icolor=1;
    ind=nsubplots(i);
    if nargin==1
        time=get(getfield(handles,['edit_ag_time' num2str(ind)]),'String');
    end
    iSlice=get(getfield(handles,['pup_ag_slice' num2str(ind)]),'Value');
    if ~strcmp(time_,time)
        loadfile=0;
        if strcmp(analysistype,'dynamicFEA')
            if str2num(time)+0.1*timestep<CurrentTime     % if time~=CurrentTime
                loadfile=1;
            end
        elseif strcmp(analysistype,'magnetostatic')
            if str2num(time)~=0
                loadfile=1;
                ShaftPosition=[0 0];
            end
        end
        if loadfile
            try
                load([datadir '\' time '.mat']);
            catch
                errordlg(['Unable to read file ' datadir '\' time '.mat : No such file or directory.'],'PlotWizard Error','modal');
                close(h_output);
                h_output=-1;
                return;
            end
        else
            if strcmp(analysistype,'dynamicFEA')
                ShaftPosition=Simulation.Private.ShaftPosition;
                A=Simulation.Private.A;
                cell_p=Simulation.Private.cell_p0;
                cell_t=Simulation.Private.cell_t0;
            elseif strcmp(analysistype,'magnetostatic')
                ShaftPosition=[0 0];
                A=Simulation.Magnetostatic.Timesteppingdata.field.A;
                cell_p=Simulation.Magnetostatic.Timesteppingdata.field.cell_p;
                cell_t=Simulation.Magnetostatic.Timesteppingdata.field.cell_t;
            end
        end
        if ~exist('A','var') || ~exist('cell_p','var') || ~exist('cell_t','var')
            errordlg(['File ' datadir '\' time '.mat is not correct.'],'PlotWizard Error','modal');
            close(h_output);
            h_output=-1;
            return;
        end
    end
    plotstr=get(getfield(handles,['edit_ag_vars' num2str(ind)]),'String');
    [nper periodicity] = VerifyPerBndCnd(Simulation.Geometry.Ns,Simulation.Mesh.nPolePairs,Simulation.Mesh.perbndcnd);
    if isempty(nper), return; end
    if findstr(plotstr,'flux')
        [phi flux]=ag_getvar(A,cell_p,cell_t,l,nt_,ShaftPosition,iSlice,'flux',method,nper,periodicity);
    end
    if findstr(plotstr,'Bn')
        [phi Bn]=ag_getvar(A,cell_p,cell_t,l,nt_,ShaftPosition,iSlice,'Bn',method,nper,periodicity);
    end
    if findstr(plotstr,'Bt')
        [phi Bt]=ag_getvar(A,cell_p,cell_t,l,nt_,ShaftPosition,iSlice,'Bt',method,nper,periodicity);
    end
    if findstr(plotstr,'Bm')
        [phi Bm]=ag_getvar(A,cell_p,cell_t,l,nt_,ShaftPosition,iSlice,'Bm',method,nper,periodicity);
    end
    if findstr(plotstr,'mmf')
        [phi mmf]=ag_getvar(A,cell_p,cell_t,l,nt_,ShaftPosition,iSlice,'mmf',method,nper,periodicity);
    end
    if findstr(plotstr,'Fn')
        [phi Fn]=ag_getvar(A,cell_p,cell_t,l,nt_,ShaftPosition,iSlice,'Fn',method,nper,periodicity);
    end
    subtitle=plotstr;
    % plotting
    mu0 = 4*pi*(10.^(-7));                      % permeability of free space
    Legend=[];
    subplot(length(nsubplots),1,i);
    plottype=get(getfield(handles,['pup_ag_plottype' num2str(ind)]),'String');
    value=get(getfield(handles,['pup_ag_plottype' num2str(ind)]),'Value');
    plottype=plottype(value);
    hold on
    while 1
        % plot string parsing
        indstr_comma=findstr(plotstr,','); if ~isempty(indstr_comma), indstr_comma=indstr_comma(1); end
        indstr_semi=findstr(plotstr,';'); if ~isempty(indstr_semi), indstr_semi=indstr_semi(1); end
        indstr_space=findstr(plotstr,';'); if ~isempty(indstr_space), indstr_space=indstr_space(1); end
        indstr=min([indstr_comma indstr_semi indstr_space]);
        if ~isempty(indstr)
            plotstr_n=plotstr(1:indstr-1); 
            plotstr(1:indstr)=[];
        else
            plotstr_n=plotstr;
            plotstr=[];
        end
        if ~isempty(plotstr_n), plotstr_n=strtrim(plotstr_n); end
        if ~isempty(plotstr_n)
            try
                Color=plotcolor(icolor);
                icolor=icolor+1;
                if icolor>length(plotcolor), icolor=1; end
                if strcmp(plottype,'distribution')
                    eval(['plot(phi,' plotstr_n ',Color);']);
                elseif strcmp(plottype,'spectrum')
                    eval(['[hn,signature]=Spectrum(phi,' plotstr_n ',ShaftPosition,method);']);
                    Xshift=0.1*(icolor-2);
                    if icolor>4, Xshift=0; end
                    bar(hn+Xshift,signature,Color);
                end
                Legend=strvcat(Legend,plotstr_n);
            catch
                errordlg(['??? Subplot ' num2str(i) ' - "' plotstr_n '": Unable to plot.'],'PlotWizard Error','modal');
                close(h_output);
                h_output=-1;
                return;
            end
        else
            break
        end
    end
    hold off
    grid;
    x_lim=get(getfield(handles,['edit_ag_xlim' num2str(ind)]),'String'); x_lim=str2num(x_lim);
    if ~isempty(x_lim)
        if length(x_lim)==1
            x_lim=[0 x_lim];
        end
        xlim(x_lim);
    end
    y_lim=get(getfield(handles,['edit_ag_ylim' num2str(ind)]),'String'); y_lim=str2num(y_lim);
    if ~isempty(y_lim)
        if length(y_lim)==1
            y_lim=[0 y_lim];
        end
        ylim(y_lim);
    end
    if strcmp(plottype,'distribution')
        set(gca,'XTick',-pi:pi/2:pi);
        set(gca,'XTickLabel',{'-pi','-pi/2','0','pi/2','pi'});
        xlabel('Angular position');
        if isempty(x_lim), xlim([-pi pi]); end
    elseif strcmp(plottype,'spectrum')
        xlabel('Harmonic number');
    end
    if strcmp(analysistype,'dynamicFEA')
        title(['Dynamic Finite Element Analysis: time = ' time ', Slice = ' num2str(iSlice) '; ' plottype{1,1}]);
    elseif strcmp(analysistype,'magnetostatic')
        title(['Magnetostatic analysis: time = ' time ', Slice = ' num2str(iSlice) '; ' plottype{1,1}]);
    end
    ShowLegend=get(handles.checkbox_ag_legend,'Value');
    if ShowLegend
        if ~isempty(Legend)
            legend(Legend);
        end
    end
    time_=time;
end


function [hn,signature]=Spectrum(phi,y,ShaftPosition,method)
dphi=diff(phi);
dphi=abs(dphi-sparse(find(dphi>pi),1,ones(length(find(dphi>pi)),1)*2*pi,length(dphi),1));
mean_dphi=mean(dphi);
mean_dphi=2*pi/round(2*pi/mean_dphi);
phi_interp=-pi:mean_dphi:pi;
if strcmp(method,'Linear')
    y = interp1([phi(end)-2*pi; phi; phi(1)+2*pi],[y(end); y; y(1)],phi_interp');
elseif strcmp(method,'Spline')
    y = Spline([phi(end)-2*pi; phi; phi(1)+2*pi],[y(end); y; y(1)],phi_interp');
else
    error('Undefined interpolation method');
end
n = length(y);
F = fft(y);
Fm = 2*abs(F)/n;
signature = Fm;
hn = 0:n-1;


% --- Executes on button press in pushbutton_cs_plot.
function pushbutton_cs_plot_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_cs_plot (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
cs_plot(handles);


function [h_output]=cs_plot(handles,time,figures)
motoranalysishandles = guidata(handles.motoranalysis);
if get(motoranalysishandles.togglebutton_dynamicFEA,'Value')
    analysistype='dynamicFEA';
elseif get(motoranalysishandles.togglebutton_MS,'Value')
    analysistype='magnetostatic';
else
    return
end
if isempty(motoranalysishandles.File)
    errordlg('No simulation file opened.','PlotWizard Error','modal');
    h_output=-1;
    return;
end
Simulation = motoranalysishandles.Simulation;
if strcmp(analysistype,'dynamicFEA')
    if isempty(Simulation.DynamicFEA.time)
        errordlg('No simulation data to plot.','PlotWizard Error','modal');
        return;    
    end
elseif strcmp(analysistype,'magnetostatic')
    if isempty(Simulation.Magnetostatic.Timesteppingdata)
        errordlg('No simulation data to plot.','PlotWizard Error','modal');
        return; 
    end
    % if length(Simulation.Magnetostatic.Timesteppingdata.time)<2
    if isempty(Simulation.Magnetostatic.Timesteppingdata.time)
        errordlg('Not enough simulation data.','PlotWizard Error','modal');
        return; 
    end
end
SourceList = get(handles.pup_source,'String');
index = get(handles.pup_source,'Value');
datadir = SourceList{index,1};
if strcmp(analysistype,'dynamicFEA')
    timestep = Simulation.Settings.DynamicFEA.DF_timestep;
    if isempty(Simulation.DynamicFEA.time)
        CurrentTime=0;
    else
        CurrentTime=Simulation.DynamicFEA.time(end)-Simulation.DynamicFEA.time(1);
    end
    % CurrentTime = Simulation.DynamicFEA.CurrentTime;
    % CurrentTime = CurrentTime-timestep;
    timearray = Simulation.DynamicFEA.time;
elseif strcmp(analysistype,'magnetostatic')
    CurrentTime = Simulation.Magnetostatic.Timesteppingdata.time(end);
    timearray = Simulation.Magnetostatic.Timesteppingdata.time;
    if length(timearray)>1
        timestep = timearray(2)-timearray(1);
    else
        timestep=0;
    end
end
Geometry = Simulation.Geometry;
l=Geometry.l/1000;
Mesh = Simulation.Mesh;
[nper, periodicity] = VerifyPerBndCnd(Geometry.Ns,Mesh.nPolePairs,Mesh.perbndcnd);
nSlices = Simulation.Mesh.nSlices;
nt_=size(Simulation.Mesh.t,2);
nfigures=handles.cs_nfigures;
time_='';
h_output=[];
for i=1:length(nfigures)
    ind=nfigures(i);
    if nargin==1
        time=get(getfield(handles,['edit_cs_time' num2str(ind)]),'String');
    end
    iSlice=get(getfield(handles,['pup_cs_slice' num2str(ind)]),'Value');
    if ~strcmp(time_,time)
        loadfile=0;
        if strcmp(analysistype,'dynamicFEA')
            if str2num(time)+0.1*timestep<CurrentTime     % if time~=CurrentTime
                loadfile=1;
            end
        elseif strcmp(analysistype,'magnetostatic')
            if str2num(time)~=0
                loadfile=1;
            end
        end
        if loadfile
            try
                load([datadir '\' time '.mat']);
            catch
                errordlg(['Unable to read file ' datadir '\' time '.mat : No such file or directory.'],'PlotWizard Error','modal');
                h_output=-1;
                return;
            end
            if ~exist('A','var') || ~exist('cell_p','var') || ~exist('cell_t','var') || ~exist('cell_Nu','var') || ~exist('cell_BBr','var')
                errordlg(['File ' datadir '\' time '.mat is not correct.'],'PlotWizard Error','modal');
                h_output=-1;
                return;
            end
        else
            if strcmp(analysistype,'dynamicFEA')
                A=Simulation.Private.A;
                cell_p=Simulation.Private.cell_p0;
                cell_t=Simulation.Private.cell_t0;
                cell_Nu=Simulation.Private.cell_Nu0;
                cell_BBr=Simulation.Private.cell_BBr0;
            elseif strcmp(analysistype,'magnetostatic')
                A=Simulation.Magnetostatic.Timesteppingdata.field.A;
                cell_p=Simulation.Magnetostatic.Timesteppingdata.field.cell_p;
                cell_t=Simulation.Magnetostatic.Timesteppingdata.field.cell_t;
                cell_Nu=Simulation.Magnetostatic.Timesteppingdata.field.cell_Nu;
                cell_BBr=Simulation.Magnetostatic.Timesteppingdata.field.cell_BBr;
            end
        end
    end
    mu0 = 4*pi*(10.^(-7));               % permeability of free space
    p=cell_p{iSlice};                   % points of iSlice
    t=cell_t{iSlice};                   % triangles of iSlice
    e=Simulation.Mesh.e;
    if strcmp(analysistype,'dynamicFEA')
        Piron_density=Simulation.DynamicFEA.Piron_density;
    elseif strcmp(analysistype,'magnetostatic')
        Piron_density=Simulation.Magnetostatic.Timesteppingdata.field.Piron_density;
    end
    Np_slice=0;
    for n=1:iSlice
        np_slice=size(cell_p{n},2);
        Np_slice=Np_slice+np_slice;
    end
    Aplot=A(Np_slice-np_slice+1:Np_slice);   % magnetic vector potential of iSlice
    Nu=cell_Nu{iSlice,1};               % magnetic reluctivity of iSlice (reciprocal of the magnetic permeability)
    mu=1./Nu/mu0;                        % magnetic permeability of iSlice
    Br=cell_BBr{iSlice,1};              % permanent magnets remanence flux density    
    plotqnt=get(getfield(handles,['pup_cs_quantity' num2str(ind)]),'Value');
    if plotqnt==8
        % Magnetic field energy density
        Wmf=MagFieldEnergy(p,t,Aplot,Br,Nu,Simulation.Private.BHcurve,Simulation.Private.Subdomains,l,ones(1,size(t,2)),nSlices,10^-4);
    else
        Wmf=[];
    end
    if plotqnt==11 || plotqnt==12
        [Ax,Ay]=gradA(p,t,Aplot);
        Bx=Ay;
        By=-Ax;
        [Hdemag, Hdemag_percent] = DemagFieldDistr(Bx,By,t,Br,Nu,Simulation.Private.Subdomains,Simulation.Private.MaterialProperties);
    else
        Hdemag=[]; Hdemag_percent=[];
    end
    p(find(abs(p)<eps))=0;
    fullview=get(handles.checkbox_fullview,'Value');
    if fullview && nper>1
        p_=p; t_=t; e_=e; Aplot_=Aplot; mu_=mu; Nu_=Nu; Wmf_=Wmf; Hdemag_=Hdemag; Hdemag_percent_=Hdemag_percent;
        if ~isempty(Piron_density)
            Piron_density=[Piron_density; zeros(size(t,2)-length(Piron_density),1)]; 
        end
        Piron_density_=Piron_density;
        for n=1:nper-1
            phi=2*pi*n/nper;
            RM=[cos(-phi) sin(-phi);
                -sin(-phi) cos(-phi)];      % clockwise rotation matrix
            p=[p RM'*p_];
            t=[t [t_(1:3,:)+n*size(p_,2); t_(4,:)]];
            e=[e [e_(1:2,:)+n*size(p_,2); e_(3:end,:)]];
            Aplot=[Aplot; Aplot_*(periodicity^n)];
            mu=[mu mu_];
            Nu=[Nu Nu_];
            Wmf=[Wmf Wmf_];
            Piron_density=[Piron_density; Piron_density_];
            Hdemag=[Hdemag Hdemag_];
            Hdemag_percent=[Hdemag_percent Hdemag_percent_];
        end
    end
    ar=(trgdata(p,t))';                  % triangles area
    String=get(getfield(handles,['pup_cs_quantity' num2str(ind)]),'String');
    Name=String{plotqnt,1};
    if strcmp(Name,'None'), Name='Motor cross-section'; end
    if strcmp(analysistype,'dynamicFEA')
        Name=[Name '; Dynamic Finite Element Analysis: time = ' time ' sec, Slice = ' num2str(iSlice)];
    elseif strcmp(analysistype,'magnetostatic')
        Name=[Name '; Magnetostatic analysis: time = ' time ' sec, Slice = ' num2str(iSlice)];
    end
    h=figure('Name',Name);
    set(h,'Visible','off');
    h_output=[h_output h];
    hold on
    if ~verLessThan('matlab', '8.4.0')
        set(gca,'SortMethod','depth')
    end
    fieldplot(p,e,[]);    % draw motor geometry
    opts=get(getfield(handles,['pup_cs_opts' num2str(ind)]),'Value');
    switch opts
        case 2
        % draw flux lines
        nfluxlevels=get(handles.edit_nfluxlevels,'String');
        [nfluxlevels status]=str2num(nfluxlevels);
        if ~status, nfluxlevels=20; end
        fieldplot(p,[],t,'xydata',Aplot,'xystyle','off','contour','on','levels',nfluxlevels,'colorbar','off');
        case 3 
            % draw flux arrows
            % triangles midpoints
            xm=p(1,t(1,:))+((p(1,t(2,:))+p(1,t(3,:)))/2-p(1,t(1,:)))*2/3;
            ym=p(2,t(1,:))+((p(2,t(2,:))+p(2,t(3,:)))/2-p(2,t(1,:)))*2/3;
            [Ax,Ay]=gradA(p,t,Aplot);
            % flux density components
            Bx=Ay;
            By=-Ax;
            quiver(xm,ym,Bx,By);
    end
    set(findobj(gca,'Type','line'),'Color','k');
    if plotqnt==2
        % Magnetic vector potential
        fieldplot(p,e,t,'xydata',Aplot,'xystyle','flat','colormap','cool');
    elseif plotqnt==3
        % Magnetic flux density
        if ~exist('Ax','var')
            [Ax,Ay]=gradA(p,t,Aplot);
            Bx=Ay;
            By=-Ax;
        end
        B=sqrt(Bx.^2+By.^2);
        fieldplot(p,e,t,'xydata',B,'xystyle','flat','colormap','jet');
    elseif plotqnt==4
        % Magnetic field intensity
        if ~exist('Ax','var')
            [Ax,Ay]=gradA(p,t,Aplot);
            Bx=Ay;
            By=-Ax;
        end
        B=sqrt(Bx.^2+By.^2);
        H=B./mu/mu0;
        fieldplot(p,e,t,'xydata',H,'xystyle','flat','colormap','jet');
    elseif plotqnt==5
        % Relative permeability
        it_core = getitcore(t,Simulation.Private.Subdomains);   % indices of iron core triangles
        fieldplot(p,e,t(:,it_core),'xydata',mu(it_core),'xystyle','flat','colormap','jet');
    elseif plotqnt==6 || plotqnt==9     % Stator current density || Joule loss density
        if strcmp(analysistype,'dynamicFEA')
            Schematic=Simulation.Private.CircuitDynFEA.Schematic;
        elseif strcmp(analysistype,'magnetostatic')
            Schematic=Simulation.Private.Circuit.Schematic;
        end
        if str2num(time)<eps
            itime=1;
        else
            itime=find(timearray>str2num(time)-0.1*timestep & timearray<str2num(time)+0.1*timestep);
        end
        if ~isempty(itime)
            % stator currents
            if strcmp(analysistype,'dynamicFEA')
                Ia=Simulation.DynamicFEA.Ia(:,itime);
                Ib=Simulation.DynamicFEA.Ib(:,itime);
                Ic=Simulation.DynamicFEA.Ic(:,itime);
            elseif strcmp(analysistype,'magnetostatic')
                Ia=Simulation.Magnetostatic.Timesteppingdata.Ia(:,itime);
                Ib=Simulation.Magnetostatic.Timesteppingdata.Ib(:,itime);
                Ic=Simulation.Magnetostatic.Timesteppingdata.Ic(:,itime);
                Npp=Simulation.Private.Circuit.Npp;
                Ia=ones(Npp,1)*Ia/Npp;
                Ib=ones(Npp,1)*Ib/Npp;
                Ic=ones(Npp,1)*Ic/Npp;
            else
                error('Something goes wrong');
            end
        else
            error('Something goes wrong');
        end
        js=zeros(nt_,1);
        for nBranch=1:length(Schematic)
            Branch=Schematic{nBranch,1};
            Components=Branch.Components;
            for n=1:length(Components)
                component=Components{n,1};
                if strcmp(component.type,'coil')
                    npath=component.value.npath;
                    if strcmp(component.value.phase,'a')
                        js=js+component.value.I2j*Ia(npath);
                    elseif strcmp(component.value.phase,'b')
                        js=js+component.value.I2j*Ib(npath);
                    elseif strcmp(component.value.phase,'c')
                        js=js+component.value.I2j*Ic(npath);
                    end
                end
            end
        end
        if fullview && nper>1
            js=[js; zeros(size(t_,2)-size(js,1),1)];
            js_=js;
            for n=1:nper-1
                js=[js; js_*(periodicity^n)];
            end
        end
        if plotqnt==6     % Stator current density
            fieldplot(p,e,t(:,find(js)),'xydata',js(find(js)),'xystyle','flat','colormap','cool');
        elseif plotqnt==9                                 % Joule loss density
            ar=ar(1:length(js));
            JouleLoss=zeros(size(js));
            ks=Simulation.Windings.ks;                     % stator winding material conductivity
            fillfactor=Simulation.Windings.fillfactor;     % stator slot fill factor (coil fill factor for dxf stator)
            if ~isempty(ks) && ~isempty(fillfactor)
                JouleLoss = JouleLoss+(l/nSlices)*js.^2*(1/ks).*ar*fillfactor;
            else
                disp('No enough data to plot Joule loss density, check stator winding material conductivity or stator slot/coil fill factor')
            end
            JouleLossDensity=JouleLoss./(ar*l/nSlices);
            fieldplot(p,e,t(:,find(JouleLossDensity)),'xydata',JouleLossDensity(find(JouleLossDensity)),'xystyle','flat','colormap','jet');
        end
    elseif plotqnt==7
        % Squared magnetic flux density
        if ~exist('Ax','var')
            [Ax,Ay]=gradA(p,t,Aplot);
            Bx=Ay;
            By=-Ax;
        end
        B=sqrt(Bx.^2+By.^2);
        fieldplot(p,e,t,'xydata',B.^2,'xystyle','flat','colormap','jet');    
    elseif plotqnt==8
        % Magnetic field energy density
        fieldplot(p,e,t,'xydata',Wmf,'xystyle','flat','colormap','jet');
    elseif plotqnt==10
        % Iron loss density
        it_core = getitcore(t,Simulation.Private.Subdomains);   % indices of iron core triangles
        if isempty(Piron_density)
            title('No iron loss computed');
        else
            fieldplot(p,e,t(:,it_core),'xydata',Piron_density(it_core),'xystyle','flat','colormap','jet');
        end
    elseif plotqnt==11
        % demagnetizing field in A/m
        fieldplot(p,e,t(:,abs(Hdemag)>0),'xydata',Hdemag(abs(Hdemag)>0),'xystyle','flat','colormap','jet');
    elseif plotqnt==12
        % demagnetizing field in percentage of intrinsic coercivity Hcj
        fieldplot(p,e,t(:,abs(Hdemag_percent)>0),'xydata',Hdemag_percent(abs(Hdemag_percent)>0),'xystyle','flat','colormap','jet');        
    elseif plotqnt==13 
        % Finite element mesh
        fieldplot(p,e,t,'mesh','on');
    end
    axis equal    
    if strcmp(Simulation.Geometry.motortype,'Inner rotor')
        axislim=Simulation.Geometry.D1s/2/1000;
    elseif strcmp(Simulation.Geometry.motortype,'Outer rotor')
        axislim=max(Simulation.DXFrotor.geometry(10,:));
    end
    axis([-axislim axislim -axislim axislim]);
    hold off
    x_lim=get(getfield(handles,['edit_cs_xlim' num2str(ind)]),'String'); x_lim=str2num(x_lim);
    if ~isempty(x_lim)
        if length(x_lim)==1
            x_lim=[0 x_lim];
        end
        xlim(x_lim);
    end
    y_lim=get(getfield(handles,['edit_cs_ylim' num2str(ind)]),'String'); y_lim=str2num(y_lim);
    if ~isempty(y_lim)
        if length(y_lim)==1
            y_lim=[0 y_lim];
        end
        ylim(y_lim);
    end
    z_lim=get(getfield(handles,['edit_cs_zlim' num2str(ind)]),'String'); z_lim=str2num(z_lim);
    if ~isempty(z_lim)
        if length(z_lim)==1
            z_lim=[0 z_lim];
        end
        caxis(z_lim);
    end
    time_=time;
end
pass=length(h_output);
for i=1:length(h_output)
    if exist('figures','var')
        try
            Visible=get(figures(i),'Visible');
            if strcmp(Visible,'on')
                while 1
                    if strcmp(get(figures(i),'Pointer'),'arrow')
                        break
                    else
                        pause(2);
                    end
                end
                XLim=get(get(figures(i),'CurrentAxes'),'XLim');
                YLim=get(get(figures(i),'CurrentAxes'),'YLim');
                clf(figures(i));
                if verLessThan('matlab', '8.4.0')
                    copyobj(get(h_output(i),'CurrentAxes'),figures(i));
                    set(get(figures(i),'CurrentAxes'),'XLim',XLim);
                    set(get(figures(i),'CurrentAxes'),'YLim',YLim);
                    copyobj(findobj(get(h_output(i),'Children'),'flat','Tag','Colorbar'),figures(i));    % copy Colorbar
                else
                    copy1=get(h_output(i),'CurrentAxes');
                    copy2=findobj(get(h_output(i),'Children'),'flat','Tag','Colorbar');
                    copyobj([copy1 copy2],figures(i));
                    set(get(figures(i),'CurrentAxes'),'XLim',XLim);
                    set(get(figures(i),'CurrentAxes'),'YLim',YLim);
                end
                set(figures(i),'Name',get(h_output(i),'Name'));
            else                % hidden figure got a handle of the closed figure 
                pass=pass-1;
            end
        catch
            pass=pass-1;
        end
        close(h_output(i));
    else
        set(h_output(i),'Visible','on');
        pass=1;
    end
end
if pass==0          % all figures are closed
    h_output=-1;
end

% --- Executes on button press in pushbutton_animate.
function pushbutton_animate_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_animate (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
motoranalysishandles = guidata(handles.motoranalysis);
if get(motoranalysishandles.togglebutton_dynamicFEA,'Value')
    analysistype='dynamicFEA';
elseif get(motoranalysishandles.togglebutton_MS,'Value')
    analysistype='magnetostatic';
else
    return
end
if isempty(motoranalysishandles.File)
    errordlg('No simulation file opened.','PlotWizard Error','modal');
    return;
end
Simulation = motoranalysishandles.Simulation;
if strcmp(analysistype,'dynamicFEA')
    if isempty(Simulation.DynamicFEA.time)
        errordlg('No simulation data for animation.','PlotWizard Error','modal');
        return;    
    end
elseif strcmp(analysistype,'magnetostatic')
    if isempty(Simulation.Magnetostatic.Timesteppingdata)
        errordlg('No simulation data for animation.','PlotWizard Error','modal');
        return; 
    end
    if length(Simulation.Magnetostatic.Timesteppingdata.time)<2
        errordlg('No simulation data for animation.','PlotWizard Error','modal');
        return; 
    end
end
if strcmp(analysistype,'dynamicFEA')
    timestep = Simulation.Settings.DynamicFEA.DF_timestep;
    if isempty(Simulation.DynamicFEA.time)
        CurrentTime=0;
    else
        CurrentTime=Simulation.DynamicFEA.time(end)-Simulation.DynamicFEA.time(1);
    end
    % CurrentTime = Simulation.DynamicFEA.CurrentTime;
    % CurrentTime = CurrentTime-timestep;
elseif strcmp(analysistype,'magnetostatic')
    CurrentTime = Simulation.Magnetostatic.Timesteppingdata.time(end);
    timestep = Simulation.Magnetostatic.Timesteppingdata.time(2)-Simulation.Magnetostatic.Timesteppingdata.time(1);
end

starttime=get(handles.edit_an_time_start,'String');
starttime=str2num(starttime);
stoptime=get(handles.edit_an_time_stop,'String');
stoptime=str2num(stoptime)+timestep/2;
skip=get(handles.edit_skip,'String');
[skip status]=str2num(skip);
if ~status || skip<0
    errordlg('Not a valid value for Skip.','PlotWizard Error','modal');
    return
end
disptime=get(handles.edit_disptime,'String');
[disptime status]=str2num(disptime);
if ~status || disptime<0
    errordlg('Not a valid value for Frame display time.','PlotWizard Error','modal');
    return
end
include_ag=get(handles.checkbox_include_ag,'Value');
include_cs=get(handles.checkbox_include_cs,'Value');
time=starttime;
set(handles.pushbutton_animate,'Enable','off');
while (time<stoptime)
    ticid=tic;
    if ~include_ag && ~include_cs
        close(findobj('Visible','off','Type','figure'));    % close all hidden figures
        set(handles.pushbutton_animate,'Enable','on');
        disp('Animation completed');
        return;
    end
    srt_time=time2str(time,timestep,CurrentTime);
    if ~exist('figures','var') || ~exist('wnd_ag_plot','var')
        figures=[]; wnd_ag_plot=[];
        if include_cs
            figures=cs_plot(handles,srt_time);
            drawnow
            if figures==-1
                include_cs=0;
                figures=[];
            end
        end
        if include_ag
            wnd_ag_plot=ag_plot(handles,srt_time);
            drawnow
            if wnd_ag_plot==-1
                include_ag=0;
                wnd_ag_plot=[];
            end            
        end
        if get(handles.checkbox_positionfigures,'Value');
            positionwnd([figures wnd_ag_plot]);
        end
    else
        if include_ag
            ag_output=ag_plot(handles,srt_time,1);
            drawnow
            if ag_output==-1
                include_ag=0;
            end
        end
        if include_cs
            cs_output=cs_plot(handles,srt_time,figures);
            drawnow
            if cs_output==-1
                include_cs=0;
            end
        end
        if include_ag
            try
                Visible=get(wnd_ag_plot,'Visible');
                if strcmp(Visible,'off')
                    include_ag=0;
                else
                    while 1
                        if strcmp(get(wnd_ag_plot,'Pointer'),'arrow')
                            break
                        else
                            pause(2);
                        end
                    end
                    Axes=findobj(get(wnd_ag_plot,'Children'),'Type','axes');
                    XLim=[]; YLim=[];
                    for i=1:length(Axes)
                        XLim=[XLim; get(Axes(i),'XLim')];
                        YLim=[YLim; get(Axes(i),'YLim')];
                    end
                    clf(wnd_ag_plot);
                    copyobj(get(ag_output,'Children'),wnd_ag_plot);
                    set(wnd_ag_plot,'Name',get(ag_output,'Name'));
                    Axes=findobj(get(wnd_ag_plot,'Children'),'Type','axes');
                    for i=1:length(Axes)
                        set(Axes(i),'XLim',XLim(i,:));
                        % set(Axes(i),'YLim',YLim(i,:));
                    end                    
                end
            catch
                include_ag=0;
            end
            close(ag_output);
        end
    end
    time=time+(skip+1)*timestep;
    calctime=toc(ticid);
    calctime=calctime*1000;  % ms
    if calctime<disptime
        pause((disptime-calctime)/1000);
    end
    while get(handles.togglebutton_pause,'Value')
        pause(0.5);
    end
end
close(findobj('Visible','off','Type','figure'));    % close all hidden figures
set(handles.pushbutton_animate,'Enable','on');
disp('Animation completed');

function positionwnd(h_wnd)
set(0,'Units','pixels') 
scnsize = get(0,'ScreenSize');
scnwidth=scnsize(3); scnheight=scnsize(4);
% rect = [left, bottom, width, height]
if length(h_wnd)==1
    set(h_wnd,'OuterPosition',scnsize);
elseif length(h_wnd)==2
    pos=[1          1 scnwidth/2 scnheight;
         scnwidth/2 1 scnwidth/2 scnheight];
    set(h_wnd(1),'OuterPosition',pos(1,:));
    set(h_wnd(2),'OuterPosition',pos(2,:));
elseif length(h_wnd)>=3 && length(h_wnd)<=4
    pos=[1          scnheight/2 scnwidth/2 scnheight/2;
         scnwidth/2 scnheight/2 scnwidth/2 scnheight/2;
         1          1           scnwidth/2 scnheight/2;
         scnwidth/2 1           scnwidth/2 scnheight/2;];
    for i=1:length(h_wnd) 
        set(h_wnd(i),'OuterPosition',pos(i,:));
    end
elseif length(h_wnd)>=5 && length(h_wnd)<=6
    % rect = [left, bottom, width, height]
    pos=[1            scnheight/2 scnwidth/3 scnheight/2;
         scnwidth/3   scnheight/2 scnwidth/3 scnheight/2;
         2*scnwidth/3 scnheight/2 scnwidth/3 scnheight/2;
         1            1           scnwidth/3 scnheight/2;
         scnwidth/3   1           scnwidth/3 scnheight/2;
         2*scnwidth/3 1           scnwidth/3 scnheight/2];
    for i=1:length(h_wnd)
        if i>6, return; end
        set(h_wnd(i),'OuterPosition',pos(i,:));
    end    
end


% --- Executes on button press in pushbutton_tm_changeplot1.
function pushbutton_tm_changeplot_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_tm_changeplot1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Tag = get(hObject,'Tag');
if strcmp(Tag(1:24),'pushbutton_tm_changeplot')
    ind=str2num(Tag(25:end));
    varslist=tm_varslist(handles);
    if ~isempty(varslist)
        plotexp=tm_changeplot('varslist',varslist);
        if ~isempty(plotexp)
            set(getfield(handles,['edit_tm_plotexp' num2str(ind)]),'String',plotexp);
            guidata(hObject, handles);
        end
    end
end


function [cell_varslist]=tm_varslist(handles)

motoranalysishandles = guidata(handles.motoranalysis);
cell_varslist=[];
if isempty(motoranalysishandles.File)
    errordlg('No simulation file opened.','PlotWizard Error','modal');
    return;
end
Simulation = motoranalysishandles.Simulation;
varslist=[];
if get(motoranalysishandles.togglebutton_dynamicFEA,'Value')               % dynamicFEA
    if isempty(Simulation.DynamicFEA.time)
        errordlg('No simulation data to plot.','PlotWizard Error','modal');
        return;    
    end
    varslist=strvcat(varslist,'Ia (Stator phase current, phase A, [A])');
    varslist=strvcat(varslist,'Ib (Stator phase current, phase B, [A])');
    varslist=strvcat(varslist,'Ic (Stator phase current, phase C, [A])');
    Npp_a=size(Simulation.DynamicFEA.Ia,1);    % number of parallel paths of phase a
    if Npp_a>1
        for i=1:Npp_a
            varslist=strvcat(varslist,['Ia' num2str(i) ' (Stator phase current of parallel path ' num2str(i) ', phase A, [A])']);
        end
    end
    Npp_b=size(Simulation.DynamicFEA.Ib,1);    % number of parallel paths of phase b
    if Npp_b>1    % number of parallel paths of phase b
        for i=1:Npp_b
            varslist=strvcat(varslist,['Ib' num2str(i) ' (Stator phase current of parallel path ' num2str(i) ', phase B, [A])']);
        end
    end
    Npp_c=size(Simulation.DynamicFEA.Ic,1);    % number of parallel paths of phase c
    if Npp_c>1    % number of parallel paths of phase c
        for i=1:Npp_c
            varslist=strvcat(varslist,['Ic' num2str(i) ' (Stator phase current of parallel path ' num2str(i) ', phase C, [A])']);
        end
    end
    varslist=strvcat(varslist,'Id (Phase current, d-axis [A])');
    varslist=strvcat(varslist,'Iq (Phase current, q-axis, [A])');
    varslist=strvcat(varslist,'Va (Phase voltage, phase A, [V])');
    varslist=strvcat(varslist,'Vb (Phase voltage, phase B, [V])');
    varslist=strvcat(varslist,'Vc (Phase voltage, phase C, [V])');
    varslist=strvcat(varslist,'Vd (Phase voltage, d-axis [V])');
    varslist=strvcat(varslist,'Vq (Phase voltage, q-axis, [V])');
    varslist=strvcat(varslist,'Gamma (Effective advance angle, [electrical degrees])');
    varslist=strvcat(varslist,'BackEMFa (Phase back-EMF, phase A, [V])');
    varslist=strvcat(varslist,'BackEMFb (Phase back-EMF, phase B, [V])');
    varslist=strvcat(varslist,'BackEMFc (Phase back-EMF, phase C, [V])');
    varslist=strvcat(varslist,'BackEMFd (Phase back-EMF, d-axis, [V])');
    varslist=strvcat(varslist,'BackEMFq (Phase back-EMF, q-axis, [V])');    
    varslist=strvcat(varslist,'Pinput (Input apparent electrical power, [VA])');
    varslist=strvcat(varslist,'Pcons (Consumed apparent power, [VA])');
    varslist=strvcat(varslist,'Ps (Apparent power (real and reactive) consumed by a stator circuit, [VA])');
    varslist=strvcat(varslist,'Pmech (Mechanical power on the rotor shaft, [W])');
    varslist=strvcat(varslist,'Pmf (Time derivative of the magnetic field energy, [VAR])');
    varslist=strvcat(varslist,'MagnetLoss (Eddy current magnet loss), [W])');
    varslist=strvcat(varslist,'Torque (Electromagnetic torque, [N*m])');
    varslist=strvcat(varslist,'Load (Load torque on the motor shaft, [N*m])');
    varslist=strvcat(varslist,'Speed (Rotor speed, [RPM])');
    varslist=strvcat(varslist,'Rotang (Rotor angular position, [rad])');
    varslist=strvcat(varslist,'Torque_maxwell (Electromagnetic torque by Maxwell stress tensor, [N*m])');
    varslist=strvcat(varslist,'Torque_vwork (Electromagnetic torque by virtual work method, [N*m])');
    varslist=strvcat(varslist,'Torque_fluxlinkage (Electromagnetic torque by flux linkage and current, [N*m])');
    varslist=strvcat(varslist,'Torque_magnet (Magnet torque (by Maxwell stress tensor), [N*m])');
    varslist=strvcat(varslist,'Torque_reluctance (Reluctance torque (by Maxwell stress tensor), [N*m])');
    varslist=strvcat(varslist,'Fluxlinkage_a (Flux linkage, phase A, [Wb])');
    varslist=strvcat(varslist,'Fluxlinkage_b (Flux linkage, phase B, [Wb])');
    varslist=strvcat(varslist,'Fluxlinkage_c (Flux linkage, phase C, [Wb])');
    varslist=strvcat(varslist,'Fluxlinkage_d (Flux linkage, d-axis, [Wb])');
    varslist=strvcat(varslist,'Fluxlinkage_q (Flux linkage, q-axis, [Wb])');
    varslist=strvcat(varslist,'Fx (Radial electromagnetic force between stator and rotor along x-direction, [N])');
    varslist=strvcat(varslist,'Fy (Radial electromagnetic force between stator and rotor along y-direction, [N])');
    if ~isempty(Simulation.Userdata)
        Uservars = fieldnames(Simulation.Userdata);
        for i=1:length(Uservars)
            if length(Simulation.Userdata.(Uservars{i}))==length(Simulation.DynamicFEA.time)    % if variable is a time sequence array
                varslist=strvcat(varslist,[Uservars{i} ' (User defined variable)']);
            end
        end
    end
elseif get(motoranalysishandles.togglebutton_MS,'Value')                   % magnetostatic
    if isempty(Simulation.Magnetostatic.Timesteppingdata) || length(Simulation.Magnetostatic.Timesteppingdata.time)<2
        errordlg('No simulation data to plot.','PlotWizard Error','modal');
        return; 
    end
    varslist=strvcat(varslist,'Ia (Stator phase current, phase A, [A])');
    varslist=strvcat(varslist,'Ib (Stator phase current, phase B, [A])');
    varslist=strvcat(varslist,'Ic (Stator phase current, phase C, [A])');
    varslist=strvcat(varslist,'Id (Phase current, d-axis [A])');
    varslist=strvcat(varslist,'Iq (Phase current, q-axis, [A])');
    varslist=strvcat(varslist,'Va (Phase voltage, phase A, [V])');
    varslist=strvcat(varslist,'Vb (Phase voltage, phase B, [V])');
    varslist=strvcat(varslist,'Vc (Phase voltage, phase C, [V])');
    varslist=strvcat(varslist,'Vd (Phase voltage, d-axis [V])');
    varslist=strvcat(varslist,'Vq (Phase voltage, q-axis, [V])');
    varslist=strvcat(varslist,'Gamma (Effective advance angle, [electrical degrees])');
    varslist=strvcat(varslist,'BackEMFa (Phase back-EMF, phase A, [V])');
    varslist=strvcat(varslist,'BackEMFb (Phase back-EMF, phase B, [V])');
    varslist=strvcat(varslist,'BackEMFc (Phase back-EMF, phase C, [V])');
    varslist=strvcat(varslist,'BackEMFd (Phase back-EMF, d-axis, [V])');
    varslist=strvcat(varslist,'BackEMFq (Phase back-EMF, q-axis, [V])');
    varslist=strvcat(varslist,'Pinput (Input electrical power, [W])');
    varslist=strvcat(varslist,'Pmech (Mechanical power on the rotor shaft, [W])');
    varslist=strvcat(varslist,'Ps (Stator winding losses, [W])');
    varslist=strvcat(varslist,'MagnetLoss (Eddy current magnet loss), [W])');
    varslist=strvcat(varslist,'Torque_maxwell (Electromagnetic torque by Maxwell stress tensor, [N*m])');
    varslist=strvcat(varslist,'Torque_vwork (Electromagnetic torque by virtual work method, [N*m])');
    varslist=strvcat(varslist,'Torque_fluxlinkage (Electromagnetic torque by flux linkage and current, [N*m])');
    varslist=strvcat(varslist,'Torque_magnet (Magnet torque (by Maxwell stress tensor), [N*m])');
    varslist=strvcat(varslist,'Torque_reluctance (Reluctance torque (by Maxwell stress tensor), [N*m])');
    if any(isnan(Simulation.Magnetostatic.Timesteppingdata.Torque_cogging))
        varslist=strvcat(varslist,'[Not available] Torque_cogging (Cogging torque (by Maxwell stress tensor), [N*m])');
    else
        varslist=strvcat(varslist,'Torque_cogging (Cogging torque (by Maxwell stress tensor), [N*m])');
    end
    varslist=strvcat(varslist,'Fluxlinkage_a (Flux linkage, phase A, [Wb])');
    varslist=strvcat(varslist,'Fluxlinkage_b (Flux linkage, phase B, [Wb])');
    varslist=strvcat(varslist,'Fluxlinkage_c (Flux linkage, phase C, [Wb])');
    varslist=strvcat(varslist,'Fluxlinkage_d (Flux linkage, d-axis, [Wb])');
    varslist=strvcat(varslist,'Fluxlinkage_q (Flux linkage, q-axis, [Wb])');
elseif get(motoranalysishandles.togglebutton_dynamicDQ,'Value')               % dynamic D-Q
    if isempty(Simulation.DynamicDQ.time)
        errordlg('No simulation data to plot.','PlotWizard Error','modal');
        return;    
    end
    varslist=strvcat(varslist,'Ia (Stator phase current, phase A, [A])');
    varslist=strvcat(varslist,'Ib (Stator phase current, phase B, [A])');
    varslist=strvcat(varslist,'Ic (Stator phase current, phase C, [A])');
    varslist=strvcat(varslist,'Id (Phase current, d-axis [A])');
    varslist=strvcat(varslist,'Iq (Phase current, q-axis, [A])');
    varslist=strvcat(varslist,'Va (Phase voltage, phase A, [V])');
    varslist=strvcat(varslist,'Vb (Phase voltage, phase B, [V])');
    varslist=strvcat(varslist,'Vc (Phase voltage, phase C, [V])');
    varslist=strvcat(varslist,'Vd (Phase voltage, d-axis [V])');
    varslist=strvcat(varslist,'Vq (Phase voltage, q-axis, [V])');
    varslist=strvcat(varslist,'Gamma (Effective advance angle, [electrical degrees])');
    varslist=strvcat(varslist,'BackEMFa (Phase back EMF, phase A, [V])');
    varslist=strvcat(varslist,'BackEMFb (Phase back EMF, phase B, [V])');
    varslist=strvcat(varslist,'BackEMFc (Phase back EMF, phase C, [V])');
    varslist=strvcat(varslist,'BackEMFd (Phase back EMF, d-axis, [V])');
    varslist=strvcat(varslist,'BackEMFq (Phase back EMF, q-axis, [V])');    
    varslist=strvcat(varslist,'Torque (Electromagnetic torque (by flux linkage and current), [N*m])');
    varslist=strvcat(varslist,'Load (Load torque on the motor shaft, [N*m])');
    varslist=strvcat(varslist,'Speed (Rotor speed, [RPM])');
    varslist=strvcat(varslist,'Rotang (Rotor angular position, [rad])');
    varslist=strvcat(varslist,'Pinput (Input active electrical power, [W])');
    varslist=strvcat(varslist,'Preact (Reactive electrical power, [VAR])');
    varslist=strvcat(varslist,'Pmech (Mechanical power on the rotor shaft, [W])');
    varslist=strvcat(varslist,'Ps (Stator winding losses, [W])');
    varslist=strvcat(varslist,'Pmf (Time derivative of the magnetic field energy, [VAR])');
    varslist=strvcat(varslist,'Fluxlinkage_a (Flux linkage, phase A, [Wb])');
    varslist=strvcat(varslist,'Fluxlinkage_b (Flux linkage, phase B, [Wb])');
    varslist=strvcat(varslist,'Fluxlinkage_c (Flux linkage, phase C, [Wb])');
    varslist=strvcat(varslist,'Fluxlinkage_d (Flux linkage, d-axis, [Wb])');
    varslist=strvcat(varslist,'Fluxlinkage_q (Flux linkage, q-axis, [Wb])');
    varslist=strvcat(varslist,'Torque_magnet (Magnet torque (by flux linkage and current), [N*m])');
    varslist=strvcat(varslist,'Torque_reluctance (Reluctance torque (by flux linkage and current), [N*m])');
    varslist=strvcat(varslist,'Ld (D-axis inductance, [H])');
    varslist=strvcat(varslist,'Lq (Q-axis inductance, [H])');
    varslist=strvcat(varslist,'Ldq (Cross-saturation inductance, [H])');
    varslist=strvcat(varslist,'Fluxlinkage_md (D-axis magnet flux linkage, [Wb])');
    varslist=strvcat(varslist,'Fluxlinkage_mqd (Q-axis cross-saturation magnet flux linkage, [Wb])');
else
    return
end
cell_varslist=cell(size(varslist,1),1);
for i=1:size(varslist,1)
    cell_varslist{i,1}=strtrim(varslist(i,:));
end


% --- Executes on button press in pushbutton_tm_plot.
function pushbutton_tm_plot_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_tm_plot (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
motoranalysishandles = guidata(handles.motoranalysis);
if isempty(motoranalysishandles.File)
    errordlg('No simulation file opened.','PlotWizard Error','modal');
    return;
end
Simulation = motoranalysishandles.Simulation;
if get(motoranalysishandles.togglebutton_dynamicFEA,'Value')               % dynamic FEA
    Settings = Simulation.Settings.DynamicFEA;
    Outputs = Simulation.DynamicFEA;    
elseif get(motoranalysishandles.togglebutton_MS,'Value')                   % magnetostatic
    Settings = Simulation.Settings.Magnetostatic;
    Outputs = Simulation.Magnetostatic.Timesteppingdata;
elseif get(motoranalysishandles.togglebutton_dynamicDQ,'Value')            % dynamic D-Q
    Settings = Simulation.Settings.DynamicDQ;
    Outputs = Simulation.DynamicDQ;     
else
    return
end
if isempty(Outputs) || length(Outputs.time)<2
    errordlg('No simulation data to plot.','PlotWizard Error','modal');
    return;    
end
CurrentTime = Outputs.time(end);
Outputs_fields = fieldnames(Outputs);
for i=1:length(Outputs_fields)
    FieldName=Outputs_fields{i,1};
    if strcmp(FieldName,'Ia') && get(motoranalysishandles.togglebutton_dynamicFEA,'Value')
        Ia=Outputs.Ia;
        Npp_a=size(Ia,1);    % number of parallel paths of phase a
        if Npp_a>1
            for j=1:Npp_a
                temp=Ia(j,:);
                eval(['Ia' num2str(j) '=temp;']);
            end
        end
        Ia=sum(Ia,1);
    elseif strcmp(FieldName,'Ib') && get(motoranalysishandles.togglebutton_dynamicFEA,'Value')
        Ib=Outputs.Ib;
        Npp_b=size(Ib,1);    % number of parallel paths of phase b
        if Npp_b>1
            for j=1:Npp_b
                temp=Ib(j,:);
                eval(['Ib' num2str(j) '=temp;']);
            end
        end
        Ib=sum(Ib,1);
    elseif strcmp(FieldName,'Ic') && get(motoranalysishandles.togglebutton_dynamicFEA,'Value')
        Ic=Outputs.Ic;
        Npp_c=size(Ic,1);    % number of parallel paths of phase c
        if Npp_c>1
            for j=1:Npp_c
                temp=Ic(j,:);
                eval(['Ic' num2str(j) '=temp;']);
            end
        end
        Ic=sum(Ic,1);
    elseif strcmp(FieldName,'Speed')    
        Speed=Outputs.Speed*60/(2*pi);   % [rad/s] to [RPM]
    elseif strcmp(FieldName,'time') 
        time=Outputs.time;
        time=time-time(1);
    else
        temp=getfield(Outputs,FieldName);
        eval([Outputs_fields{i,1} '=temp;']);
    end
end
Geometry_fields = fieldnames(Simulation.Geometry);
for i=1:length(Geometry_fields)
    FieldName=Geometry_fields{i,1};
    temp=getfield(Simulation.Geometry,FieldName);
    if strcmp(FieldName,'Tas') || strcmp(FieldName,'Ns') || strcmp(FieldName,'rotorskew') || strcmp(FieldName,'statorskew') || ...
       strcmp(FieldName,'statorslottype') || strcmp(FieldName,'slotlayertype') || strcmp(FieldName,'statorslotcornertype') || ...
       strcmp(FieldName,'layerpos') || strcmp(FieldName,'motortype')
    % no action
    else
        temp=temp/1000;
    end
    eval([Geometry_fields{i,1} '=temp;']);
end
Mesh_fields = fieldnames(Simulation.Mesh);
for i=1:length(Mesh_fields)
    temp=getfield(Simulation.Mesh,Mesh_fields{i,1});
    eval([Mesh_fields{i,1} '=temp;']);
end
Windings_fields = fieldnames(Simulation.Windings);
for i=1:length(Windings_fields)
    temp=getfield(Simulation.Windings,Windings_fields{i,1});
    eval([Windings_fields{i,1} '=temp;']);
end
Settings_fields = fieldnames(Settings);
for i=1:length(Settings_fields)
    temp=getfield(Settings,Settings_fields{i,1});
    eval([Settings_fields{i,1} '=temp;']);
end
if get(motoranalysishandles.togglebutton_dynamicFEA,'Value')
    if ~isempty(Simulation.Userdata)
        Userdata_fields = fieldnames(Simulation.Userdata);
        for i=1:length(Userdata_fields)
            temp=getfield(Simulation.Userdata,Userdata_fields{i,1});
            if length(temp)==length(time)    % if variable is a time sequence array
                eval([Userdata_fields{i,1} '=temp;']);
            end
        end
    end
end
clear temp
nsubplots=handles.tm_nsubplots;
hsp=[];
hf=figure;
for i=1:length(nsubplots)
    ind=nsubplots(i);
    plotexp=get(getfield(handles,['edit_tm_plotexp' num2str(ind)]),'String');
    if ~isempty(plotexp)
        h=subplot(length(nsubplots),1,i);
        hsp=[hsp h];
        try
            eval(plotexp);
        catch err
            close(hf);
            msgText = getReport(err);
            pattern='Undefined function or variable';
            ind=strfind(msgText,pattern);
            if ind       % if 'Undefined function or variable...' error message
                strvar=msgText(ind+length(pattern):end-1);
                strvar=strvar(1:strfind(strvar,'.')-1);
                if get(motoranalysishandles.togglebutton_dynamicFEA,'Value')               % dynamicFEA
                    stranalysistype='Dynamic FE Analysis';
                elseif get(motoranalysishandles.togglebutton_MS,'Value')                   % magnetostatic analysis    
                    stranalysistype='Magnetostatic Analysis';
                elseif get(motoranalysishandles.togglebutton_dynamicDQ,'Value')            % dynamic D-Q analysis  
                    stranalysistype='Dynamic D-Q Analysis';
                else 
                    error('Something goes wrong!');
                end
                errordlg(['Incorrect plotting expression. Variable' strvar ' is not defined for ' stranalysistype '.'],'PlotWizard Error','modal');
            else
                errordlg('Incorrect plotting expression.','PlotWizard Error','modal');
            end
            return
        end
        grid;
        x_lim=get(getfield(handles,['edit_tm_xlim' num2str(ind)]),'String'); x_lim=str2num(x_lim);
        if ~isempty(x_lim)
            if length(x_lim)==1
                x_lim=[0 x_lim];
            end
            xlim(x_lim);
        else
            if findstr(plotexp,'time')
                xlim([0 time(end)]);
                xlabel('Time, s');
            end
        end
        y_lim=get(getfield(handles,['edit_tm_ylim' num2str(ind)]),'String'); y_lim=str2num(y_lim);
        if ~isempty(y_lim)
            if length(y_lim)==1
                y_lim=[0 y_lim];
            end
            ylim(y_lim);
        end
    end
end
if isempty(hsp)
    close(hf);
    return
end
if get(handles.checkbox_linkaxes,'Value')
    linkaxes(hsp,'x');
end

% --- Executes on button press in pushbutton_chgsource.
function pushbutton_chgsource_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_chgsource (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Allow the user to select the directory
SourceList = get(handles.pup_source,'String');
index = get(handles.pup_source,'Value');
if ~isempty(SourceList)
    start_path = SourceList{index,1};
else
    start_path = cd;
end
directory_name = uigetdir(start_path,'Select a Directory');
% If 'Cancel' was selected then return
if isequal(directory_name,0)
    return
else
    SetSourceFolder(handles,directory_name);
end


function SetSourceFolder(handles,SourceFolder)
SourceList = get(handles.pup_source,'String');
if isempty(SourceList)
    SourceList = cell(1,1);
    SourceList{1,1} = SourceFolder;
    set(handles.pup_source,'String',SourceList);
end
for i=1:length(SourceList)
    if strcmp(SourceFolder,SourceList(i))
        break;
    elseif i==length(SourceList)  % if thire is no SourceFolder in SourceList then add it
        SourceList_ = SourceList;
        SourceList = cell(length(SourceList)+1,1);
        for j=1:length(SourceList_)
            SourceList{j,1}=SourceList_{j,1};
        end
        i = i+1;
        SourceList{i,1} = SourceFolder;
        set(handles.pup_source,'String',SourceList);
        break;
    end
end
set(handles.pup_source,'Value',i);
set(handles.pup_source,'UserData',i);        % store item index in UserData


function editplotwizard_Callback(hObject, eventdata, handles)
% hObject    handle
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
UpdatePlotWizard(hObject,[]);


% --- Executes on button press in pushbutton_showplottedquantities.
function pushbutton_showplottedquantities_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_showplottedquantities (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
OuterPosition=get(handles.PlotWizard,'OuterPosition');
ButtonString=get(hObject,'String');
if strcmp(ButtonString,'Plotted quantities  >>')   % click to expand
    set(hObject,'String','Plotted quantities  <<');
    set(hObject,'TooltipString','Click to hide plotted quantities.');
    OuterPosition(3) = OuterPosition(3)*3/2;
    set(0,'Units',get(handles.PlotWizard,'Units'));
    scnsize = get(0,'ScreenSize');
    if OuterPosition(1)+OuterPosition(3)>scnsize(3)
        OuterPosition(1) = scnsize(3)-OuterPosition(3);
    end
    if OuterPosition(2)+OuterPosition(4)>scnsize(4)
        OuterPosition(2) = scnsize(4)-OuterPosition(4);
    end
else                                               % click to collapse
    set(hObject,'String','Plotted quantities  >>');
    set(hObject,'TooltipString','Click to show plotted quantities.');
    OuterPosition(3) = OuterPosition(3)*2/3;
end
set(handles.PlotWizard,'OuterPosition',OuterPosition);


% --- Executes on button press in pushbutton_dq_how.
function pushbutton_setupdefault_Callback(hObject, eventdata, handles)
% hObject    handle
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% Click to see how 'Max. RMS phase voltage' is computed.
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Drive=Simulation.Drive;
RatedData=Simulation.RatedData;
Windings=Simulation.Windings;
Tag = get(hObject,'Tag');
if strcmp(Tag,'pushbutton_em_defaultvoltage')
    Vdc=Drive.Vdc;
    if isempty(Vdc)
        errordlg('No DC supply voltage specified in Drive Settings window.','Default Voltage Setup','modal');
        return
    end
    if strcmp(Drive.DriveType,'Six-step')
        errordlg('Not suitable for six-step drive.','Default Voltage Setup','modal');
        return
    elseif strcmp(Drive.DriveType,'Current hysteresis PWM')
        if strcmp(Windings.statorcircuit,'StarConnection')
            V = Vdc/2/sqrt(2);
            button = questdlg({'Input data for voltage calculation:',...
                              ['  DC supply voltage: Vdc = ' num2str(Vdc)],...
                               '  PWM method: current hysteresis',...
                               '  Stator winding connection: star',...
                               '',...
                               ['Max. RMS phase voltage to setup: V = Vdc/2/sqrt(2) = ' num2str(V)]},...
                               'Default Voltage Setup','OK','Cancel','OK');
        elseif strcmp(Windings.statorcircuit,'DeltaConnection')    
            V = Vdc/2/sqrt(2)*sqrt(3);
            button = questdlg({'Input data for voltage calculation:',...
                              ['  DC supply voltage: Vdc = ' num2str(Vdc)],...
                               '  PWM method: current hysteresis',...
                               '  Stator winding connection: delta',...
                               '',...
                               ['Max. RMS phase voltage to setup: V = Vdc/2/sqrt(2)*sqrt(3) = ' num2str(V)]},...
                               'Default Voltage Setup','OK','Cancel','OK');
        end
    elseif strcmp(Drive.DriveType,'Space vector PWM')
        if strcmp(Windings.statorcircuit,'StarConnection')
            V = Vdc/sqrt(3)/sqrt(2);
            button = questdlg({'Input data for voltage calculation:',...
                              ['  DC supply voltage: Vdc = ' num2str(Vdc)],...
                               '  PWM method: space vector',...
                               '  Stator winding connection: star',...
                               '',...
                               ['Max. RMS phase voltage to setup: V = Vdc/sqrt(3)/sqrt(2) = ' num2str(V)]},...
                               'Default Voltage Setup','OK','Cancel','OK');
        elseif strcmp(Windings.statorcircuit,'DeltaConnection')    
            V = Vdc/sqrt(3)/sqrt(2)*sqrt(3);
            button = questdlg({'Input data for voltage calculation:',...
                              ['  DC supply voltage: Vdc = ' num2str(Vdc)],...
                               '  PWM method: space vector',...
                               '  Stator winding connection: delta',...
                               '',...
                               ['Max. RMS phase voltage to setup: V = Vdc/sqrt(3)/sqrt(2)*sqrt(3) = ' num2str(V)]},...
                               'Default Voltage Setup','OK','Cancel','OK');
        end
    end
    if strcmp(button,'OK')
         set(handles.edit_em_Vphasemax,'String',num2str(V,6));
    end
elseif strcmp(Tag,'pushbutton_em_defaultcurrent')
    RatedCurrent=RatedData.RatedCurrent;   % rated supply current
    if isempty(RatedCurrent)
        errordlg('No rated supply current specified in Rated Data window.','Default Current Setup','modal');
        return
    end
    if strcmp(Windings.statorcircuit,'StarConnection')
        I=RatedCurrent;
        button = questdlg(['Maximum RMS phase current will be changed to ' num2str(I)],...
                           'Default Current Setup','OK','Cancel','OK');    
    elseif strcmp(Windings.statorcircuit,'DeltaConnection')    
        I=RatedCurrent/sqrt(3);
        button = questdlg(['Maximum RMS phase current will be changed to ' num2str(RatedCurrent) '/sqrt(3) = ' num2str(I)],...
                           'Default Current Setup','OK','Cancel','OK');       
    end
    if strcmp(button,'OK')
        set(handles.edit_em_Iphasemax,'String',num2str(I,6));
    end
elseif strcmp(Tag,'pushbutton_em_defaultpower')
    RatedPower=RatedData.RatedPower;
    if isempty(RatedPower)
        errordlg('No rated power specified in Rated Data window.','Default Power Setup','modal');
        return
    end
    button = questdlg(['Maximum input power will be changed to ' num2str(RatedPower)],...
                       'Default Power Setup','OK','Cancel','OK');   
    if strcmp(button,'OK')
        set(handles.edit_em_Pinputmax,'String',num2str(RatedPower,10));
    end
elseif strcmp(Tag,'pushbutton_em_defaultspeed')
    RatedSpeed=RatedData.RatedSpeed;
    if isempty(RatedSpeed)
        errordlg('No rated speed specified in Rated Data window.','Default Speed Setup','modal');
        return
    end
    button = questdlg(['Maximum speed will be changed to ' num2str(RatedSpeed)],...
                       'Default Speed Setup','OK','Cancel','OK');   
    if strcmp(button,'OK')
        set(handles.edit_em_speedmax,'String',num2str(RatedSpeed,10));
    end
end


function SetDQPhaseVoltage(hObject)
handles = guidata(hObject);
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Drive=Simulation.Drive;
Windings=Simulation.Windings;
Vdc=Drive.Vdc;
if isempty(Vdc)
    set(handles.edit_dq_Vsrms_max,'String','N/A');
    return
end
if strcmp(Drive.DriveType,'Six-step')
    set(handles.edit_dq_Vsrms_max,'String','N/A');
    return
elseif strcmp(Drive.DriveType,'Current hysteresis PWM')
    if strcmp(Windings.statorcircuit,'StarConnection')
        V = Vdc/2/sqrt(2);
    elseif strcmp(Windings.statorcircuit,'DeltaConnection')
        V = Vdc/2/sqrt(2)*sqrt(3);
    end
elseif strcmp(Drive.DriveType,'Space vector PWM')
    if strcmp(Windings.statorcircuit,'StarConnection')
        V = Vdc/sqrt(3)/sqrt(2);
    elseif strcmp(Windings.statorcircuit,'DeltaConnection')
        V = Vdc/sqrt(3)/sqrt(2)*sqrt(3);
    end
end
set(handles.edit_dq_Vsrms_max,'String',num2str(V,6));
    
    
% --- Executes on button press in pushbutton_dq_how.
function pushbutton_dq_how_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_dq_how (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% Click to see how 'Max. RMS phase voltage' is computed.
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Drive=Simulation.Drive;
Vdc=Drive.Vdc;
if isempty(Vdc)
    errordlg('No DC supply voltage specified in Drive Settings window.','PlotWizard Error','modal');
    return
end
if strcmp(Drive.DriveType,'Six-step')
    errordlg('Six-step drive is not suitable for this type of analysis.','PlotWizard Error','modal');
    return
end
msg={'Max. RMS phase voltage is computed as follows:';
     ' ';
     'For star connected stator winding and current hysteresis PWM method:';
     'Vmax = Vdc/2/sqrt(2)';
     ' ';
     'For delta connected stator winding and current hysteresis PWM method:';
     'Vmax = Vdc/2/sqrt(2)*sqrt(3)';
     ' ';
     'For star connected stator winding and space vector PWM method:';
     'Vmax = Vdc/sqrt(3)/sqrt(2)';
     ' ';
     'For delta connected stator winding and space vector PWM method:';
     'Vmax = Vdc/sqrt(3)/sqrt(2)*sqrt(3)'};
msgbox(msg,'PlotWizard Message','modal');


% --- Executes on button press in pushbutton_DQspeedaccuracy.
function pushbutton_DQspeedaccuracy_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_DQspeedaccuracy (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
motoranalysishandles = guidata(handles.motoranalysis);
DriveSettings=motoranalysishandles.DriveSettings;
SA=handles.DQPWMSpeedAccuracy;
SA=dqpwmspeedaccuracy('SA',SA,'DriveSettings',DriveSettings);
if ~isempty(SA)
    handles.DQPWMSpeedAccuracy=SA;
    guidata(hObject,handles);
    UpdatePlotWizard(handles.PlotWizard,[]);
end

% --- Executes on button press in pushbutton_DQplot.
function pushbutton_DQplot_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_DQplot (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles = guidata(hObject);
if strcmp(get(handles.pushbutton_DQplot,'String'),'Plot')
    handles.StopPlotting=0;
    guidata(hObject,handles);
    motoranalysishandles = guidata(handles.motoranalysis);
    if isempty(motoranalysishandles.File)
        errordlg('No simulation file opened.','PlotWizard Error','modal');
        return;
    end
    Simulation = motoranalysishandles.Simulation;
    set(handles.PlotWizard,'Pointer','watch');
    index = get(handles.pup_dq_xaxisquantity,'Value');
    strlist = get(handles.pup_dq_xaxisquantity,'String');
    xaxisquantity = strlist{index,1};
    str_SpeedValues = get(handles.edit_dq_speedvalues,'String');
    str_CurrentValues = get(handles.edit_dq_currentvalues,'String');
    str_GammaValues = get(handles.edit_dq_gammavalues,'String');
    index = get(handles.pup_dq_fieldweakeningcontrol,'Value');
    strlist = get(handles.pup_dq_fieldweakeningcontrol,'String');
    fieldweakeningcontrol = strlist{index,1};
    fieldweakeningalg = MotorAnalysisSettings('fieldweakeningalg');
    Drive=Simulation.Drive;
    DQPWMSpeedAccuracy=handles.DQPWMSpeedAccuracy;
    str_Vsrms_max = '';
    if get(handles.pup_dq_voltageselection,'Value')~=1          % voltageselection: 'Based on Vdc and PWM method' or 'Specified by user'
        str_Vsrms_max = get(handles.edit_dq_Vsrms_max,'String');
        if isempty(str_Vsrms_max)
            errordlg('Max. RMS phase voltage is not specified.','PlotWizard Error','modal');
            set(handles.PlotWizard,'Pointer','arrow');
            return
        end
    end
    multipleyaxes = get(handles.checkbox_dq_multipleyaxes,'Value');
    index = get(handles.pup_dq_modeltype,'Value');
    strlist = get(handles.pup_dq_modeltype,'String');
    modeltype = strlist{index,1};
    index = get(handles.pup_dq_interpmethod,'Value');
    strlist = get(handles.pup_dq_interpmethod,'String');
    interpmethod = strlist{index,1};
    plotlist = {};
    if get(handles.checkbox_Is,'Value'), plotlist = celladd(plotlist,'Is'); end
    if get(handles.checkbox_Vs,'Value'), plotlist = celladd(plotlist,'Vs'); end
    if get(handles.checkbox_Id,'Value'), plotlist = celladd(plotlist,'Id'); end
    if get(handles.checkbox_Iq,'Value'), plotlist = celladd(plotlist,'Iq'); end
    if get(handles.checkbox_Vd,'Value'), plotlist = celladd(plotlist,'Vd'); end
    if get(handles.checkbox_Vq,'Value'), plotlist = celladd(plotlist,'Vq'); end
    if get(handles.checkbox_Gamma,'Value'), plotlist = celladd(plotlist,'Gamma'); end
    if get(handles.checkbox_Torque,'Value'), plotlist = celladd(plotlist,'Torque'); end
    if get(handles.checkbox_MagnetTorque,'Value'), plotlist = celladd(plotlist,'MagnetTorque'); end
    if get(handles.checkbox_ReluctanceTorque,'Value'), plotlist = celladd(plotlist,'ReluctanceTorque'); end
    if get(handles.checkbox_Pinput,'Value'), plotlist = celladd(plotlist,'Pinput'); end
    if get(handles.checkbox_Pmech,'Value'), plotlist = celladd(plotlist,'Pmech'); end
    if get(handles.checkbox_Preact,'Value'), plotlist = celladd(plotlist,'Preact'); end
    if get(handles.checkbox_Efficiency,'Value'), plotlist = celladd(plotlist,'Efficiency'); end
    if get(handles.checkbox_PowerFactor,'Value'), plotlist = celladd(plotlist,'PowerFactor'); end
    if get(handles.checkbox_Ps,'Value'), plotlist = celladd(plotlist,'Ps'); end
    if get(handles.checkbox_backEMF,'Value'), plotlist = celladd(plotlist,'backEMF'); end
    if get(handles.checkbox_Ld,'Value'), plotlist = celladd(plotlist,'Ld'); end
    if get(handles.checkbox_Lq,'Value'), plotlist = celladd(plotlist,'Lq'); end
    if get(handles.checkbox_Ldq,'Value'), plotlist = celladd(plotlist,'Ldq'); end
    if get(handles.checkbox_fluxlinkage_md,'Value'), plotlist = celladd(plotlist,'fluxlinkage_md'); end
    if get(handles.checkbox_fluxlinkage_mqd,'Value'), plotlist = celladd(plotlist,'fluxlinkage_mqd'); end
    set(handles.pushbutton_DQplot,'String','Stop plotting');
    set(handles.pushbutton_DQplot,'TooltipString','Click to stop plotting.');
    set(handles.pushbutton_createmap,'Enable','off');
    set(handles.pushbutton_plotmap,'Enable','off');
    set(handles.pushbutton_mapopts,'Enable','off');
    DQplot(Simulation,plotlist,str_SpeedValues,str_CurrentValues,str_GammaValues,xaxisquantity,str_Vsrms_max,modeltype,Drive,DQPWMSpeedAccuracy,...
           interpmethod,multipleyaxes,fieldweakeningcontrol,fieldweakeningalg,handles);
    set(handles.pushbutton_DQplot,'String','Plot');
    set(handles.pushbutton_DQplot,'TooltipString','Click to start plotting.');
    set(handles.pushbutton_createmap,'Enable','on');
    if ~isempty(Simulation.EfficiencyMap)
        set(handles.pushbutton_plotmap,'Enable','on');
        set(handles.pushbutton_mapopts,'Enable','on');
    end
    set(handles.PlotWizard,'Pointer','arrow');
elseif strcmp(get(handles.pushbutton_DQplot,'String'),'Stop plotting')
    button = questdlg('Cancel plotting?',...
        'PlotWizard','Yes','No','No');
    if strcmp(button,'No')
        return;
    end
    handles.StopPlotting=1;
    guidata(hObject,handles);
end


% --- Executes on button press in pushbutton_createmap.
function pushbutton_createmap_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_createmap (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles = guidata(hObject);
if strcmp(get(handles.pushbutton_createmap,'String'),'Create Efficiency Map')
    [Pinputmax, status]= str2num(get(handles.edit_em_Pinputmax,'String'));
    Pinputmax=checkPinputmax(Pinputmax,status);
    if isnan(Pinputmax)
        return
    end
    Kmechloss=get(handles.edit_em_Kmechloss,'String');
    Kmechloss=checkKmechloss(Kmechloss);
    if isnan(Kmechloss)
        return
    end
    handles.StopPlotting=0;
    guidata(hObject,handles);
    motoranalysishandles = guidata(handles.motoranalysis);
    if isempty(motoranalysishandles.File)
        errordlg('No simulation file opened.','PlotWizard Error','modal');
        return;
    end
    Simulation = motoranalysishandles.Simulation;
    str_GammaValues = get(handles.edit_em_gammavalues,'String');
    str_Vphasemax = get(handles.edit_em_Vphasemax,'String');
    str_Iphasemax = get(handles.edit_em_Iphasemax,'String');
    str_speedmax = get(handles.edit_em_speedmax,'String');
    str_torquestep = get(handles.edit_em_torquestep,'String');
    str_speedstep = get(handles.edit_em_speedstep,'String');
    index = get(handles.pup_em_modeltype,'Value');
    strlist = get(handles.pup_em_modeltype,'String');
    modeltype = strlist{index,1};
    index = get(handles.pup_em_interpmethod,'Value');
    strlist = get(handles.pup_em_interpmethod,'String');
    interpmethod = strlist{index,1};
    if strcmp(modeltype,'FEA based')
        msg='You are about to compute the efficiency map using direct FEA solutions. This operation can take a very long time to complete. It is usually faster to build D-Q model and use it to compute the efficiency map.';
        button = questdlg(msg,'PlotWizard','Continue with FEA','Cancel','Cancel');
        if strcmp(button,'Cancel')
            return;
        end
    end
    set(handles.PlotWizard,'Pointer','watch');
    set(motoranalysishandles.motoranalysis,'Pointer','watch');
    set(handles.pushbutton_createmap,'String','Stop');
    set(handles.pushbutton_createmap,'TooltipString','Click to stop efficiency map computation.');
    set(handles.pushbutton_DQplot,'Enable','off');
    set(handles.pushbutton_plotmap,'Enable','off');
    set(handles.pushbutton_mapopts,'Enable','off');
    [Ismax,Vmax,speedmax,torquestep,speedstep,Speed,Torque,BorderTorque,BorderInputPower,Struct_plot,Struct_tbl,mode]=...
    GetEfficiencyMap(Simulation,str_GammaValues,str_Vphasemax,str_Iphasemax,str_speedmax,str_torquestep,str_speedstep,modeltype,interpmethod,handles);
    set(handles.text_mapplotstatus,'String','Efficiency map: computation completed');drawnow
    if ~isempty(Speed)
        EfficiencyMap.Speed=Speed;
        EfficiencyMap.Torque=Torque;
        EfficiencyMap.BorderTorque=BorderTorque;
        EfficiencyMap.BorderInputPower=BorderInputPower;
        EfficiencyMap.Struct_plot=Struct_plot;
        EfficiencyMap.Struct_tbl=Struct_tbl;
        EfficiencyMap.strGamma=str_GammaValues;
        EfficiencyMap.Ismax=Ismax;
        EfficiencyMap.Vmax=Vmax;
        EfficiencyMap.speedmax=speedmax;
        EfficiencyMap.torquestep=torquestep;
        EfficiencyMap.speedstep=speedstep;
        EfficiencyMap.interpmethod=interpmethod;
        EfficiencyMap.mode=mode;
        if ~isempty(Struct_plot)
            if ~isempty(Simulation.EfficiencyMap)
                button = questdlg('Efficiency map has been previously computed. Do you want to replace existing efficiency map with the new one?',...
                    'Plot Wizard: D-Q Analysis','Yes','No','No');
            else
                button='Yes';
            end
            if strcmp(button,'Yes')
                Simulation.EfficiencyMap=EfficiencyMap;
                motoranalysishandles.Simulation=Simulation;
                guidata(handles.motoranalysis,motoranalysishandles);
                motoranalysishandles.Save_Callback(motoranalysishandles.menuSave,[],motoranalysishandles);
                guidata(hObject, handles);
            end
        end
        set(handles.text_mapplotstatus,'String','Efficiency map: plotting...');drawnow
        set(handles.text_mapplotstatus,'Visible','on');drawnow
        PlotEfficiencyMap(EfficiencyMap,Pinputmax,Kmechloss,mode);
    end
    set(handles.text_mapplotstatus,'Visible','off');drawnow
    set(handles.pushbutton_createmap,'String','Create Efficiency Map');
    set(handles.pushbutton_createmap,'TooltipString','Click to compute efficiency map.');
    set(handles.pushbutton_DQplot,'Enable','on');
    if ~isempty(Simulation.EfficiencyMap)
        set(handles.pushbutton_plotmap,'Enable','on');
        set(handles.pushbutton_mapopts,'Enable','on');
    end
    set(handles.PlotWizard,'Pointer','arrow');
    set(motoranalysishandles.motoranalysis,'Pointer','arrow');
elseif strcmp(get(handles.pushbutton_createmap,'String'),'Stop')
    button = questdlg('Stop efficiency map computation?',...
        'PlotWizard','Yes','No','No');
    if strcmp(button,'No')
        return;
    end
    handles.StopPlotting=1;
    guidata(hObject,handles);
end
UpdatePlotWizard(hObject,[]);


% --- Executes on button press in pushbutton_plotmap.
function pushbutton_plotmap_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_plotmap (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles = guidata(hObject);
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
EfficiencyMap = Simulation.EfficiencyMap;
if isempty(EfficiencyMap)
    warndlg('No efficiency map data found','PlotWizard','modal');
    return
end
[Pinputmax, status]= str2num(get(handles.edit_em_Pinputmax,'String'));
Pinputmax=checkPinputmax(Pinputmax,status);
if isnan(Pinputmax)
    return
end
Kmechloss=get(handles.edit_em_Kmechloss,'String');
Kmechloss=checkKmechloss(Kmechloss);
if isnan(Kmechloss)
    return
end
set(motoranalysishandles.motoranalysis,'Pointer','watch');
set(handles.PlotWizard,'Pointer','watch');
mode=EfficiencyMap.mode;
set(handles.text_mapplotstatus,'String','Efficiency map: plotting...');drawnow
set(handles.text_mapplotstatus,'Visible','on');
set(handles.pushbutton_createmap,'Enable','off');
set(handles.pushbutton_DQplot,'Enable','off');
set(handles.pushbutton_plotmap,'Enable','off');
set(handles.pushbutton_mapopts,'Enable','off');drawnow
PlotEfficiencyMap(EfficiencyMap,Pinputmax,Kmechloss,mode);
set(handles.pushbutton_createmap,'Enable','on');
set(handles.pushbutton_DQplot,'Enable','on');
set(handles.pushbutton_plotmap,'Enable','on');
set(handles.pushbutton_mapopts,'Enable','on');
set(handles.text_mapplotstatus,'Visible','off');drawnow
set(motoranalysishandles.motoranalysis,'Pointer','arrow');
set(handles.PlotWizard,'Pointer','arrow');


% --- Executes on selection change in pushbutton_mapopts.
function pushbutton_mapopts_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_mapopts (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles = guidata(hObject);
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
EfficiencyMap = Simulation.EfficiencyMap;
if isempty(EfficiencyMap)
    warndlg('No efficiency map data found.','PlotWizard','modal');
    return
end
[Pinputmax, status]= str2num(get(handles.edit_em_Pinputmax,'String'));
Pinputmax=checkPinputmax(Pinputmax,status);
if isnan(Pinputmax)
    return
end
Kmechloss=get(handles.edit_em_Kmechloss,'String');
Kmechloss=checkKmechloss(Kmechloss);
if isnan(Kmechloss)
    return
end
mode=EfficiencyMap.mode;
index=get(hObject,'Value');
DispEfficiencyMap(EfficiencyMap,Pinputmax,Kmechloss,mode,index);


function Pinputmax=checkPinputmax(Pinputmax,status)
if isempty(Pinputmax)
    Pinputmax=inf;
    return
end
if ~status || length(Pinputmax)>1 || ~isreal(Pinputmax) || Pinputmax<=0
    if Pinputmax<=0
        errordlg('Maximum input power must be greater than zero.','PlotWizard','modal');
    else
        errordlg('Maximum input power is not correct.','PlotWizard','modal');
    end
    Pinputmax=NaN;
end

function Kmechloss=checkKmechloss(Kmechloss)
if ~isempty(Kmechloss)
    try
        Kmechloss=eval(['[' Kmechloss ']']);
    catch
        Kmechloss=NaN;
        errordlg('Mechanical loss coefficients are not correct.','PlotWizard Error','modal');
        return
    end
    if ~isreal(Kmechloss)
        Kmechloss=NaN;
        errordlg('Mechanical loss coefficients are not correct.','PlotWizard Error','modal');
        return
    end
else
    Kmechloss=0;
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% CreateFcn block        
        
% --- Executes during object creation, after setting all properties.
function edit_ag_time1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_time1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_ag_xlim1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_xlim1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_ag_vars1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_vars1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function pup_ag_slice1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_ag_slice1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function pup_ag_plottype1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_ag_plottype1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_ag_ylim1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_ylim1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_ag_time2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_time2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_ag_xlim2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_xlim2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_ag_vars2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_vars2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_ag_plottype2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_ag_plottype2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_ag_slice2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_ag_slice2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



% --- Executes during object creation, after setting all properties.
function edit_ag_ylim2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_ylim2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_ag_time3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_time3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_ag_xlim3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_xlim3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_ag_vars3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_vars3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_ag_slice3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_ag_slice3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_ag_plottype3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_ag_plottype3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_ag_ylim3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_ylim3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_ag_time4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_time4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_ag_xlim4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_xlim4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_ag_slice4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_ag_slice4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_ag_plottype4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_ag_plottype4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_ag_ylim4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_ylim4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_ag_vars4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_vars4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_ag_time5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_time5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_ag_xlim5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_xlim5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_ag_vars5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_vars5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function text_ag_subplot5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to text_ag_subplot5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_ag_slice5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_ag_slice5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_ag_plottype5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_ag_plottype5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_ag_ylim5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ag_ylim5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function pup_interpmethod_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_interpmethod (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function pup_cs_quantity1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_cs_quantity1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_time1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_time1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function pup_cs_slice1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_cs_slice1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_cs_slice2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_cs_slice2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_cs_quantity2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_cs_quantity2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_time2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_time2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_cs_quantity3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_cs_quantity3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_time3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_time3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_cs_slice3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_cs_slice3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_cs_quantity4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_cs_quantity4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_time4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_time4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_cs_slice4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_cs_slice4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_cs_quantity5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_cs_quantity5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_time5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_time5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_cs_slice5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_cs_slice5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_xlim1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_xlim1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_ylim1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_ylim1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_xlim2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_xlim2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_ylim2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_ylim2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_xlim3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_xlim3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_ylim3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_ylim3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_xlim4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_xlim4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_ylim4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_ylim4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_xlim5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_xlim5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_ylim5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_ylim5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_cs_opts1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_cs_opts1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_cs_opts2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_cs_opts2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_cs_opts3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_cs_opts3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_cs_opts4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_cs_opts4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_cs_opts5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_cs_opts5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_nfluxlevels_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_nfluxlevels (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_an_time_start_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_an_time_start (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_an_time_stop_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_an_time_stop (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_skip_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_skip (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_disptime_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_disptime (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_tm_xlim1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_tm_xlim1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_tm_xlim2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_tm_xlim2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_tm_ylim1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_tm_ylim1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_tm_ylim2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_tm_ylim2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_tm_xlim3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_tm_xlim3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_tm_ylim3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_tm_ylim3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_tm_xlim4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_tm_xlim4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_tm_ylim4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_tm_ylim4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_tm_xlim5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_tm_xlim5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_tm_ylim5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_tm_ylim5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_tm_plotexp1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_tm_plotexp1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_tm_plotexp2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_tm_plotexp2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_tm_plotexp3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_tm_plotexp3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_tm_plotexp4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_tm_plotexp4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_tm_plotexp5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_tm_plotexp5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_zlim1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_zlim1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_zlim2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_zlim2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_zlim3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_zlim3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_zlim4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_zlim4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_cs_zlim5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_cs_zlim5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_source_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_source (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_dq_xaxisquantity_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_dq_xaxisquantity (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_dq_speedvalues_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_dq_speedvalues (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_dq_currentvalues_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_dq_currentvalues (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_dq_gammavalues_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_dq_gammavalues (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_dq_Vsrms_max_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_dq_Vsrms_max (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_dq_modeltype_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_dq_modeltype (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_dq_interpmethod_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_dq_interpmethod (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pushbutton_mapopts_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pushbutton_mapopts (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_em_Vphasemax_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_em_Vphasemax (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_em_Iphasemax_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_em_Iphasemax (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_em_speedmax_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_em_speedmax (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_em_Pinputmax_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_em_Pinputmax (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_em_Kmechloss_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_em_Kmechloss (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_em_gammavalues_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_em_gammavalues (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_em_modeltype_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_em_modeltype (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_em_interpmethod_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_em_interpmethod (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_em_torquestep_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_em_torquestep (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_em_speedstep_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_em_speedstep (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_dq_fieldweakeningcontrol_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_dq_fieldweakeningcontrol (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_dq_voltageselection_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_dq_voltageselection (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

"""

def plotwizard(*args, **kwargs):
    """Placeholder for translated MATLAB function."""
    raise NotImplementedError(
        "This function requires manual translation from MATLAB."
    )
