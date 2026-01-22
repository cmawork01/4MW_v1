function varargout = motoranalysissettingsgui(varargin)
% MOTORANALYSISSETTINGSGUI MATLAB code for motoranalysissettingsgui.fig
%      MOTORANALYSISSETTINGSGUI, by itself, creates a new MOTORANALYSISSETTINGSGUI or raises the existing
%      singleton*.
%
%      H = MOTORANALYSISSETTINGSGUI returns the handle to a new MOTORANALYSISSETTINGSGUI or the handle to
%      the existing singleton*.
%
%      MOTORANALYSISSETTINGSGUI('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in MOTORANALYSISSETTINGSGUI.M with the given input arguments.
%
%      MOTORANALYSISSETTINGSGUI('Property','Value',...) creates a new MOTORANALYSISSETTINGSGUI or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before motoranalysissettingsgui_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to motoranalysissettingsgui_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help motoranalysissettingsgui

% Last Modified by GUIDE v2.5 05-Feb-2018 10:51:38

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @motoranalysissettingsgui_OpeningFcn, ...
                   'gui_OutputFcn',  @motoranalysissettingsgui_OutputFcn, ...
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


% --- Executes just before motoranalysissettingsgui is made visible.
function motoranalysissettingsgui_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to motoranalysissettingsgui (see VARARGIN)

% Choose default command line output for motoranalysissettingsgui
handles.output = hObject;

if exist('profilePM.mat','file')
    load('profilePM.mat','profile');
    try
        set(handles.edit_substepmax,'String',profile.substepmax);
        set(handles.edit_relaxmin,'String',profile.relaxmin);
        set(handles.pup_convreport,'Value',profile.convreport);
        set(handles.pup_NonconvHnd,'Value',profile.NonconvHnd);
        set(handles.edit_vd,'String',profile.vd);
        set(handles.edit_vad,'String',profile.vad);
        set(handles.edit_ECLnlayers,'String',profile.ECLnlayers);
        if ~isdeployed
            set(handles.pup_MesherPreference,'Value',profile.MesherPreference);
        else
            set(handles.pup_MesherPreference,'Value',2);
            set(handles.pup_MesherPreference,'Enable','off');
        end
    catch
        pushbutton_default_Callback(hObject, eventdata, handles);
    end
else
    pushbutton_default_Callback(hObject, eventdata, handles);
end

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes motoranalysissettingsgui wait for user response (see UIRESUME)
% uiwait(handles.motoranalysissettingsgui);


% --- Outputs from this function are returned to the command line.
function varargout = motoranalysissettingsgui_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
varargout{1} = handles.output;


% --- Executes when user attempts to close motoranalysissettingsgui.
function motoranalysissettingsgui_CloseRequestFcn(hObject, eventdata, handles)
% hObject    handle to motoranalysissettingsgui (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if exist('profilePM.mat','file')
    load('profilePM.mat','profile');
end
profile.substepmax=get(handles.edit_substepmax,'String');
profile.relaxmin=get(handles.edit_relaxmin,'String');
profile.convreport=get(handles.pup_convreport,'Value');
profile.NonconvHnd=get(handles.pup_NonconvHnd,'Value');
profile.vd=get(handles.edit_vd,'String');
profile.vad=get(handles.edit_vad,'String');
profile.ECLnlayers=get(handles.edit_ECLnlayers,'String');
profile.MesherPreference=get(handles.pup_MesherPreference,'Value');
save('profilePM.mat','profile');
delete(hObject);


function editsettings_Callback(hObject, eventdata, handles)
% hObject    handle to edit_substepmax (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Tag = get(hObject,'Tag');
if strcmp(Tag,'edit_substepmax')
    Value = get(hObject,'String');
    [Value, status] = str2num(Value);
    if ~isempty(Value) && status && length(Value)==1 && Value>0 && Value<1000
        % value is correct, no action
    else
        errordlg('Not a valid value.','Settings Error','modal');
        set(hObject,'String',num2str(40));
    end
end
if strcmp(Tag,'edit_relaxmin') || strcmp(Tag,'edit_vd') || strcmp(Tag,'edit_vad')
    Value = get(hObject,'String');
    [Value, status] = str2num(Value);
    if ~isempty(Value) && status && length(Value)==1 && Value>0 && Value<1
        % value is correct, no action
    else
        errordlg('Not a valid value.','Settings Error','modal');
        if strcmp(Tag,'edit_relaxmin')
            set(hObject,'String',num2str(10^-8));
        elseif strcmp(Tag,'edit_vd')
            set(hObject,'String',num2str(10^-10));
        elseif strcmp(Tag,'edit_vad')
            set(hObject,'String',num2str(10^-9));
        end
    end
end


% --- Executes on button press in pushbutton_default.
function pushbutton_default_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_default (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
set(handles.edit_substepmax,'String','40');
set(handles.edit_relaxmin,'String','1.0e-08');
set(handles.pup_convreport,'Value',1);
set(handles.pup_NonconvHnd,'Value',2);
set(handles.edit_vd,'String','1.0e-10');
set(handles.edit_vad,'String','1.0e-09');
set(handles.edit_ECLnlayers,'String','20');
if ~isdeployed
    set(handles.pup_MesherPreference,'Value',1);
else
    set(handles.pup_MesherPreference,'Value',2);
end


% --- Executes during object creation, after setting all properties.
function edit_substepmax_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_substepmax (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_vd_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_vd (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_vad_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_vad (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_relaxmin_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_relaxmin (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_convreport_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_convreport (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_NonconvHnd_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_NonconvHnd (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_ECLnlayers_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ECLnlayers (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_MesherPreference_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_MesherPreference (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
