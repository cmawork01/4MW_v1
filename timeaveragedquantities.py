# Auto-generated from timeaveragedquantities.m
# NOTE: This is a placeholder stub. Manual translation required.

from __future__ import annotations

"""
Original MATLAB source:

function varargout = timeaveragedquantities(varargin)
% TIMEAVERAGEDQUANTITIES MATLAB code for timeaveragedquantities.fig
%      TIMEAVERAGEDQUANTITIES, by itself, creates a new TIMEAVERAGEDQUANTITIES or raises the existing
%      singleton*.
%
%      H = TIMEAVERAGEDQUANTITIES returns the handle to a new TIMEAVERAGEDQUANTITIES or the handle to
%      the existing singleton*.
%
%      TIMEAVERAGEDQUANTITIES('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in TIMEAVERAGEDQUANTITIES.M with the given input arguments.
%
%      TIMEAVERAGEDQUANTITIES('Property','Value',...) creates a new TIMEAVERAGEDQUANTITIES or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before timeaveragedquantities_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to timeaveragedquantities_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help timeaveragedquantities

% Last Modified by GUIDE v2.5 17-Aug-2017 16:08:31

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @timeaveragedquantities_OpeningFcn, ...
                   'gui_OutputFcn',  @timeaveragedquantities_OutputFcn, ...
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


% --- Executes just before timeaveragedquantities is made visible.
function timeaveragedquantities_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to timeaveragedquantities (see VARARGIN)

% Choose default command line output for timeaveragedquantities
handles.output = handles.timeaveragedquantities;

input = find(strcmp(varargin,'results'));
if ~isempty(input)
    results=varargin{input+1};
    handles.results=results;
else
    error(' ');
end

% Update handles structure
guidata(hObject, handles);
Update(handles);

% UIWAIT makes timeaveragedquantities wait for user response (see UIRESUME)
% uiwait(handles.timeaveragedquantities);


% --- Outputs from this function are returned to the command line.
function varargout = timeaveragedquantities_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;
% delete(hObject);


function Update(handles)
set(handles.timeaveragedquantities,'Pointer','watch');
set(handles.list_AveragedQuantities,'Value',1);
set(handles.list_AveragedQuantities,'String','updating...');drawnow;
if get(handles.pup_averagingtime,'Value')==4      % User choice
    set(handles.edit_starttime,'Enable','on');
    set(handles.edit_stoptime,'Enable','on');
    set(handles.pushbutton_set2lasttime,'Enable','on');
    set(handles.text_starttime,'Enable','on');
    set(handles.text_stoptime,'Enable','on');
else
    set(handles.edit_starttime,'Enable','off');
    set(handles.edit_stoptime,'Enable','off');  
    set(handles.pushbutton_set2lasttime,'Enable','off');
    set(handles.text_starttime,'Enable','off');
    set(handles.text_stoptime,'Enable','off');
end
set(handles.text_warning,'Visible','off');
AveragedQuantities=GetAveragedQuantities(handles);
set(handles.list_AveragedQuantities,'String',AveragedQuantities);
set(handles.timeaveragedquantities,'Pointer','arrow');drawnow;

function AveragedQuantities=GetAveragedQuantities(handles)
results=handles.results;
time=results.time;
if length(time)>1
    time=time-time(1);
    nPolePairs=results.nPolePairs;
    if get(handles.pup_averagingtime,'Value')==1       % one electrical period
        n=1;
    elseif get(handles.pup_averagingtime,'Value')==2   % two electrical periods
        n=2;
    elseif get(handles.pup_averagingtime,'Value')==3   % three electrical periods
        n=3;        
    else                                               % User choice
        n=0;
        [stoptime, status]=str2num(get(handles.edit_stoptime,'String'));
        if isempty(stoptime) || ~status || length(stoptime)>1 || ~isreal(stoptime) || stoptime<0 || isnan(stoptime)
            AveragedQuantities='Incorrect averaging time interval';
            return
        end
        if stoptime>time(end)
            stoptime=time(end);
            set(handles.edit_stoptime,'String',num2str(time(end)));
        end
        [starttime, status]=str2num(get(handles.edit_starttime,'String'));
        if isempty(starttime) || ~status || length(starttime)>1 || ~isreal(starttime) || starttime<0 || isnan(starttime) || isinf(starttime) || starttime>=stoptime || starttime>time(end)
            AveragedQuantities='Incorrect averaging time interval';
            return
        end
        if starttime<time(2)
            starttime=time(2);
            set(handles.edit_starttime,'String',num2str(time(2)));
        end
    end
    if n>0
        Speed=results.Speed;   % rad/s
        if any(diff(Speed))      
            % variable speed
            F1=Speed*nPolePairs/(2*pi);
            for i=1:length(time)
                if i==length(time)
                    AveragedQuantities='No enough simulation data for specified averaging time';
                    return
                end
                f1=mean(F1(end-i:end));
                if time(end)-time(end-i)>n/f1
                    starttime=time(end-i);
                    break
                end
            end
            stoptime=time(end);
        else    
            % fixed speed
            f1=Speed(1)*nPolePairs/(2*pi);
            starttime=time(end)-n/f1;
            stoptime=time(end);
            if starttime<0
                AveragedQuantities='No enough simulation data for specified averaging time';
                return
            end
        end
    end
    AveragedQuantities={};
    strwarning={};  
    Id=mean(results.Id(time>=starttime & time<=stoptime));
    Iq=mean(results.Iq(time>=starttime & time<=stoptime));
    Vd=mean(results.Vd(time>=starttime & time<=stoptime));
    Vq=mean(results.Vq(time>=starttime & time<=stoptime));
    RMScurrent=sqrt(Id^2+Iq^2)/sqrt(2);                % phase current
    RMSvoltage=sqrt(Vd^2+Vq^2)/sqrt(2);                % phase voltage
    AveragedQuantities=celladd(AveragedQuantities, ['RMS phase current:         ' num2str(RMScurrent) ' A']);
    AveragedQuantities=celladd(AveragedQuantities, ['RMS phase voltage:         ' num2str(RMSvoltage) ' V']);
    AveragedQuantities=celladd(AveragedQuantities, ['D-axis current:            ' num2str(Id) ' A']);
    AveragedQuantities=celladd(AveragedQuantities, ['Q-axis current:            ' num2str(Iq) ' A']);
    AveragedQuantities=celladd(AveragedQuantities, ['D-axis voltage:            ' num2str(Vd) ' V']);
    AveragedQuantities=celladd(AveragedQuantities, ['Q-axis voltage:            ' num2str(Vq) ' V']); 
    if isfield(results,'motoranalysis')
        % Current density
        motoranalysis=results.motoranalysis;
        motoranalysishandles = guidata(motoranalysis);
        Simulation = motoranalysishandles.Simulation;
        Npp=Simulation.Windings.Npp;
        Schematic=Simulation.Private.CircuitDynFEA.Schematic;
        fillfactor=Simulation.Windings.fillfactor;     % coil fill factor
        if ~isempty(fillfactor)
            Is=ones(Npp,1)*RMScurrent/Npp;   % rms phase current for each parallel path
            nt=size(Simulation.Mesh.t,2);
            jsa=zeros(nt,1); jsb=zeros(nt,1); jsc=zeros(nt,1);
            for nBranch=1:length(Schematic)
                Branch=Schematic{nBranch,1};
                Components=Branch.Components;
                for n=1:length(Components)
                    component=Components{n,1};
                    if strcmp(component.type,'coil')
                        npath=component.value.npath;
                        if strcmp(component.value.phase,'a')
                            jsa=jsa+component.value.I2j*Is(npath);
                        elseif strcmp(component.value.phase,'b')
                            jsb=jsb+component.value.I2j*Is(npath);
                        elseif strcmp(component.value.phase,'c')
                            jsc=jsc+component.value.I2j*Is(npath);
                        end
                    end
                end
            end
            jsa=abs(jsa); jsb=abs(jsb); jsc=abs(jsc);
            CurrentDensity=mean([jsa(jsa>0); jsb(jsb>0); jsc(jsc>0)])/fillfactor;
            AveragedQuantities=celladd(AveragedQuantities, ['RMS current density:       ' num2str(CurrentDensity) ' A/m^2']);
        end
    end
    Gamma=results.Gamma(time>=starttime & time<=stoptime);
    if max(abs(diff(Gamma)))>300    % gamma   0  360
        Gamma_mean1=mean(Gamma(Gamma<=180));
        nmean1=sum(Gamma<=180);
        Gamma_mean2=mean(Gamma(Gamma>180));
        nmean2=sum(Gamma>180);
        Gamma=Gamma_mean1*nmean1/(nmean1+nmean2)+(Gamma_mean2-360)*nmean2/(nmean1+nmean2);
    else
        Gamma=mean(Gamma);
    end
    if Gamma>300
        Gamma=Gamma-360;
    end
    AveragedQuantities=celladd(AveragedQuantities, ['Effective advance angle:   ' num2str(Gamma) ' electrical degrees']); 
    backEMFd=mean(results.BackEMFd(time>=starttime & time<=stoptime));
    backEMFq=mean(results.BackEMFq(time>=starttime & time<=stoptime));
    AveragedQuantities=celladd(AveragedQuantities, ['RMS phase back-EMF:        ' num2str(sqrt(backEMFd^2+backEMFq^2)/sqrt(2)) ' V']); 
    AveragedQuantities=celladd(AveragedQuantities, ['Rotor speed:               ' num2str(mean(results.Speed(time>=starttime & time<=stoptime))*60/(2*pi)) ' RPM']); 
    AveragedQuantities=celladd(AveragedQuantities, ['Supply frequency:          ' num2str(mean(results.Speed(time>=starttime & time<=stoptime))*nPolePairs/(2*pi)) ' Hz']); 
    Torque=results.Torque(time>=starttime & time<=stoptime);
    AveragedQuantities=celladd(AveragedQuantities, ['Total torque:              ' num2str(mean(Torque)) ' N*m']); 
    AveragedQuantities=celladd(AveragedQuantities, ['Reluctance torque:         ' num2str(mean(results.Torque_reluctance(time>=starttime & time<=stoptime))) ' N*m']);     
    AveragedQuantities=celladd(AveragedQuantities, ['Magnet torque:             ' num2str(mean(results.Torque_magnet(time>=starttime & time<=stoptime))) ' N*m']); 
    TorqueRipple=100*abs((max(Torque)-min(Torque))/mean(Torque));
    AveragedQuantities=celladd(AveragedQuantities, ['Torque ripple:             ' num2str(TorqueRipple) ' %']);
    Pinput=mean(results.Pinput(time>=starttime & time<=stoptime));
    Pmech=mean(results.Pmech(time>=starttime & time<=stoptime));
    AveragedQuantities=celladd(AveragedQuantities, ['Input electrical power:    ' num2str(Pinput) ' W']);   
    AveragedQuantities=celladd(AveragedQuantities, ['Output mechanical power:   ' num2str(Pmech) ' W']); 
    Piron_rotor=0; Piron_stator=0; MagnetLoss=0;
    if isfield(results,'Piron')
        if ~isempty(results.Piron.rotor)
            Piron_rotor=results.Piron.rotor;
        end
        if ~isempty(results.Piron.stator)
            Piron_stator=results.Piron.stator;
        end
    end
    if isfield(results,'MagnetLoss')
        MagnetLoss=mean(results.MagnetLoss(time>=starttime & time<=stoptime));
    end
    if Pmech>0
        Efficiency=100*Pmech/(Pinput+Piron_rotor+Piron_stator+MagnetLoss);             % motor mode
    else
        Efficiency=100*(Pinput+Piron_rotor+Piron_stator+MagnetLoss)/Pmech;             % generator mode
    end
    AveragedQuantities=celladd(AveragedQuantities, ['Efficiency:                ' num2str(Efficiency) ' %']);
    PowerFactor=Pinput/(3*RMScurrent*RMSvoltage);
    AveragedQuantities=celladd(AveragedQuantities, ['Power factor:              ' num2str(PowerFactor)]);
    AveragedQuantities=celladd(AveragedQuantities, ['Stator winding loss:       ' num2str(mean(results.Ps(time>=starttime & time<=stoptime))) ' W']);  
    
    Torque1=abs(mean(results.Torque(time>starttime & time<=(stoptime+starttime)/2)));
    Torque2=abs(mean(results.Torque(time>(stoptime+starttime)/2 & time<=stoptime)));
    if abs(2*(Torque1-Torque2)/(Torque1+Torque2))>0.03
        strwarning=celladd(strwarning,'Steady state is not possibly reached. Result may be incorrect.');
    end
    if max(abs(diff(diff(time(time>=starttime & time<=stoptime)))))>eps
        strwarning=celladd(strwarning,'Time step is not constant. Result may be incorrect.');
    end
    if isfield(results,'Piron')     % if dynamic FEA
        AveragedQuantities=celladd(AveragedQuantities, ['Total iron core loss:      ' num2str(Piron_rotor+Piron_stator) ' W']);
        AveragedQuantities=celladd(AveragedQuantities, ['Rotor iron core loss:      ' num2str(Piron_rotor) ' W']);
        AveragedQuantities=celladd(AveragedQuantities, ['Stator iron core loss:     ' num2str(Piron_stator) ' W']);
        Pcons=results.Pcons(time>=starttime & time<=stoptime);
        AveragedQuantities=celladd(AveragedQuantities, ['Eddy current magnet loss:  ' num2str(MagnetLoss) ' W']);
    else
        Pcons=results.Pmech(time>=starttime & time<=stoptime)+results.Ps(time>=starttime & time<=stoptime)+results.Pmf(time>=starttime & time<=stoptime);
    end
    if isfield(results,'DemagH_max')     % if dynamic FEA
        AveragedQuantities=celladd(AveragedQuantities, ['Max. demag. field:         ' num2str(results.DemagH_max) ' A/m']);
        AveragedQuantities=celladd(AveragedQuantities, ['Max. demag. field:         ' num2str(results.DemagHpercent_max) ' % of Hcj']);
    end
    Pinput=results.Pinput(time>=starttime & time<=stoptime);
    Error=100*abs(mean(Pinput-Pcons)/mean(Pinput));
    AveragedQuantities=celladd(AveragedQuantities, ['Discretization error:      ' num2str(Error) ' %']);
    if Error>5
        strwarning=celladd(strwarning,'Discretization error is higher than 5%. Result may be incorrect.');
        strwarning=celladd(strwarning,'Try to rerun simulation with reduced time step.');
    end
    if ~isempty(strwarning)
        set(handles.text_warning,'Visible','on');
        set(handles.text_warning,'String',strwarning);
    else
        set(handles.text_warning,'Visible','off');
    end
else
    AveragedQuantities='No simulation data';
end


% --- Executes on selection change in pup_averagingtime.
function pup_averagingtime_Callback(hObject, eventdata, handles)
% hObject    handle to pup_averagingtime (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Update(handles);


function edittime_Callback(hObject, eventdata, handles)
% hObject    handle to edit_stoptime (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Update(handles);


% --- Executes on button press in pushbutton_set2lasttime.
function pushbutton_set2lasttime_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_set2lasttime (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
results=handles.results;
time=results.time;
if ~isempty(time)
    set(handles.edit_stoptime,'String',num2str(time(end)));
end
Update(handles);


% --- Executes when user attempts to close timeaveragedquantities.
function timeaveragedquantities_CloseRequestFcn(hObject, eventdata, handles)
% hObject    handle to timeaveragedquantities (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
delete(hObject);


% --- Executes on button press in pushbutton_update.
function pushbutton_update_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_update (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Update(handles);


% --------------------------------------------------------------------
function AveragedQuantitiesMenuCopy_Callback(hObject, eventdata, handles)
% hObject    handle to AveragedQuantitiesMenuCopy (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
index_selected = get(handles.list_AveragedQuantities,'Value');
list = get(handles.list_AveragedQuantities,'String');
data=[];
for i=1:length(index_selected)
    line=list{index_selected(i)};
    if strcmp(line(end),'%')
        line=[line '%'];
    end
    data=[data line '\n'];
end
data = sprintf(data); 
clipboard('copy',data);

% --- Executes during object creation, after setting all properties.
function pup_averagingtime_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_averagingtime (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

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
function list_AveragedQuantities_CreateFcn(hObject, eventdata, handles)
% hObject    handle to list_AveragedQuantities (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

"""

def timeaveragedquantities(*args, **kwargs):
    """Placeholder for translated MATLAB function."""
    raise NotImplementedError(
        "This function requires manual translation from MATLAB."
    )
