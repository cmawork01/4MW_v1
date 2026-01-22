# Auto-generated from drivesettings.m
# NOTE: This is a placeholder stub. Manual translation required.

from __future__ import annotations

"""
Original MATLAB source:

function varargout = drivesettings(varargin)
% DRIVESETTINGS MATLAB code for drivesettings.fig
%      DRIVESETTINGS, by itself, creates a new DRIVESETTINGS or raises the existing
%      singleton*.
%
%      H = DRIVESETTINGS returns the handle to a new DRIVESETTINGS or the handle to
%      the existing singleton*.
%
%      DRIVESETTINGS('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in DRIVESETTINGS.M with the given input arguments.
%
%      DRIVESETTINGS('Property','Value',...) creates a new DRIVESETTINGS or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before drivesettings_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to drivesettings_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help drivesettings

% Last Modified by GUIDE v2.5 02-Aug-2017 17:40:06

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @drivesettings_OpeningFcn, ...
                   'gui_OutputFcn',  @drivesettings_OutputFcn, ...
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


% --- Executes just before drivesettings is made visible.
function drivesettings_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to drivesettings (see VARARGIN)

% Choose default command line output for drivesettings
handles.output = hObject;

motoranalysisInput = find(strcmp(varargin, 'motoranalysis'));
if ~isempty(motoranalysisInput)
   handles.motoranalysis = varargin{motoranalysisInput+1};
end
% publish function UpdateDriveSettings
handles.UpdateDriveSettings = @UpdateDriveSettings;

% Tooltips
tooltip1='Specifies the time in electrical degrees when the switch is turned on. \n120 degrees  two switches are turned on at the same time;';
tooltip2='\n180 degrees  three switches are turned on at the same time.';
Tooltip=sprintf([tooltip1 tooltip2]);
set(handles.text_SwitchDutyCycle_sixstep,'TooltipString',Tooltip);
set(handles.pup_SwitchDutyCycle_sixstep,'TooltipString',Tooltip);

tooltip1='Allows to shift forward the commutation timing to compensate';
tooltip2='\na phase lag of the current with respect to the voltage.';
Tooltip=sprintf([tooltip1 tooltip2]);
set(handles.text_CommutationAdvanceAngle_sixstep,'TooltipString',Tooltip);
set(handles.edit_CommutationAdvanceAngle_sixstep,'TooltipString',Tooltip);

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes drivesettings wait for user response (see UIRESUME)
% uiwait(handles.DriveSettings);


% --- Outputs from this function are returned to the command line.
function varargout = drivesettings_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes when user attempts to close DriveSettings.
function DriveSettings_CloseRequestFcn(hObject, eventdata, handles)
% Don't close this figure. It must be deleted from motoranalysis
% Make it invisible then user tries to close it
set(hObject,'Visible','off');
motoranalysishandles = guidata(handles.motoranalysis);
set(motoranalysishandles.menuDriveSettings,'Checked','off');


function UpdateDriveSettings(hObject)
handles = guidata(hObject);
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Drive = Simulation.Drive;
DriveFields = fieldnames(Drive);
for i=1:length(DriveFields)
    DriveField = DriveFields{i};
    editbox = ['edit_' DriveField];
    if isfield(handles,editbox)           % if editbox
        DriveFieldValue = getfield(Drive,DriveField);
        set(getfield(handles,editbox),'String',num2str(DriveFieldValue,10));
    end
    popup = ['pup_' DriveField];
    if isfield(handles,popup)           % if popup menu
        DriveFieldValue = getfield(Drive,DriveField);
        strlist = get(getfield(handles,popup),'String');
        for n=1:length(strlist)
            if strcmp(DriveFieldValue,strlist(n))
                break;
            elseif n==length(strlist)
                error(['Inappropriate value for <' DriveField '>: something goes wrong']);
                return;
            end
        end
        set(getfield(handles,popup),'Value',n);
        set(getfield(handles,popup),'UserData',n);        % store item index in UserData
    end
end
if strcmp(Drive.DriveType,'Current hysteresis PWM')
    set(handles.edit_Is_hyst_perc,'Visible','on');
    set(handles.text_Is_hyst_perc,'Visible','on');
    set(handles.text_Is_hyst_perc_units,'Visible','on');
    set(handles.edit_fspwm,'Visible','off');
    set(handles.text_fspwm,'Visible','off');
    set(handles.text_fspwm_units,'Visible','off');
    set(handles.pup_SwitchDutyCycle_sixstep,'Visible','off');
    set(handles.text_SwitchDutyCycle_sixstep,'Visible','off');
    set(handles.text_SwitchDutyCycle_sixstep_units,'Visible','off');    
    set(handles.edit_CommutationAdvanceAngle_sixstep,'Visible','off');
    set(handles.text_CommutationAdvanceAngle_sixstep,'Visible','off');
    set(handles.text_CommutationAdvanceAngle_sixstep_units,'Visible','off');  
    set(handles.pup_SixStepOptions,'Visible','off');
    set(handles.text_SixStepOptions,'Visible','off');    
    set(handles.edit_Vdc_perc_sixstep,'Visible','off');
    set(handles.text_Vdc_perc_sixstep,'Visible','off');
    set(handles.text_Vdc_perc_sixstep_units,'Visible','off');
    set(handles.edit_Is_max_sixstep,'Visible','off');
    set(handles.text_Is_max_sixstep,'Visible','off');
    set(handles.text_Is_max_sixstep_units,'Visible','off');
    set(handles.edit_Is_hyst_perc_sixstep,'Visible','off');
    set(handles.text_Is_hyst_perc_sixstep,'Visible','off');
    set(handles.text_Is_hyst_perc_sixstep_units,'Visible','off');    
elseif strcmp(Drive.DriveType,'Space vector PWM')
    set(handles.edit_Is_hyst_perc,'Visible','off');
    set(handles.text_Is_hyst_perc,'Visible','off');
    set(handles.text_Is_hyst_perc_units,'Visible','off');
    set(handles.edit_fspwm,'Visible','on');
    set(handles.text_fspwm,'Visible','on');
    set(handles.text_fspwm_units,'Visible','on');
    set(handles.pup_SwitchDutyCycle_sixstep,'Visible','off');
    set(handles.text_SwitchDutyCycle_sixstep,'Visible','off');
    set(handles.text_SwitchDutyCycle_sixstep_units,'Visible','off');    
    set(handles.edit_CommutationAdvanceAngle_sixstep,'Visible','off');
    set(handles.text_CommutationAdvanceAngle_sixstep,'Visible','off');
    set(handles.text_CommutationAdvanceAngle_sixstep_units,'Visible','off');  
    set(handles.pup_SixStepOptions,'Visible','off');
    set(handles.text_SixStepOptions,'Visible','off');    
    set(handles.edit_Vdc_perc_sixstep,'Visible','off');
    set(handles.text_Vdc_perc_sixstep,'Visible','off');
    set(handles.text_Vdc_perc_sixstep_units,'Visible','off');
    set(handles.edit_Is_max_sixstep,'Visible','off');
    set(handles.text_Is_max_sixstep,'Visible','off');
    set(handles.text_Is_max_sixstep_units,'Visible','off');
    set(handles.edit_Is_hyst_perc_sixstep,'Visible','off');
    set(handles.text_Is_hyst_perc_sixstep,'Visible','off');
    set(handles.text_Is_hyst_perc_sixstep_units,'Visible','off');    
elseif strcmp(Drive.DriveType,'Six-step')
    set(handles.edit_Is_hyst_perc,'Visible','off');
    set(handles.text_Is_hyst_perc,'Visible','off');
    set(handles.text_Is_hyst_perc_units,'Visible','off');
    set(handles.edit_fspwm,'Visible','off');
    set(handles.text_fspwm,'Visible','off');
    set(handles.text_fspwm_units,'Visible','off');
    set(handles.pup_SwitchDutyCycle_sixstep,'Visible','on');
    set(handles.text_SwitchDutyCycle_sixstep,'Visible','on');
    set(handles.text_SwitchDutyCycle_sixstep_units,'Visible','on');    
    set(handles.edit_CommutationAdvanceAngle_sixstep,'Visible','on');
    set(handles.text_CommutationAdvanceAngle_sixstep,'Visible','on');
    set(handles.text_CommutationAdvanceAngle_sixstep_units,'Visible','on');  
    set(handles.pup_SixStepOptions,'Visible','on');
    set(handles.text_SixStepOptions,'Visible','on');   
    if strcmp(Drive.SixStepOptions,'General')
        set(handles.edit_Vdc_perc_sixstep,'Visible','off');
        set(handles.text_Vdc_perc_sixstep,'Visible','off');
        set(handles.text_Vdc_perc_sixstep_units,'Visible','off');
        set(handles.edit_Is_max_sixstep,'Visible','off');
        set(handles.text_Is_max_sixstep,'Visible','off');
        set(handles.text_Is_max_sixstep_units,'Visible','off');
        set(handles.edit_Is_hyst_perc_sixstep,'Visible','off');
        set(handles.text_Is_hyst_perc_sixstep,'Visible','off');
        set(handles.text_Is_hyst_perc_sixstep_units,'Visible','off');    
    elseif strcmp(Drive.SixStepOptions,'Six-step with limited maximum current')
        set(handles.edit_Vdc_perc_sixstep,'Visible','off');
        set(handles.text_Vdc_perc_sixstep,'Visible','off');
        set(handles.text_Vdc_perc_sixstep_units,'Visible','off');
        set(handles.edit_Is_max_sixstep,'Visible','on');
        set(handles.text_Is_max_sixstep,'Visible','on');
        set(handles.text_Is_max_sixstep_units,'Visible','on');
        set(handles.edit_Is_hyst_perc_sixstep,'Visible','on');
        set(handles.text_Is_hyst_perc_sixstep,'Visible','on');
        set(handles.text_Is_hyst_perc_sixstep_units,'Visible','on');  
    elseif strcmp(Drive.SixStepOptions,'Six-step with variable DC voltage')
        set(handles.edit_fspwm,'Visible','on');
        set(handles.text_fspwm,'Visible','on');
        set(handles.text_fspwm_units,'Visible','on');
        set(handles.edit_Vdc_perc_sixstep,'Visible','on');
        set(handles.text_Vdc_perc_sixstep,'Visible','on');
        set(handles.text_Vdc_perc_sixstep_units,'Visible','on');
        set(handles.edit_Is_max_sixstep,'Visible','off');
        set(handles.text_Is_max_sixstep,'Visible','off');
        set(handles.text_Is_max_sixstep_units,'Visible','off');
        set(handles.edit_Is_hyst_perc_sixstep,'Visible','off');
        set(handles.text_Is_hyst_perc_sixstep,'Visible','off');
        set(handles.text_Is_hyst_perc_sixstep_units,'Visible','off');      
    end
end
% % Update PlotWizard
% motoranalysishandles = guidata(handles.motoranalysis);
% PlotWizard = motoranalysishandles.PlotWizard;
% PlotWizardHandles = guidata(PlotWizard);
% PlotWizardHandles.UpdatePlotWizard(PlotWizard,[]);


function editdriveCallback(hObject, eventdata, handles)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Drive = Simulation.Drive;
% editbox Tag
Tag = get(hObject,'Tag');
if strcmp(Tag(1:4),'edit')     % if editbox changed
    % editbox value
    String = get(hObject,'String');
    DriveField = Tag(6:end);
    if isfield(Drive,DriveField)
        [DriveFieldValue, status] = str2num(String);
        if length(DriveFieldValue)>1
            status=0;
        end
        if ~isempty(DriveFieldValue) && status && isreal(DriveFieldValue) && ~isinf(DriveFieldValue) && ~isnan(DriveFieldValue) && DriveFieldValue>=0
            Drive = setfield(Drive,DriveField,DriveFieldValue);
        else
            errordlg('Not a valid value.','Drive Settings Error','modal');
            editbox=['edit_' DriveField];
            set(handles.(editbox),'String',num2str(Drive.(DriveField)));
            return
        end
    end
elseif strcmp(Tag(1:3),'pup')     % if popupmenu changed
    % popupmenu value
    index = get(hObject,'Value');
    strlist = get(hObject,'String');
    String = strlist{index,1};
    Field = Tag(5:end);
    if isfield(Drive,Field)
        if ~isempty(String)
            Drive = setfield(Drive,Field,String);
        else
            error('Something goes wrong');
        end
    end
    if strcmp(Field,'DriveType')
        if index==1 || index==2  % DriveType==Current hysteresis PWM || DriveType==Space vector PWM
            if strcmp(Simulation.Settings.DynamicFEA.DF_settings,'General')
                Simulation.Settings.DynamicFEA.DF_SpeedDependency = 'Fixed speed simulation';
            end
            Simulation.Settings.DynamicDQ.DD_SpeedDependency = 'Fixed speed simulation';
        end
        if strcmp(Simulation.Settings.DynamicFEA.DF_settings,'General')
            if index==1         % 'Current hysteresis PWM'
                Simulation.Settings.DynamicFEA.DF_script = 'simscript_hystpwm.m';
            elseif index==2     % 'Space vector PWM'
                Simulation.Settings.DynamicFEA.DF_script = 'simscript_spacevecpwm.m';
            elseif index==3     % 'Six-step'
                Simulation.Settings.DynamicFEA.DF_script = 'simscript_sixstep.m';
            end
            Simulation.Settings.DynamicFEA.DF_statorcircuit = 'InverterCircuit';
        end
    end
else
    error('Undefined field');
end
Simulation.Drive = Drive;
motoranalysishandles.Simulation = Simulation;
motoranalysishandles.Saved = 0;
guidata(handles.motoranalysis,motoranalysishandles);
motoranalysishandles.Update(handles.motoranalysis);
UpdateDriveSettings(hObject);
% Update PlotWizard
PlotWizard = motoranalysishandles.PlotWizard;
PlotWizardHandles = guidata(PlotWizard);
PlotWizardHandles.UpdatePlotWizard(PlotWizard,[]);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% --- Executes during object creation, after setting all properties.
function pup_DriveType_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_DriveType (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_Vdc_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Vdc (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_Is_hyst_perc_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Is_hyst_perc (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_fspwm_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_fspwm (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_SixStepOptions_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_SixStepOptions (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_CommutationAdvanceAngle_sixstep_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_CommutationAdvanceAngle_sixstep (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_SwitchDutyCycle_sixstep_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_SwitchDutyCycle_sixstep (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_Is_max_sixstep_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Is_max_sixstep (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_Is_hyst_perc_sixstep_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Is_hyst_perc_sixstep (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_Vdc_perc_sixstep_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Vdc_perc_sixstep (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

"""

def drivesettings(*args, **kwargs):
    """Placeholder for translated MATLAB function."""
    raise NotImplementedError(
        "This function requires manual translation from MATLAB."
    )
