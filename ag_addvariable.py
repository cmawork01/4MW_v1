# Auto-generated from ag_addvariable.m
# NOTE: This is a placeholder stub. Manual translation required.

from __future__ import annotations

"""
Original MATLAB source:

function varargout = ag_addvariable(varargin)
% AG_ADDVARIABLE M-file for ag_addvariable.fig
%      AG_ADDVARIABLE, by itself, creates a new AG_ADDVARIABLE or raises the existing
%      singleton*.
%
%      H = AG_ADDVARIABLE returns the handle to a new AG_ADDVARIABLE or the handle to
%      the existing singleton*.
%
%      AG_ADDVARIABLE('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in AG_ADDVARIABLE.M with the given input arguments.
%
%      AG_ADDVARIABLE('Property','Value',...) creates a new AG_ADDVARIABLE or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before ag_addvariable_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to ag_addvariable_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help ag_addvariable

% Last Modified by GUIDE v2.5 23-Sep-2013 09:33:57

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @ag_addvariable_OpeningFcn, ...
                   'gui_OutputFcn',  @ag_addvariable_OutputFcn, ...
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


% --- Executes just before ag_addvariable is made visible.
function ag_addvariable_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to ag_addvariable (see VARARGIN)

% Choose default command line output for ag_addvariable
handles.output = [];

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes ag_addvariable wait for user response (see UIRESUME)
uiwait(handles.ag_addvariable);


% --- Outputs from this function are returned to the command line.
function varargout = ag_addvariable_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;
delete(hObject);

% --- Executes when selected cell(s) is changed in table_variables.
function table_variables_CellSelectionCallback(hObject, eventdata, handles)
% hObject    handle to table_variables (see GCBO)
% eventdata  structure with the following fields (see UITABLE)
%	Indices: row and column indices of the cell(s) currently selecteds
% handles    structure with handles and user data (see GUIDATA)
inds=eventdata.Indices;
inds=inds(:,1);
varslist=cell(length(inds),1);
Variables=get(handles.table_variables, 'Data');
for i=1:length(inds)
    var=Variables{inds(i),1};
    ispace=findstr(var,' '); ispace=ispace(1)-1;
    var=var(1:ispace);
    varslist{i,1}=var;    
end
handles.output=varslist;
guidata(hObject, handles);


% --- Executes on button press in pushbutton_add.
function pushbutton_add_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_add (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
uiresume(handles.ag_addvariable);

% --- Executes on button press in pushbutton_cancel.
function pushbutton_cancel_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_cancel (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.output=[];
guidata(hObject, handles);
uiresume(handles.ag_addvariable);

% --- Executes when user attempts to close ag_addvariable.
function ag_addvariable_CloseRequestFcn(hObject, eventdata, handles)
% hObject    handle to ag_addvariable (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% Hint: delete(hObject) closes the figure
handles.output=[];
guidata(hObject, handles);
uiresume(hObject);

"""

def ag_addvariable(*args, **kwargs):
    """Placeholder for translated MATLAB function."""
    raise NotImplementedError(
        "This function requires manual translation from MATLAB."
    )
