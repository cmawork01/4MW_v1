function varargout = mesheditor(varargin)
% MESHEDITOR M-file for mesheditor.fig
%      MESHEDITOR, by itself, creates a new MESHEDITOR or raises the existing
%      singleton*.
%
%      H = MESHEDITOR returns the handle to a new MESHEDITOR or the handle to
%      the existing singleton*.
%
%      MESHEDITOR('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in MESHEDITOR.M with the given input arguments.
%
%      MESHEDITOR('Property','Value',...) creates a new MESHEDITOR or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before mesheditor_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to mesheditor_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help mesheditor

% Last Modified by GUIDE v2.5 07-Feb-2018 11:56:41

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @mesheditor_OpeningFcn, ...
                   'gui_OutputFcn',  @mesheditor_OutputFcn, ...
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


% --- Executes just before mesheditor is made visible.
function mesheditor_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to mesheditor (see VARARGIN)

% Choose default command line output for mesheditor
handles.output = hObject;

motoranalysisInput = find(strcmp(varargin, 'motoranalysis'));
if ~isempty(motoranalysisInput)
   handles.motoranalysis = varargin{motoranalysisInput+1};
end
% publish function UpdateMeshEditor
handles.UpdateMeshEditor = @UpdateMeshEditor;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes mesheditor wait for user response (see UIRESUME)
% uiwait(handles.MeshEditor);


% --- Outputs from this function are returned to the command line.
function varargout = mesheditor_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes when user attempts to close MeshEditor.
function MeshEditor_CloseRequestFcn(hObject, eventdata, handles)
% Don't close this figure. It must be deleted from motoranalysis
% Make it invisible then user tries to close it
set(hObject,'Visible','off');
motoranalysishandles = guidata(handles.motoranalysis);
set(motoranalysishandles.menuMeshEditor,'Checked','off');


function editMeshCallback(hObject, eventdata, handles)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Mesh = Simulation.Mesh;
Geometry = Simulation.Geometry;
% editbox Tag
Tag = get(hObject,'Tag');
if strcmp(Tag(1:4),'edit')     % if editbox changed
    % editbox value
    String = get(hObject,'String');
    MeshField = Tag(6:end);
    if isfield(Mesh,MeshField)
        if ~isempty(String)
            [MeshFieldValue, status] = str2num(String);
            ok=0;
            if length(MeshFieldValue)>1
                status=0;
            end
            if status  && isreal(MeshFieldValue) && ~isinf(MeshFieldValue) && ~isnan(MeshFieldValue)
                if MeshFieldValue>0
                    if strcmp(MeshField,'Hgrad')
                        if MeshFieldValue>1 && MeshFieldValue<2
                            Mesh = setfield(Mesh,MeshField,MeshFieldValue);
                            ok=1;
                        end
                    else
                        if rem(MeshFieldValue,1)==0
                            Mesh = setfield(Mesh,MeshField,MeshFieldValue);
                            ok=1;
                        end
                    end
                end                
            end
            if ~ok
                if strcmp(MeshField,'nPolePairs')
                    errordlg('Enter an appropriate number of periodicity factor or leave this field empty','Mesh Editor Error','modal');
                else
                    errordlg('Not a valid value','Mesh Editor Error','modal');
                end
                editbox=['edit_' MeshField];
                set(getfield(handles,editbox),'String',num2str(getfield(Mesh,MeshField)));
                return
            end
        else
            Mesh = setfield(Mesh,MeshField,[]);
        end
    end
% elseif strcmp(Tag(1:8),'checkbox')     % if checkbox changed
%     Value = get(hObject,'Value');
%     MeshField = Tag(10:end);
%     if isfield(Mesh,MeshField)
%         if Value
%             Mesh = setfield(Mesh,MeshField,1);
%         else
%             Mesh = setfield(Mesh,MeshField,0);
%         end    
%     end
elseif strcmp(Tag(1:3),'pup')     % if popupmenu changed
    % popupmenu value
    index = get(hObject,'Value');
    strlist = get(hObject,'String');
    String = strlist(index);
    MeshField = Tag(5:end);
    if isfield(Mesh,MeshField)
        if ~isempty(String)
            if strcmp(MeshField,'perbndcnd')
                nPolePairs = Mesh.nPolePairs;
                Ns = Geometry.Ns;
                [nper periodicity] = VerifyPerBndCnd(Ns,nPolePairs,String);
                if isempty(nper)
                    ok=0;
                else
                    ok=1;
                end
                if ok
                    Mesh = setfield(Mesh,MeshField,String);
                    index=get(hObject,'Value');
                    set(hObject,'UserData',index);
                else
                    previndex = get(hObject,'UserData');   % previous index
                    set(hObject,'Value',previndex);        % select a previous menu item
                end
            elseif strcmp(MeshField,'nAirGapLayers')
                Mesh = setfield(Mesh,MeshField,str2num(String{1}));
            else
                Mesh = setfield(Mesh,MeshField,String);    
            end
        else
            error('String is empty');
        end
    end
end
Simulation.Mesh = Mesh;
motoranalysishandles.Simulation = Simulation;
motoranalysishandles.Saved = 0;
guidata(handles.motoranalysis,motoranalysishandles);


function UpdateMeshEditor(hObject)
handles = guidata(hObject);
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Mesh = Simulation.Mesh;
% update editbox values
MeshFields = fieldnames(Mesh);
for i=1:length(MeshFields)
    MeshField = MeshFields{i};
    editbox = ['edit_' MeshField];
    if isfield(handles,editbox)        % if editbox
        MeshFieldValue = getfield(Mesh,MeshField);
        set(getfield(handles,editbox),'String',num2str(MeshFieldValue,10));
    end
    checkbox = ['checkbox_' MeshField];
    if isfield(handles,checkbox)       % if checkbox
        MeshFieldValue = getfield(Mesh,MeshField);
        if MeshFieldValue
            set(getfield(handles,checkbox),'Value',1);
        else
            set(getfield(handles,checkbox),'Value',0);
        end
    end
    popup = ['pup_' MeshField];
    if isfield(handles,popup)          % if popup menu
        MeshFieldValue = getfield(Mesh,MeshField);
        if strcmp(MeshField,'nAirGapLayers')
            MeshFieldValue=num2str(MeshFieldValue);
        end
        strlist = get(getfield(handles,popup),'String');
        for n=1:length(strlist)
            if strcmp(MeshFieldValue,strlist(n))
                break;
            elseif n==length(strlist)
                error(['Inappropriate value for <' MeshField '>: something goes wrong']);
            end
        end
        set(getfield(handles,popup),'Value',n);
        set(getfield(handles,popup),'UserData',n);        % store item index in UserData
    end
end
setoutputs(handles);
EnableMeshEditor(handles);
drawmesh(handles);
guidata(hObject, handles);

function setoutputs(handles)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Mesh = Simulation.Mesh;
Geometry = Simulation.Geometry;
Windings = Simulation.Windings;
Materials = Simulation.Materials;
p = Mesh.p; t = Mesh.t; e = Mesh.e;
Ns = Geometry.Ns;
l = Geometry.l/1000; 
nper = VerifyPerBndCnd(Ns,Mesh.nPolePairs,Mesh.perbndcnd);
DXFrotor = Simulation.DXFrotor;
DXFstator = Simulation.DXFstator;
dxfstator=Geometry.dxfstator;
if isempty(Windings.layout)
    Subdomains=[];
else
    try
        Subdomains=GetSubdomains(Geometry,DXFrotor,DXFstator,Windings,Materials,nper,dxfstator);
    catch
        Subdomains=[];
    end
end
if ~isempty(p) && ~isempty(t) && ~isempty(e) && ~isempty(Subdomains)
    it_magnet=[];
    itss=[];
    it_rotorcore=[];
    it_statorcore=[];
    for j=1:length(Subdomains)
        subdomain=Subdomains(j);
        if strcmp(subdomain.position,'rotor')
            if strcmp(subdomain.type,'magnet')
                it_magnet=[it_magnet find(t(4,:)==j)];
            elseif strcmp(subdomain.type,'core')
                it_rotorcore=[it_rotorcore find(t(4,:)==j)];
            end
        elseif strcmp(subdomain.position,'stator')
            if strcmp(subdomain.type,'winding')
                itss=[itss find(t(4,:)==j)];
            elseif strcmp(subdomain.type,'core')
                it_statorcore=[it_statorcore find(t(4,:)==j)];
            end
        end
    end
    np=size(p,2);
    nt=size(t,2);
    ar=trgdata(p,t);
    Sss=sum(ar(itss))/(Ns/nper)*10^6;
    Sls=sum(ar(it_statorcore))*nper*10^6;
    Slr=sum(ar(it_rotorcore))*nper*10^6;
    Smagnet=sum(ar(it_magnet))*nper;
    set(handles.edit_np,'String',num2str(np));
    set(handles.edit_nt,'String',num2str(nt));
    set(handles.edit_Sss,'String',num2str(Sss,7));
    set(handles.edit_Sls,'String',num2str(Sls,7));
    set(handles.edit_Slr,'String',num2str(Slr,7));
    % Stator iron weight
    StatorIronWeight=[];
    statorironmaterial=Materials.statorironmaterial;
    k_st_stator=Materials.k_st_stator;
    if strcmp(statorironmaterial,'Not assigned')
        set(handles.edit_StatorIronWeight,'String','');
    else
        MassDensity=ReadMaterialData('Iron',statorironmaterial,'<Mass Density>');
        StatorIronWeight=MassDensity*k_st_stator*l*Sls/10^6;
        set(handles.edit_StatorIronWeight,'String',num2str(StatorIronWeight,7));
    end
    % Rotor iron weight
    RotorIronWeight=[];
    rotorironmaterial=Materials.rotorironmaterial;
    k_st_rotor=Materials.k_st_rotor;
    if strcmp(rotorironmaterial,'Not assigned')
        set(handles.edit_RotorIronWeight,'String','');
    else
        MassDensity=ReadMaterialData('Iron',rotorironmaterial,'<Mass Density>');
        RotorIronWeight=MassDensity*k_st_rotor*l*Slr/10^6;
        set(handles.edit_RotorIronWeight,'String',num2str(RotorIronWeight,7));
    end
    % Magnet weight
    MagnetWeight=[];
    magnetmaterial=Materials.magnetmaterial;
    if strcmp(magnetmaterial,'Not assigned')
        set(handles.edit_MagnetWeight,'String','');
    else
        MassDensity=ReadMaterialData('Magnet',magnetmaterial,'<Mass Density>');
        MagnetWeight=MassDensity*l*Smagnet;
        set(handles.edit_MagnetWeight,'String',num2str(MagnetWeight,7));
    end
    % Winding weight
    WindingWeight=[];
    statorwindingmaterial=Materials.statorwindingmaterial;
    if strcmp(statorwindingmaterial,'Not assigned')
        set(handles.edit_WindingWeight,'String','');
        set(handles.edit_WireLength,'String','');
    else
        MassDensity=ReadMaterialData('Conductor',statorwindingmaterial,'<Mass Density>');
        WindingEditor=motoranalysishandles.WindingEditor;
        WindingEditorHandles = guidata(WindingEditor);
        layout1=Windings.layout.layout1;
        layout2=Windings.layout.layout2;
        layout3=Windings.layout.layout3;
        D2s=Geometry.D2s/1000; Sds=Geometry.Sds/1000; slotlayertype=Geometry.slotlayertype;
        Hsew=Windings.Hsew/1000; W=Windings.W; fillfactor=Windings.fillfactor; ks=Windings.ks; Npp=Windings.Npp;
        try
            [~,~,WireLength]=WindingEditorHandles.GetStatorWinding(Geometry,Mesh,Windings,layout1,layout2,layout3,Ns,D2s,Sds,Hsew,W,slotlayertype,ks,fillfactor,Npp,l,0);
            set(handles.edit_WireLength,'String',num2str(WireLength,7));
            wirediameter=Windings.wirediameter/1000;   
            wirearea=Windings.nstrands*pi*(wirediameter/2)^2;
            if ~isempty(Windings.fillfactor) && ~isempty(WireLength)
                WindingWeight=MassDensity*wirearea*WireLength;
                set(handles.edit_WindingWeight,'String',num2str(WindingWeight,7));
            end
        catch
            set(handles.edit_WindingWeight,'String','');
            set(handles.edit_WireLength,'String','');
        end
    end
    TotalWeight=MagnetWeight+WindingWeight+RotorIronWeight+StatorIronWeight;
    set(handles.edit_TotalWeight,'String',num2str(TotalWeight,7));
else
    set(handles.edit_np,'String','');
    set(handles.edit_nt,'String','');
    set(handles.edit_Sss,'String','');
    set(handles.edit_Sls,'String','');
    set(handles.edit_Slr,'String','');
    set(handles.edit_StatorIronWeight,'String','');
    set(handles.edit_RotorIronWeight,'String','');
    set(handles.edit_MagnetWeight,'String','');
    set(handles.edit_WindingWeight,'String','');
    set(handles.edit_WireLength,'String','');
    set(handles.edit_TotalWeight,'String','');
end

function drawmesh(handles)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Mesh = Simulation.Mesh;
p = Mesh.p; t = Mesh.t; e = Mesh.e;
if ~isempty(p) && ~isempty(t) && ~isempty(e)
    try
        Visible = get(handles.MeshEditor,'Visible');
        if strcmp(Visible,'on')
            newplot(handles.axes_mesheditor);
            axes(handles.axes_mesheditor);
            fieldplot(p,e,t,'contour','on','mesh','on');axis equal;
%             xlimits=xlim;
%             if xlimits(1)+xlimits(2)>eps
%                 xlim([0 xlimits(2)+abs(xlimits(1))]);
%             end
        end
    catch
        % no preview available
        Visible = get(handles.MeshEditor,'Visible');
        if strcmp(Visible,'on')
            newplot(handles.axes_mesheditor);
            axes(handles.axes_mesheditor);
            hold on
            ylim([-10 10]);
            text(0,0,'No mesh generated','FontSize',18,'HorizontalAlignment','center');
            axis equal
            hold off
        end
    end
else
    % no preview available
    Visible = get(handles.MeshEditor,'Visible');
    if strcmp(Visible,'on')
        newplot(handles.axes_mesheditor);
        axes(handles.axes_mesheditor);
        hold on
        ylim([-10 10]);
        text(0,0,'No mesh generated','FontSize',18,'HorizontalAlignment','center');
        axis equal
        hold off
    end
end

% --- Executes on button press in pushbutton_generatemesh.
function pushbutton_generatemesh_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_generatemesh (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Visible = get(handles.MeshEditor,'Visible');
if strcmp(Visible,'on')
    newplot(handles.axes_mesheditor);
    axes(handles.axes_mesheditor);
    hold on
    ylim([-10 10]);
    text(0,0,'Please wait...','FontSize',18,'HorizontalAlignment','center');
    axis equal
    hold off
    drawnow;
end
try
    set(handles.MeshEditor,'Pointer','watch');drawnow;
    motoranalysishandles = guidata(handles.motoranalysis);
    Simulation = motoranalysishandles.Simulation;
    Mesh = Simulation.Mesh;
    Geometry = Simulation.Geometry; 
    DXFrotor = Simulation.DXFrotor;
    DXFstator = Simulation.DXFstator;
    dxfstator=Geometry.dxfstator;
    if isfield(DXFrotor,'geometry')
        RotorGeometry = DXFrotor.geometry;
    else
        RotorGeometry = [];
        errordlg('No rotor geometry found','Mesh Editor Error','modal');
    end
    StatorGeometry = [];
    if isfield(DXFstator,'geometry')
        StatorGeometry = DXFstator.geometry;
    else
        if dxfstator
            errordlg('No stator geometry found','Mesh Editor Error','modal');
        end
    end
    Windings = Simulation.Windings; 
    nAirGapLayers = Mesh.nAirGapLayers; 
    AirGapSlidingLayer = round(nAirGapLayers/2);
    Hgrad = Mesh.Hgrad;
    agmeshqlt = Mesh.agmeshqlt;
    Ns=Geometry.Ns;
    dxfstator=Geometry.dxfstator;
    nPolePairs = Mesh.nPolePairs;
    perbndcnd = Mesh.perbndcnd;
    [geom, ~, ~, lag]=initgeom(Geometry,RotorGeometry,StatorGeometry,Mesh,[],dxfstator);
    [nper periodicity] = VerifyPerBndCnd(Ns,nPolePairs,perbndcnd);
    if isempty(nper) || isempty(RotorGeometry) || (dxfstator && isempty(StatorGeometry))
        newplot(handles.axes_mesheditor);
        axes(handles.axes_mesheditor);
        hold on
        ylim([-10 10]);
        text(0,0,'No mesh generated','FontSize',18,'HorizontalAlignment','center');
        axis equal
        hold off
        set(handles.MeshEditor,'Pointer','arrow');drawnow;
        return; 
    end
    dxfstator=Geometry.dxfstator;
    [p,e,t]=createmesh(geom,Geometry,lag,nAirGapLayers,agmeshqlt,Hgrad);
    nSlotLayers=1;
    if strcmp(Geometry.slotlayertype,'Double layer')
        nSlotLayers=2;
    end
    [p,t,e,b,Rotate]=replicatemesh(p,e,t,Geometry,lag,nAirGapLayers,AirGapSlidingLayer,nSlotLayers,nper,periodicity,dxfstator,DXFstator);
    % figure; pdeplot(p,e,t,'contour','on','mesh','on');axis equal;
    Mesh.p = p;
    Mesh.t = t;
    Mesh.e = e;
    Mesh.b = b;    
    Mesh.Rotate = Rotate;
    Simulation.Mesh = Mesh;
    motoranalysishandles.Simulation = Simulation;
    motoranalysishandles.Saved = 0;
    guidata(handles.motoranalysis,motoranalysishandles);
    UpdateMeshEditor(handles.MeshEditor);
    set(handles.MeshEditor,'Pointer','arrow');drawnow;
catch
    set(handles.MeshEditor,'Pointer','arrow');drawnow;
    newplot(handles.axes_mesheditor);
    axes(handles.axes_mesheditor);
    hold on
    ylim([-10 10]);
    text(0,0,'Error while trying to generate mesh...','FontSize',18,'HorizontalAlignment','center');
    axis equal
    hold off
    pause(1);
end

function EnableMeshEditor(handles)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
if isempty(Simulation.Private)
    enable = 'on';
else
    enable = 'off';
end
set(handles.pup_nAirGapLayers,'Enable',enable);
set(handles.edit_Hgrad,'Enable',enable);
set(handles.pup_agmeshqlt,'Enable',enable);
set(handles.edit_nSlices,'Enable',enable);
set(handles.pushbutton_generatemesh,'Enable',enable);
set(handles.edit_nPolePairs,'Enable',enable);
set(handles.pup_perbndcnd,'Enable',enable);

% --- Executes during object creation, after setting all properties.
function pup_nAirGapLayers_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_nAirGapLayers (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Hgrad_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Hgrad (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_np_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_np (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_nt_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_nt (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Sss_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Sss (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Sls_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Sls (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Slr_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Slr (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function pup_agmeshqlt_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_agmeshqlt (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_nSlices_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_nSlices (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --------------------------------------------------------------------
function plot_MeshEditor_Callback(hObject, eventdata, handles)
% hObject    handle to plot_MeshEditor (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function plot_newwnd_Callback(hObject, eventdata, handles)
% hObject    handle to plot_newwnd (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Displays contents of axes_mesheditor in a new figure

Title = 'Mesh';
% Create a figure to receive this axes' data
axes1fig = figure('Name',Title);
% Copy the axes and size it to the figure
axes1copy = copyobj(handles.axes_mesheditor,axes1fig);
set(axes1copy,'Units','Normalized',...
              'Position',[0,0.05,1,0.9]);


% --- Executes during object creation, after setting all properties.
function pup_perbndcnd_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_perbndcnd (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_nPolePairs_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_nPolePairs (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_StatorIronWeight_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_StatorIronWeight (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_RotorIronWeight_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_RotorIronWeight (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_WindingWeight_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_WindingWeight (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_MagnetWeight_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_MagnetWeight (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_TotalWeight_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_TotalWeight (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_WireLength_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_WireLength (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
