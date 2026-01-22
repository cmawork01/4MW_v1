function varargout = ironlosscalculator(varargin)
% IRONLOSSCALCULATOR M-file for ironlosscalculator.fig
%      IRONLOSSCALCULATOR, by itself, creates a new IRONLOSSCALCULATOR or raises the existing
%      singleton*.
%
%      H = IRONLOSSCALCULATOR returns the handle to a new IRONLOSSCALCULATOR or the handle to
%      the existing singleton*.
%
%      IRONLOSSCALCULATOR('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in IRONLOSSCALCULATOR.M with the given input arguments.
%
%      IRONLOSSCALCULATOR('Property','Value',...) creates a new IRONLOSSCALCULATOR or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before ironlosscalculator_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to ironlosscalculator_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help ironlosscalculator

% Last Modified by GUIDE v2.5 21-Oct-2015 14:07:24

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @ironlosscalculator_OpeningFcn, ...
                   'gui_OutputFcn',  @ironlosscalculator_OutputFcn, ...
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


% --- Executes just before ironlosscalculator is made visible.
function ironlosscalculator_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to ironlosscalculator (see VARARGIN)

% Choose default command line output for ironlosscalculator
handles.output = hObject;

motoranalysisInput = find(strcmp(varargin, 'motoranalysis'));
if ~isempty(motoranalysisInput)
   handles.motoranalysis = varargin{motoranalysisInput+1};
end
% publish function setupironlosscalc
handles.setupironlosscalc = @setupironlosscalc;

strlist = cell(1,1); strlist{1,1} = cd;
set(handles.pup_datasource,'String',strlist);

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes ironlosscalculator wait for user response (see UIRESUME)
% uiwait(handles.IronLossCalculator);


% --- Outputs from this function are returned to the command line.
function varargout = ironlosscalculator_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes when user attempts to close IronLossCalculator.
function IronLossCalculator_CloseRequestFcn(hObject, eventdata, handles)
% Don't close this figure. It must be deleted from motoranalysis
% Make it invisible then user tries to close it
set(hObject,'Visible','off');


% --- Executes on button press in pushbutton_startcalculation.
function pushbutton_startcalculation_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_startcalculation (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% handles = guidata(hObject);
Tag = get(hObject,'Tag');
motoranalysishandles = guidata(handles.motoranalysis);
if isempty(motoranalysishandles.File)
    errordlg('No simulation file opened.','Iron Loss Calculator Error','modal');
    return;
end
Simulation = motoranalysishandles.Simulation;
if isempty(Simulation.Private)
    errordlg('No simulation data computed','Iron Loss Calculator Error','modal');
    return;
end    
nSlices=Simulation.Mesh.nSlices;
Subdomains=Simulation.Private.Subdomains;
Mesh=Simulation.Mesh;
Geometry=Simulation.Geometry;
nper=Simulation.Private.nper;
tbyp=Simulation.Private.tbyp;
MaterialProperties=Simulation.Private.MaterialProperties;
l=Geometry.l/1000;
[starttime, status]=str2num(get(handles.edit_starttime,'String'));
if isempty(starttime) || ~status || length(starttime)>1 || ~isreal(starttime) || starttime<0
    errordlg('Not a valid value for ''Time interval (from)''','Iron Loss Calculator Error','modal');
    return
end
[stoptime, status]=str2num(get(handles.edit_stoptime,'String'));
if isempty(stoptime) || ~status || length(stoptime)>1 || ~isreal(stoptime) || stoptime<0
    errordlg('Not a valid value for ''Time interval (to)''','Iron Loss Calculator Error','modal');
    return
end
if strcmp(Tag,'pushbutton_startcalculation')
    [frq_max, status]=str2num(get(handles.edit_frq_max,'String'));
    if isempty(frq_max) || ~status || length(frq_max)>1 || ~isreal(frq_max) || frq_max<=0
        errordlg('Not a valid value for ''Maximum fft frequency of flux density'' field','Iron Loss Calculator Error','modal');
        return
    end
else
    frq_max=inf;
end
strlist=cellstr(get(handles.pup_datasource,'String'));
datadir=strlist{get(handles.pup_datasource,'Value')};
set(handles.IronLossCalculator,'Pointer','watch');
[Piron, Piron_stator, Piron_rotor, Piron_density, details] = ironlosstransient(datadir,starttime,stoptime,l,Mesh,Geometry,Subdomains,nSlices,nper,tbyp,MaterialProperties,frq_max,handles,Tag);
if ~isempty(Piron)
    Simulation.DynamicFEA.Piron.rotor=Piron_rotor; 
    Simulation.DynamicFEA.Piron.stator=Piron_stator; 
    Simulation.DynamicFEA.Piron.details=details; 
    Simulation.DynamicFEA.Piron_density=Piron_density; 
    motoranalysishandles.Simulation=Simulation;
    guidata(handles.motoranalysis,motoranalysishandles);
    motoranalysishandles.Save_Callback(motoranalysishandles.menuSave,[],motoranalysishandles);
end
set(handles.IronLossCalculator,'Pointer','arrow');
dispironloss(handles);


% --- Executes on button press in pushbutton_changedatasource.
function pushbutton_changedatasource_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_changedatasource (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% Allow the user to select the directory
start_path = cd;
directory_name = uigetdir(start_path,'Select a Directory');
if strfind(directory_name,cd)==1
    if length(directory_name)>length(cd)
        directory_name(1:length(cd)+1)=[];
    end
end
    
% If 'Cancel' was selected then return
if isequal(directory_name,0)
    return
else
    changedatasource(handles,directory_name);
end

function changedatasource(handles,directory_name)
strlist = get(handles.pup_datasource,'String');
for i=1:length(strlist)
    if strcmp(directory_name,strlist(i))
        break;
    elseif i==length(strlist)  % if thire is no directory_name in strlist then add it
        strlist_ = strlist;
        strlist = cell(length(strlist)+1,1);
        for j=1:length(strlist_)
            strlist{j,1}=strlist_{j,1};
        end
        i = i+1;
        strlist{i,1} = directory_name;
        set(handles.pup_datasource,'String',strlist);
        break;
    end
end
set(handles.pup_datasource,'Value',i);


function setupironlosscalc(handles,CurrentTime,datasource)
set(handles.edit_stoptime,'String',num2str(CurrentTime));
set(handles.edit_starttime,'String',num2str(0));
motoranalysishandles=guidata(handles.motoranalysis);
Simulation=motoranalysishandles.Simulation;
timestep=Simulation.Settings.DynamicFEA.DF_timestep;
frq_max=1/timestep/2;
set(handles.edit_frq_max,'String',num2str(frq_max));
changedatasource(handles,datasource);
dispironloss(handles);


function dispironloss(handles)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Piron_rotor=Simulation.DynamicFEA.Piron.rotor; 
Piron_stator=Simulation.DynamicFEA.Piron.stator; 
details=Simulation.DynamicFEA.Piron.details;
if ~isempty(details)
    frq_max=details(1);
    time_begin=details(2);
    time_end=details(3);
    Ironloss_rotor_hyst=details(4); 
    Ironloss_rotor_eddy=details(5); 
    Ironloss_stator_hyst=details(6); 
    Ironloss_stator_eddy=details(7);
    FrequencyResolution=details(8:end-1);
    SuggestedMaxFrequency=details(end);
    reporttext=cell(1,0); reporttext{1}=['Iron loss - total (W):              ' num2str(Piron_rotor+Piron_stator)];
    reporttext=celladd(reporttext,      ['Iron loss - rotor (W):              ' num2str(Piron_rotor)]);
    reporttext=celladd(reporttext,      ['Iron loss - stator (W):             ' num2str(Piron_stator)]);
    reporttext=celladd(reporttext,      ['Eddy current rotor iron loss (W):   ' num2str(Ironloss_rotor_eddy)]);
    reporttext=celladd(reporttext,      ['Hysteresis rotor iron loss (W):     ' num2str(Ironloss_rotor_hyst)]);
    reporttext=celladd(reporttext,      ['Eddy current stator iron loss (W):  ' num2str(Ironloss_stator_eddy)]);
    reporttext=celladd(reporttext,      ['Hysteresis stator iron loss (W):    ' num2str(Ironloss_stator_hyst)]);    
    reporttext=celladd(reporttext,      ' ');
    reporttext=celladd(reporttext,'details:');
    reporttext=celladd(reporttext,['Averaging time: ' num2str(time_begin) ' - ' num2str(time_end) ' seconds']);
    reporttext=celladd(reporttext,['Flux density frequency range: 0 - ' num2str(frq_max) ' Hz']);
    reporttext=celladd(reporttext,['Frequency resolution: ' num2str(FrequencyResolution) ' Hz']);
    if SuggestedMaxFrequency
        reporttext=celladd(reporttext,['Suggested max. fft frequency: ' num2str(SuggestedMaxFrequency) ' Hz']);
    end
else
    reporttext='No iron loss computed';
end
set(handles.text_report,'String',reporttext);

% --- Executes on button press in pushbutton_set2lasttime.
function pushbutton_set2lasttime_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_set2lasttime (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
motoranalysishandles = guidata(handles.motoranalysis);
if isempty(motoranalysishandles.File)
    return;
end
Simulation = motoranalysishandles.Simulation;
DynamicFEA = Simulation.DynamicFEA;
if isempty(DynamicFEA.time)
    lasttime=0;
else
    lasttime=DynamicFEA.time(end)-DynamicFEA.time(1);
end
set(handles.edit_stoptime,'String',num2str(lasttime));


% --- Executes during object creation, after setting all properties.
function edit_starttime_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_starttime (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_stoptime_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_stoptime (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function pup_datasource_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_datasource (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_frq_max_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_frq_max (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
