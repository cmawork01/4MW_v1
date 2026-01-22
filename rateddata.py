# Auto-generated from rateddata.m
# NOTE: This is a placeholder stub. Manual translation required.

from __future__ import annotations

"""
Original MATLAB source:

function varargout = rateddata(varargin)
% RATEDDATA MATLAB code for rateddata.fig
%      RATEDDATA, by itself, creates a new RATEDDATA or raises the existing
%      singleton*.
%
%      H = RATEDDATA returns the handle to a new RATEDDATA or the handle to
%      the existing singleton*.
%
%      RATEDDATA('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in RATEDDATA.M with the given input arguments.
%
%      RATEDDATA('Property','Value',...) creates a new RATEDDATA or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before rateddata_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to rateddata_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help rateddata

% Last Modified by GUIDE v2.5 10-Aug-2017 13:07:44

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @rateddata_OpeningFcn, ...
                   'gui_OutputFcn',  @rateddata_OutputFcn, ...
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


% --- Executes just before rateddata is made visible.
function rateddata_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to rateddata (see VARARGIN)

% Choose default command line output for rateddata
handles.output = hObject;

motoranalysisInput = find(strcmp(varargin, 'motoranalysis'));
if ~isempty(motoranalysisInput)
   handles.motoranalysis = varargin{motoranalysisInput+1};
end
% publish function UpdateRatedData
handles.UpdateRatedData = @UpdateRatedData;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes rateddata wait for user response (see UIRESUME)
% uiwait(handles.RatedData);


% --- Outputs from this function are returned to the command line.
function varargout = rateddata_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes when user attempts to close RatedData.
function RatedData_CloseRequestFcn(hObject, eventdata, handles)
% Don't close this figure. It must be deleted from motoranalysis
% Make it invisible then user tries to close it
set(hObject,'Visible','off');
motoranalysishandles = guidata(handles.motoranalysis);
set(motoranalysishandles.menuRatedData,'Checked','off');


function UpdateRatedData(hObject)
handles = guidata(hObject);
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
% update editbox values
RatedData = Simulation.RatedData;
RatedDataFields = fieldnames(RatedData);
for i=1:length(RatedDataFields)
    RatedDataField = RatedDataFields{i};
    editbox = ['edit_' RatedDataField];
    if isfield(handles,editbox)           % if editbox
        RatedDataFieldValue = getfield(RatedData,RatedDataField);
        set(getfield(handles,editbox),'String',num2str(RatedDataFieldValue,10));
    end
end


function editrateddata_Callback(hObject, eventdata, handles)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
RatedData = Simulation.RatedData;
% editbox Tag
Tag = get(hObject,'Tag');
if strcmp(Tag(1:4),'edit')     % if editbox changed
    % editbox value
    String = get(hObject,'String');
    RatedDataField = Tag(6:end);
    if isfield(RatedData,RatedDataField)
        if ~isempty(String)
            [RatedDataFieldValue, status] = str2num(String);
            if length(RatedDataFieldValue)>1
                status=0;
            end
            if status && isreal(RatedDataFieldValue) && ~isinf(RatedDataFieldValue) && ~isnan(RatedDataFieldValue) && RatedDataFieldValue>0
                RatedData = setfield(RatedData,RatedDataField,RatedDataFieldValue);
            else
                errordlg('Not a valid value.','Rated Data Error','modal');
                editbox=['edit_' RatedDataField];
                set(getfield(handles,editbox),'String','');
                return
            end
        else
            RatedData = setfield(RatedData,RatedDataField,[]);
        end
    end
else
    error('Undefined field');
end
Simulation.RatedData = RatedData;
motoranalysishandles.Simulation = Simulation;
motoranalysishandles.Saved = 0;
guidata(handles.motoranalysis,motoranalysishandles);


% --- Executes during object creation, after setting all properties.
function edit_RatedCurrent_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_RatedCurrent (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_RatedPower_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_RatedPower (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_RatedSpeed_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_RatedSpeed (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_MomentInertia_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_MomentInertia (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

"""

def rateddata(*args, **kwargs):
    """Placeholder for translated MATLAB function."""
    raise NotImplementedError(
        "This function requires manual translation from MATLAB."
    )
