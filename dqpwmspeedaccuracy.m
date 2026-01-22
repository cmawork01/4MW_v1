function varargout = dqpwmspeedaccuracy(varargin)
% DQPWMSPEEDACCURACY MATLAB code for dqpwmspeedaccuracy.fig
%      DQPWMSPEEDACCURACY, by itself, creates a new DQPWMSPEEDACCURACY or raises the existing
%      singleton*.
%
%      H = DQPWMSPEEDACCURACY returns the handle to a new DQPWMSPEEDACCURACY or the handle to
%      the existing singleton*.
%
%      DQPWMSPEEDACCURACY('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in DQPWMSPEEDACCURACY.M with the given input arguments.
%
%      DQPWMSPEEDACCURACY('Property','Value',...) creates a new DQPWMSPEEDACCURACY or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before dqpwmspeedaccuracy_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to dqpwmspeedaccuracy_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help dqpwmspeedaccuracy

% Last Modified by GUIDE v2.5 11-Sep-2017 14:20:17

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @dqpwmspeedaccuracy_OpeningFcn, ...
                   'gui_OutputFcn',  @dqpwmspeedaccuracy_OutputFcn, ...
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


% --- Executes just before dqpwmspeedaccuracy is made visible.
function dqpwmspeedaccuracy_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to dqpwmspeedaccuracy (see VARARGIN)

% Choose default command line output for dqpwmspeedaccuracy
handles.output = [];

input = find(strcmp(varargin,'SA'));
if ~isempty(input)
   SA=varargin{input+1};
   if ~isempty(SA)
        setSA(SA,handles);
   end
end
input = find(strcmp(varargin, 'DriveSettings'));
if ~isempty(input)
   handles.DriveSettings = varargin{input+1};
end

% Update handles structure
guidata(hObject, handles);
updatespeedaccuracy(hObject);

% UIWAIT makes dqpwmspeedaccuracy wait for user response (see UIRESUME)
uiwait(handles.dqpwmspeedaccuracy);


% --- Outputs from this function are returned to the command line.
function varargout = dqpwmspeedaccuracy_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;
delete(hObject);


% --- Executes on selection change in pup_speedaccuracy_setup.
function editspeedaccuracy_Callback(hObject, eventdata, handles)
updatespeedaccuracy(hObject);


function updatespeedaccuracy(hObject)
handles = guidata(hObject);
SA=getSA(handles);
drivesettingshandles = guidata(handles.DriveSettings);
strlist = get(drivesettingshandles.pup_DriveType,'String');
n=get(drivesettingshandles.pup_DriveType,'Value');
DriveType=strlist(n);
set(handles.text_speedaccuracy_Ndt,'Visible','on');
if strcmp(DriveType,'Current hysteresis PWM')
    set(handles.pup_speedaccuracy_Ndt_sv,'Visible','off');
    set(handles.pup_speedaccuracy_Ndt_ch,'Visible','on');
    set(handles.pup_speedaccuracy_Itol,'Visible','off');  
    set(handles.text_speedaccuracy_Itol,'Visible','off');  
else
    set(handles.pup_speedaccuracy_Ndt_sv,'Visible','on');
    set(handles.pup_speedaccuracy_Ndt_ch,'Visible','off');    
    set(handles.pup_speedaccuracy_Itol,'Visible','on');  
    set(handles.text_speedaccuracy_Itol,'Visible','on');  
end
if strcmp(SA.speedaccuracy_setup,'User choice')
    set(handles.pup_speedaccuracy_solvertype,'Enable','on');
    set(handles.pup_speedaccuracy_Ndt_sv,'Enable','on');
    set(handles.pup_speedaccuracy_Ndt_ch,'Enable','on');
    set(handles.pup_speedaccuracy_Itol,'Enable','on');
    set(handles.pup_speedaccuracy_timestepselection,'Enable','on');
else
    set(handles.pup_speedaccuracy_solvertype,'Enable','off');
    set(handles.pup_speedaccuracy_Ndt_sv,'Enable','off');
    set(handles.pup_speedaccuracy_Ndt_ch,'Enable','off');
    set(handles.pup_speedaccuracy_Itol,'Enable','off');  
    set(handles.pup_speedaccuracy_timestepselection,'Enable','off');
    SA.speedaccuracy_timestepselection='Automatic';
    if strcmp(SA.speedaccuracy_setup,'Fastest')
        SA.speedaccuracy_solvertype='Linear';
        SA.speedaccuracy_Ndt_sv='30';
        SA.speedaccuracy_Ndt_ch='3';
        SA.speedaccuracy_Itol='2%';
    elseif strcmp(SA.speedaccuracy_setup,'Balanced')
        SA.speedaccuracy_solvertype='Linearized';
        SA.speedaccuracy_Ndt_sv='50';
        SA.speedaccuracy_Ndt_ch='10';
        SA.speedaccuracy_Itol='0.5%';
    elseif strcmp(SA.speedaccuracy_setup,'Accurate')
        SA.speedaccuracy_solvertype='Nonlinear';
        SA.speedaccuracy_Ndt_sv='150';
        SA.speedaccuracy_Ndt_ch='50';
        SA.speedaccuracy_Itol='0.1%';
    else
        error(' ');
    end
end
if strcmp(SA.speedaccuracy_timestepselection,'Automatic')
    set(handles.edit_speedaccuracy_timestep,'Visible','off');  
    set(handles.text_speedaccuracy_timestep,'Visible','off');  
else   % timestepselection=='Manual'
    set(handles.edit_speedaccuracy_timestep,'Visible','on');  
    set(handles.text_speedaccuracy_timestep,'Visible','on');  
    set(handles.text_speedaccuracy_Ndt,'Visible','off');
    set(handles.pup_speedaccuracy_Ndt_sv,'Visible','off');
    set(handles.pup_speedaccuracy_Ndt_ch,'Visible','off');
end
setSA(SA,handles);


function SA=getSA(handles)
SA.speedaccuracy_setup='';
SA.speedaccuracy_solvertype='';
SA.speedaccuracy_Ndt_sv='';
SA.speedaccuracy_Ndt_ch='';
SA.speedaccuracy_Itol='';
SA.speedaccuracy_timestepselection='';
SA.speedaccuracy_timestep='';
SAFields = fieldnames(SA);
for i=1:length(SAFields)
    SAField = SAFields{i};
    if strcmp(SAField,'speedaccuracy_timestep')
        strvalue=get(handles.edit_speedaccuracy_timestep,'String');
        [value, status] = str2num(strvalue);
        if ~status || length(value)~=1 || ~isreal(value) || isinf(value) || isnan(value) || value<=0
            errordlg('Not a valid value.','Time step error','modal');
            value=0.000001;
        end
        SA.speedaccuracy_timestep=value;
    else
        popup = ['pup_' SAField];
        strlist = get(getfield(handles,popup),'String');
        n=get(getfield(handles,popup),'Value');
        SA=setfield(SA,SAField,strlist(n));
    end
end


function setSA(SA,handles)
SAFields = fieldnames(SA);
for i=1:length(SAFields)
    SAField = SAFields{i};
    edit = ['edit_' SAField];
    if isfield(handles,edit)           % if editbox
        SAFieldValue = getfield(SA,SAField);
        set(getfield(handles,edit),'String',num2str(SAFieldValue));
    end
    popup = ['pup_' SAField];    
    if isfield(handles,popup)           % if popup menu
        SAFieldValue = getfield(SA,SAField);
        strlist = get(getfield(handles,popup),'String');
        for n=1:length(strlist)
            if strcmp(SAFieldValue,strlist(n))
                break;
            elseif n==length(strlist)
                error(['Inappropriate value for <' SAField '>: something goes wrong']);
            end
        end
        set(getfield(handles,popup),'Value',n);
    end
end
guidata(handles.dqpwmspeedaccuracy,handles);


% --- Executes when user attempts to close dqpwmspeedaccuracy.
function dqpwmspeedaccuracy_CloseRequestFcn(hObject, eventdata, handles)
% hObject    handle to dqpwmspeedaccuracy (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: delete(hObject) closes the figure
handles.output=[];
guidata(hObject, handles);
uiresume(hObject);


% --- Executes on button press in pushbutton_cancel.
function pushbutton_cancel_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_cancel (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.output=[];
guidata(hObject, handles);
uiresume(handles.dqpwmspeedaccuracy);


% --- Executes on button press in pushbutton_ok.
function pushbutton_ok_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_ok (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
SA=getSA(handles);
handles.output=SA;
guidata(hObject, handles);
uiresume(handles.dqpwmspeedaccuracy);

% --- Executes during object creation, after setting all properties.
function pup_speedaccuracy_setup_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_speedaccuracy_setup (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_speedaccuracy_solvertype_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_speedaccuracy_solvertype (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_speedaccuracy_Ndt_sv_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_speedaccuracy_Ndt_sv (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_speedaccuracy_Itol_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_speedaccuracy_Itol (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_speedaccuracy_Ndt_ch_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_speedaccuracy_Ndt_ch (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_speedaccuracy_timestepselection_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_speedaccuracy_timestepselection (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_speedaccuracy_timestep_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_speedaccuracy_timestep (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
