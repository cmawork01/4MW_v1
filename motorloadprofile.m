function varargout = motorloadprofile(varargin)
% MOTORLOADPROFILE MATLAB code for motorloadprofile.fig
%      MOTORLOADPROFILE, by itself, creates a new MOTORLOADPROFILE or raises the existing
%      singleton*.
%
%      H = MOTORLOADPROFILE returns the handle to a new MOTORLOADPROFILE or the handle to
%      the existing singleton*.
%
%      MOTORLOADPROFILE('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in MOTORLOADPROFILE.M with the given input arguments.
%
%      MOTORLOADPROFILE('Property','Value',...) creates a new MOTORLOADPROFILE or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before motorloadprofile_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to motorloadprofile_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help motorloadprofile

% Last Modified by GUIDE v2.5 12-Aug-2017 21:05:28

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @motorloadprofile_OpeningFcn, ...
                   'gui_OutputFcn',  @motorloadprofile_OutputFcn, ...
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


% --- Executes just before motorloadprofile is made visible.
function motorloadprofile_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to motorloadprofile (see VARARGIN)

% Choose default command line output for motorloadprofile
handles.output = [];

input = find(strcmp(varargin, 'LoadPrfl'));
if ~isempty(input)
   LoadProfile=varargin{input+1};
   if ~iscell(LoadProfile)
       LoadProfile={0 inf LoadProfile};
   end
   handles.LoadProfile=LoadProfile;
else
    error(' ');
end

% Update handles structure
guidata(hObject, handles);
updateloadprofile(hObject);

% UIWAIT makes motorloadprofile wait for user response (see UIRESUME)
uiwait(handles.motorloadprofile);


% --- Outputs from this function are returned to the command line.
function varargout = motorloadprofile_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;
delete(hObject);


function updateloadprofile(hObject)
handles = guidata(hObject);
LoadProfile=handles.LoadProfile;
nlines=size(LoadProfile,1);
for i=1:nlines
    set(handles.(['edit_timefrom' num2str(i)]),'String',num2str(LoadProfile{i,1}));
    set(handles.(['edit_timeto' num2str(i)]),'String',num2str(LoadProfile{i,2}));
    if isnumeric(LoadProfile{i,2})
        set(handles.(['edit_loadexpression' num2str(i)]),'String',num2str(LoadProfile{i,3}));
    else
        set(handles.(['edit_loadexpression' num2str(i)]),'String',LoadProfile{i,3});
    end
    set(handles.(['edit_loadexpression' num2str(i)]),'Enable','on');
    if size(LoadProfile,1)==1
        set(handles.(['pushbutton_addtimeinterval' num2str(i)]),'Enable','off');
    else
        set(handles.(['pushbutton_addtimeinterval' num2str(i)]),'Enable','on');
    end
    set(handles.(['pushbutton_addtimeinterval' num2str(i)]),'String','-');
    set(handles.(['pushbutton_addtimeinterval' num2str(i)]),'TooltipString','Delete time interval');
    if i==nlines
        set(handles.(['edit_timeto' num2str(i)]),'Enable','off');
    else
        set(handles.(['edit_timeto' num2str(i)]),'Enable','on');
    end
end
for i=nlines+1:5
    if i==nlines+1
        set(handles.(['pushbutton_addtimeinterval' num2str(i)]),'TooltipString','Add new time interval');
        set(handles.(['pushbutton_addtimeinterval' num2str(i)]),'Enable','on');
    else
        set(handles.(['pushbutton_addtimeinterval' num2str(i)]),'Enable','off');  
    end    
    set(handles.(['edit_timefrom' num2str(i)]),'String','');
    set(handles.(['edit_timeto' num2str(i)]),'String','');
    set(handles.(['edit_loadexpression' num2str(i)]),'String','');
    set(handles.(['pushbutton_addtimeinterval' num2str(i)]),'String','+');
    set(handles.(['edit_timefrom' num2str(i)]),'Enable','off');
    set(handles.(['edit_timeto' num2str(i)]),'Enable','off');
    set(handles.(['edit_loadexpression' num2str(i)]),'Enable','off');
end


function edit_edittimeinterval_Callback(hObject, eventdata, handles)
% hObject    handle to edit_timefrom1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
LoadProfile=handles.LoadProfile;
Tag = get(hObject,'Tag');
nline=str2num(Tag(12:end));
String = get(hObject,'String');
[FieldValue, status] = str2num(String);
if isempty(FieldValue) || ~status || length(FieldValue)>1 || ~isreal(FieldValue) || isinf(FieldValue) || isnan(FieldValue) || FieldValue<=0
    errordlg('Not a valid value.','Error','modal');
    updateloadprofile(hObject);
    return
else
    if (nline==1 && FieldValue<LoadProfile{nline+1,2}) || (nline>1 && FieldValue>LoadProfile{nline-1,2} && FieldValue<LoadProfile{nline+1,2})
        LoadProfile{nline,2}=FieldValue;
        LoadProfile{nline+1,1}=FieldValue;
    else
        errordlg('Intervals should be in increasing order.','Error','modal');
        updateloadprofile(hObject);
        return
    end
end
handles.LoadProfile=LoadProfile;
guidata(hObject, handles);
updateloadprofile(hObject);


function editloadexpression_Callback(hObject, eventdata, handles)
% hObject    handle to edit_loadexpression1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
LoadProfile=handles.LoadProfile;
Tag = get(hObject,'Tag');
nline=str2num(Tag(20:end));
String = get(hObject,'String');
[FieldValue, status] = str2num(String);
if ~isempty(FieldValue) && status   % if number
    if length(FieldValue)>1 || ~isreal(FieldValue) || isinf(FieldValue) || isnan(FieldValue) || FieldValue<0
        errordlg('Not a valid value.','Error','modal');
        updateloadprofile(hObject);
        return
    else
        LoadProfile{nline,3}=FieldValue;    % write as number
    end
else   % if string
    if isempty(String)
        errordlg('Not a valid value.','Error','modal');
        updateloadprofile(hObject);
        return
    end
    LoadProfile{nline,3}=String;    % write as string
end
set(hObject,'ForegroundColor',[0 0 0]);    % black color
handles.LoadProfile=LoadProfile;
guidata(hObject, handles);
updateloadprofile(hObject);


% --- Executes on button press in pushbutton_addtimeinterval1.
function pushbutton_addtimeinterval_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_addtimeinterval1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
LoadProfile=handles.LoadProfile;
Tag = get(hObject,'Tag');
nline=str2num(Tag(27:end));
if nline==size(LoadProfile,1)+1    % add new time interval
    for i=1:size(LoadProfile,1)
        if isempty(LoadProfile{i,2})
            errordlg('Fill in an empty field.','Error','modal');
            return
        end
    end
    LoadProfile_old=LoadProfile;
    LoadProfile=cell(nline,3);
    for i=1:nline-1
        LoadProfile{i,1}=LoadProfile_old{i,1};
        LoadProfile{i,2}=LoadProfile_old{i,2};
        LoadProfile{i,3}=LoadProfile_old{i,3};
    end
    LoadProfile{nline-1,2}=[];
    LoadProfile{nline,1}=[];
    LoadProfile{nline,2}=inf;
    LoadProfile{nline,3}=LoadProfile_old{nline-1,3};
else                             % delete time interval
    if size(LoadProfile,1)==1
        return
    end
    LoadProfile_old=LoadProfile;
    LoadProfile=cell(size(LoadProfile,1)-1,3);
    for i=1:size(LoadProfile,1)
        if i<=nline-1
            LoadProfile{i,1}=LoadProfile_old{i,1};
            LoadProfile{i,2}=LoadProfile_old{i,2};
            LoadProfile{i,3}=LoadProfile_old{i,3};
            if nline==size(LoadProfile_old,1)
                if i==nline-1
                    LoadProfile{i,2}=inf;
                end
            end
        elseif i==nline
            if nline==1
                LoadProfile{1,1}=0;
            else
                LoadProfile{i,1}=LoadProfile_old{i-1,2};
            end
            LoadProfile{i,2}=LoadProfile_old{i+1,2};
            LoadProfile{i,3}=LoadProfile_old{i+1,3};
        else   % i>nline
            LoadProfile{i,1}=LoadProfile_old{i+1,1};
            LoadProfile{i,2}=LoadProfile_old{i+1,2};
            LoadProfile{i,3}=LoadProfile_old{i+1,3};
        end
    end
end
handles.LoadProfile=LoadProfile;
guidata(hObject, handles);
updateloadprofile(hObject);


% --- Executes on button press in pushbutton_cancel.
function pushbutton_cancel_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_cancel (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.output=[];
guidata(hObject, handles);
uiresume(handles.motorloadprofile);

% --- Executes on button press in pushbutton_ok.
function pushbutton_ok_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_ok (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
LoadProfile=handles.LoadProfile;
time=1; w=1; rpm=1;
for i=1:size(LoadProfile,1)
    if isempty(LoadProfile{i,2})
        errordlg('Fill in an empty field.','Error','modal');
        return
    end
    try
        eval(['load=' num2str(LoadProfile{i,3}) ';']);
    catch
        set(handles.(['edit_loadexpression' num2str(i)]),'ForegroundColor',[1 0 0]);     % mark red
        guidata(hObject, handles);
        errordlg('Incorrect load expression.','Error','modal');
        updateloadprofile(hObject);
        return
    end
end
if size(LoadProfile,1)==1
    if isnumeric(LoadProfile{1,3})   % if number
        LoadProfile=LoadProfile{1,3};
    end    
end
handles.output=LoadProfile;
guidata(hObject, handles);
uiresume(handles.motorloadprofile);

% --- Executes when user attempts to close motorloadprofile.
function motorloadprofile_CloseRequestFcn(hObject, eventdata, handles)
% hObject    handle to motorloadprofile (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.output=[];
guidata(hObject, handles);
uiresume(hObject);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% --- Executes during object creation, after setting all properties.
function edit_timefrom1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_timefrom1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_timefrom2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_timefrom2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_timefrom3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_timefrom3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_timefrom4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_timefrom4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_timefrom5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_timefrom5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_timeto1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_timeto1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_timeto2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_timeto2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_timeto3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_timeto3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_timeto4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_timeto4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_timeto5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_timeto5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_loadexpression1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_loadexpression1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_loadexpression2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_loadexpression2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_loadexpression3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_loadexpression3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_loadexpression4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_loadexpression4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_loadexpression5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_loadexpression5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
