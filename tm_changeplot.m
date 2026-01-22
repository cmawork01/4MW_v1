function varargout = tm_changeplot(varargin)
% TM_CHANGEPLOT M-file for tm_changeplot.fig
%      TM_CHANGEPLOT, by itself, creates a new TM_CHANGEPLOT or raises the existing
%      singleton*.
%
%      H = TM_CHANGEPLOT returns the handle to a new TM_CHANGEPLOT or the handle to
%      the existing singleton*.
%
%      TM_CHANGEPLOT('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in TM_CHANGEPLOT.M with the given input arguments.
%
%      TM_CHANGEPLOT('Property','Value',...) creates a new TM_CHANGEPLOT or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before tm_changeplot_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to tm_changeplot_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help tm_changeplot

% Last Modified by GUIDE v2.5 14-Oct-2013 14:04:13

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @tm_changeplot_OpeningFcn, ...
                   'gui_OutputFcn',  @tm_changeplot_OutputFcn, ...
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


% --- Executes just before tm_changeplot is made visible.
function tm_changeplot_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to tm_changeplot (see VARARGIN)

% Choose default command line output for tm_changeplot
handles.output = [];

input = find(strcmp(varargin, 'varslist'));
if ~isempty(input)
   Data=varargin{input+1};
   set(getfield(handles,'table_variables'),'Data',Data);
end

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes tm_changeplot wait for user response (see UIRESUME)
uiwait(handles.tm_changeplot);


% --- Outputs from this function are returned to the command line.
function varargout = tm_changeplot_OutputFcn(hObject, eventdata, handles) 
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
handles.output=inds(:,1);
guidata(hObject, handles);


% --- Executes on button press in pushbutton_cancel.
function pushbutton_ok_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_cancel (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
plotexp=buildplotexp(handles);
handles.output=plotexp;
guidata(hObject, handles);
uiresume(handles.tm_changeplot);

function plotexp=buildplotexp(handles)
plotexp='';
inds=handles.output;
if ~isempty(inds)
    Data=get(getfield(handles,'table_variables'),'Data');
    plotexp='plot(';
    legendexp='legend(';
    for i=1:length(inds)
        var=Data{inds(i),:};
        if findstr(var,'[Not available]')
            plotexp='';
            return
        end
        i1unit=findstr(var,'[');
        i2unit=findstr(var,']');   
        if ~isempty(i1unit) && ~isempty(i2unit)
            unit=[', ' var(i1unit+1:i2unit-1)];
        else
            unit=[];
        end
        ispace=findstr(var,' '); ispace=ispace(1);
        var=var(1:ispace-1);
        if i==1
            plotexp=[plotexp 'time,' var];
            legendexp=[legendexp '''' [strrep(var,'_',' ') unit] ''''];
        else
            plotexp=[plotexp ',time,' var];
            legendexp=[legendexp ',''' [strrep(var,'_',' ') unit] ''''];
        end
    end
    plotexp=[plotexp ');'];
    legendexp=[legendexp ');'];
    if get(getfield(handles,'checkbox_legend'),'Value')
        plotexp=[plotexp legendexp];
    end
end
    

% --- Executes on button press in pushbutton_ok.
function pushbutton_cancel_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_ok (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.output=[];
guidata(hObject, handles);
uiresume(handles.tm_changeplot);

% --- Executes when user attempts to close tm_changeplot.
function tm_changeplot_CloseRequestFcn(hObject, eventdata, handles)
% hObject    handle to tm_changeplot (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: delete(hObject) closes the figure
handles.output=[];
guidata(hObject, handles);
uiresume(hObject);
