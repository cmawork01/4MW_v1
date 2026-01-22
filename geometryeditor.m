function varargout = geometryeditor(varargin)
%GEOMETRYEDITOR M-file for GeometryEditor.fig
%      GEOMETRYEDITOR, by itself, creates a new GEOMETRYEDITOR or raises the existing
%      singleton*.
%
%      H = GEOMETRYEDITOR returns the handle to a new GEOMETRYEDITOR or the handle to
%      the existing singleton*.
%
%      GEOMETRYEDITOR('Property','Value',...) creates a new GEOMETRYEDITOR using the
%      given property value pairs. Unrecognized properties are passed via
%      varargin to GeometryEditor_OpeningFcn.  This calling syntax produces a
%      warning when there is an existing singleton*.
%
%      GEOMETRYEDITOR('CALLBACK') and GEOMETRYEDITOR('CALLBACK',hObject,...) call the
%      local function named CALLBACK in GEOMETRYEDITOR.M with the given input
%      arguments.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help GeometryEditor

% Last Modified by GUIDE v2.5 13-Sep-2017 19:35:32

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @GeometryEditor_OpeningFcn, ...
                   'gui_OutputFcn',  @GeometryEditor_OutputFcn, ...
                   'gui_LayoutFcn',  [], ...
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


% --- Executes just before GeometryEditor is made visible.
function GeometryEditor_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   unrecognized PropertyName/PropertyValue pairs from the
%            command line (see VARARGIN)

% Choose default command line output for GeometryEditor
handles.output = hObject;

motoranalysisInput = find(strcmp(varargin, 'motoranalysis'));
if ~isempty(motoranalysisInput)
   handles.motoranalysis = varargin{motoranalysisInput+1};
end
% publish function UpdateGeometryEditor
handles.UpdateGeometryEditor = @UpdateGeometryEditor;

% Update handles structure
guidata(hObject, handles);


% --- Outputs from this function are returned to the command line.
function varargout = GeometryEditor_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes when user attempts to close GeometryEditor.
function GeometryEditor_CloseRequestFcn(hObject, eventdata, handles)
% Don't close this figure. It must be deleted from motoranalysis
% Make it invisible when user tries to close it
set(hObject,'Visible','off');
motoranalysishandles = guidata(handles.motoranalysis);
set(motoranalysishandles.menuGeometryEditor,'Checked','off');


function editGeometryCallback(hObject, eventdata, handles)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Geometry = Simulation.Geometry;
UpdateWindingEditor=0;
% editbox | popupmenu | checkbox Tag
Tag = get(hObject,'Tag');
if strcmp(Tag(1:4),'edit')     % if editbox changed
    % editbox value
    String = get(hObject,'String');
    GeometryField = Tag(6:end);
    if isfield(Geometry,GeometryField)
        if ~isempty(String)
            [GeometryFieldValue, status] = str2num(String);
            if length(GeometryFieldValue)>1 || (strcmp(GeometryField,'D1s') && GeometryFieldValue==0) || (strcmp(GeometryField,'D2s') && GeometryFieldValue==0)
                status=0;
            end
            if status && isreal(GeometryFieldValue) && ~isinf(GeometryFieldValue) && ~isnan(GeometryFieldValue)
                Geometry = setfield(Geometry,GeometryField,GeometryFieldValue);
                 % update WindingEditor if number of stator slots or slot dimensions are changed
                if strcmp(GeometryField,'Ns') || strcmp(GeometryField,'Ods') || strcmp(GeometryField,'Ows') || strcmp(GeometryField,'Tas') || strcmp(GeometryField,'Sds') || ...
                   strcmp(GeometryField,'Rcs') || strcmp(GeometryField,'Ws') || strcmp(GeometryField,'Rcs_ag')  
                    UpdateWindingEditor=1;
                end 
                if (strcmp(GeometryField,'D2s') && strcmp(Geometry.motortype,'Inner rotor')) || (strcmp(GeometryField,'D1s') && strcmp(Geometry.motortype,'Outer rotor'))
                    if ~Geometry.dxfstator
                        if ~isempty(Simulation.DXFrotor)
                            DXFRotorGeometry = Simulation.DXFrotor.geometry;
                            [~, ~, ~, lag]=initgeom(Geometry,DXFRotorGeometry,[],Simulation.Mesh,[],Geometry.dxfstator);
                            Geometry.lag = 1000*lag;
                        end
                    end
                end
            else
                errordlg('Not a valid value','Geometry Editor Error','modal');
                editbox=['edit_' GeometryField];
                set(getfield(handles,editbox),'String','');
                return
            end
        else
            Geometry = setfield(Geometry,GeometryField,[]);
        end
    end
elseif strcmp(Tag(1:3),'pup')     % if popupmenu changed
    % popupmenu value
    index = get(hObject,'Value');
    strlist = get(hObject,'String');
    String = strlist(index);
    
    GeometryField = Tag(5:end);
    if isfield(Geometry,GeometryField)
        if ~isempty(String)
            if strcmp(String,'User defined')  % is not supported!!!
                msgbox('User defined slot geometry is not supported in this version','Message','modal');
                previndex = get(hObject,'UserData');   % previous index
                set(hObject,'Value',previndex);        % select a previous menu item
                return
            else
                Geometry = setfield(Geometry,GeometryField,String);
                index=get(hObject,'Value');
                set(hObject,'UserData',index);
                % update WindingEditor if number of stator slot layers or slot dimensions are changed
                if strcmp(GeometryField,'slotlayertype') || strcmp(GeometryField,'motortype') || strcmp(GeometryField,'statorslottype') || strcmp(GeometryField,'layerpos') || ...
                   strcmp(GeometryField,'statorslotcornertype') 
                    UpdateWindingEditor=1;
                end
            end
        else
            error('String is empty');
        end
    end   
elseif strcmp(Tag(1:8),'checkbox')     % if checkbox changed
    Value = get(hObject,'Value');
    GeometryField = Tag(10:end);
    if isfield(Geometry,GeometryField)
        if strcmp(GeometryField,'dxfstator')
            if Value==0    % if template-based stator geometry is chosen
                if ~isempty(Simulation.DXFstator)   % if dxf stator geometry was previously imported
                    button = questdlg('Stator geometry previously imported from dxf-file will be deleted. Continue?',...
                        'Geometry Editor','Yes','No','No');
                    if strcmp(button,'No')
                        Value=1;
                    else
                        Simulation.DXFstator=[];
                    end
                end
            else
                % if stator from dxf file is chosen
                Simulation.Windings.Lsew_inputmethod='Manual';
                Simulation.Windings.Rs_inputmethod='Manual';
            end
        end
        if Value
            Geometry = setfield(Geometry,GeometryField,1);
        else
            Geometry = setfield(Geometry,GeometryField,0);
        end
    end
end
Simulation.Geometry = Geometry;
motoranalysishandles.Simulation = Simulation;
motoranalysishandles.Saved = 0;
guidata(handles.motoranalysis,motoranalysishandles);

if UpdateWindingEditor
    WindingEditor=motoranalysishandles.WindingEditor;
    WindingEditorHandles = guidata(WindingEditor);
    WindingEditorHandles.UpdateWindingEditor(WindingEditor,0,0);
end

Update(motoranalysishandles.GeometryEditor);

function Update(hObject)
handles = guidata(hObject);

motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
% timestep = Simulation.Settings.Transient.timestep;
% CurrentTime = Simulation.Outputs.CurrentTime;
if isempty(Simulation.Private) % && CurrentTime<timestep
     enable = 'on';
     EnableGeometryEditor(handles,enable);
else
    enable = 'off';
end
Geometry = Simulation.Geometry;
% update editbox and popup menu values
GeometryFields = fieldnames(Geometry);
for i=1:length(GeometryFields)
    GeometryField = GeometryFields{i};
    editbox = ['edit_' GeometryField];
    if isfield(handles,editbox)           % if editbox
        GeometryFieldValue = getfield(Geometry,GeometryField);
        set(getfield(handles,editbox),'String',num2str(GeometryFieldValue,10));
    end
    popup = ['pup_' GeometryField];
    if isfield(handles,popup)           % if popup menu
        GeometryFieldValue = getfield(Geometry,GeometryField);
        strlist = get(getfield(handles,popup),'String');
        for n=1:length(strlist)
            if strcmp(GeometryFieldValue,strlist(n))
                break;
            elseif n==length(strlist)
                error(['Inappropriate value for <' GeometryField '>: something goes wrong']);
                return;
            end
        end
        set(getfield(handles,popup),'Value',n);
        set(getfield(handles,popup),'UserData',n);        % store item index in UserData
        
        if strcmp(GeometryField,'statorslottype')
            if strcmp(GeometryFieldValue,'Parallel tooth')
                set(getfield(handles,'text_Ws'),'String','Tooth width (Ws):');
            elseif strcmp(GeometryFieldValue,'Parallel slot')
                set(getfield(handles,'text_Ws'),'String','Slot width (Ws):');
            end
        end
        if strcmp(GeometryField,'statorslotcornertype')
            if strcmp(GeometryFieldValue,'Round')
                set(getfield(handles,'edit_Rcs'),'Enable','off');
                set(getfield(handles,'text_Rcs'),'Enable','off');
                set(getfield(handles,'text_Rcs_units'),'Enable','off');
            else
                set(getfield(handles,'edit_Rcs'),'Enable',enable);
                set(getfield(handles,'text_Rcs'),'Enable','on');  
                set(getfield(handles,'text_Rcs_units'),'Enable','on'); 
            end
        end        
        
    end
    checkbox = ['checkbox_' GeometryField];
    if isfield(handles,checkbox)        % if checkbox
        GeometryFieldValue = getfield(Geometry,GeometryField);
        set(getfield(handles,checkbox),'Value',GeometryFieldValue);
        if strcmp(GeometryField,'dxfstator')
            if GeometryFieldValue   % if stator is imported from dxf
                enable = 'off';     % disable stator geometry template fields
                set(handles.dxfstatorimport,'Enable','on');
            else
                enable = 'on';
                set(handles.dxfstatorimport,'Enable','off');
            end
            ItemList=findobj(get(handles.GeometryEditor,'Children'));
            for n=1:length(ItemList)
                Tag = get(ItemList(n),'Tag');
                if length(Tag)>2
                    if strcmp(Tag(1:3),'pup') || strcmp(Tag(1:4),'edit')
                        if strcmp(Tag,'pup_preview') || strcmp(Tag,'edit_l') || strcmp(Tag,'edit_rotorskew') || strcmp(Tag,'edit_statorskew') || strcmp(Tag,'pup_motortype')
                            % no action
                        else
                            if strcmp(Tag,'edit_Rcs') && strcmp(enable,'on')
                                % no action
                            else
                                set(ItemList(n),'Enable',enable);
                            end
                        end
                    end
                end
            end
        end
    end
end
if strcmp(Geometry.slotlayertype,'Single layer')
    set(handles.pup_layerpos,'Visible','off');
    set(handles.text_layerpos,'Visible','off');
else
    set(handles.pup_layerpos,'Visible','on');
    set(handles.text_layerpos,'Visible','on');
end
if ~isempty(Simulation.Private) % && CurrentTime<timestep
     enable = 'off';
     EnableGeometryEditor(handles,enable);
end
guidata(hObject, handles);

function UpdateGeometryEditor(hObject)
Update(hObject);
handles = guidata(hObject);
redrawgeometry(handles);


% --------------------------------------------------------------------
function dxfrotorimport_Callback(hObject, eventdata, handles)
% hObject    handle to dxfrotorimport (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
[~,maxArraySize]=computer; 
is64bit=maxArraySize>2^31;
set(handles.GeometryEditor,'Pointer','watch');drawnow;
if is64bit
    if isdeployed
        [notfound, warninigs] = loadlibrary('MDR_64.dll', @MDRprotofile);
    else
        [notfound, warninigs] = loadlibrary('MDR_64.dll', 'MDR.h');
    end
    [geometry, materials, properties, ~] = calllib('MDR_64', 'execute', '');
    unloadlibrary('MDR_64');
else
    if isdeployed
        [notfound, warninigs] = loadlibrary('MDR.dll', @MDRprotofile);
    else
        [notfound, warninigs] = loadlibrary('MDR.dll', 'MDR.h');
    end
    [geometry, materials, properties, ~] = calllib('MDR', 'execute', '');
    unloadlibrary('MDR');
end
set(handles.GeometryEditor,'Pointer','arrow');drawnow;
if ~isempty(geometry)
    geometry=normsdm(geometry);
    motoranalysishandles = guidata(handles.motoranalysis);
    MeshEditorHandles = guidata(motoranalysishandles.MeshEditor);
    Simulation = motoranalysishandles.Simulation;
    Mesh = Simulation.Mesh;
    Geometry = Simulation.Geometry;
    DXFstator = Simulation.DXFstator;
    if isfield(DXFstator,'geometry')
        DXFStatorGeometry = DXFstator.geometry;
    else
        DXFStatorGeometry = [];
    end
    geometry(abs(geometry)<10^-12)=0;
    try
        [~, ~, nPolePairs, lag, isfullrotor]=initgeom(Simulation.Geometry,geometry,DXFStatorGeometry,Mesh,[],Geometry.dxfstator);
    catch ME
        if ~strcmp(ME.message,'initgeom error')
            errordlg({'Failed to import rotor geometry. The possible reason:';
                     '- stator geometry is incomplete or incorrect';
                     '- rotor geometry is not correct'},'Geometry Editor Error','modal');
        end
        return
    end
    if isfullrotor
        errordlg('Whole rotor geometry cannot be imported. Use division factor to select one half of pole pitch!','Geometry Editor Error','modal');
        return
    end
    DXFrotor.geometry = geometry;
    DXFrotor.materials = materials;
    DXFrotor.properties = properties;
    DXFrotor.nPolePairs = nPolePairs;
    if ~isempty(nPolePairs)
        Mesh.nPolePairs = nPolePairs;
        Ns=Geometry.Ns;
        if ~isempty(Ns)
            if rem(Ns,2*nPolePairs)==0
                Mesh.perbndcnd = 'Antiperiodic';
            elseif rem(Ns,nPolePairs)==0
                Mesh.perbndcnd = 'Periodic';
            else
                Mesh.perbndcnd = 'None';
            end
        else
            Mesh.perbndcnd = 'None';
        end
    end
    Mesh.p=[]; Mesh.t=[]; Mesh.e=[]; Mesh.b=[]; Mesh.Rotate=[];    % delete mesh
    if ~isempty(lag)
        Geometry.lag = 1000*lag;
    end
    Simulation.DXFrotor = DXFrotor;
    Simulation.Mesh = Mesh;
    Simulation.Geometry = Geometry;
    motoranalysishandles.Simulation = Simulation;
    motoranalysishandles.Saved = 0;
    guidata(handles.motoranalysis,motoranalysishandles);
    MeshEditorHandles.UpdateMeshEditor(motoranalysishandles.MeshEditor);
end
redrawgeometry(handles);


% --------------------------------------------------------------------
function dxfstatorimport_Callback(hObject, eventdata, handles)
% hObject    handle to dxfstatorimport (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
[~,maxArraySize]=computer; 
is64bit=maxArraySize>2^31;
if is64bit
    if isdeployed
        [notfound, warninigs] = loadlibrary('MDR_64.dll', @MDRprotofile);
    else
        [notfound, warninigs] = loadlibrary('MDR_64.dll', 'MDR.h');
    end
    [geometry, materials, properties, doublenlayers] = calllib('MDR_64', 'execute', '');
    unloadlibrary('MDR_64');
else
    if isdeployed
        [notfound, warninigs] = loadlibrary('MDR.dll', @MDRprotofile);
    else
        [notfound, warninigs] = loadlibrary('MDR.dll', 'MDR.h');
    end
    [geometry, materials, properties, doublenlayers] = calllib('MDR', 'execute', '');
    unloadlibrary('MDR');
end
if ~isempty(geometry)
    geometry=normsdm(geometry);
    motoranalysishandles = guidata(handles.motoranalysis);
    Simulation = motoranalysishandles.Simulation;
    Mesh = Simulation.Mesh;
    Geometry = Simulation.Geometry;
    Windings = Simulation.Windings;
    DXFrotor = Simulation.DXFrotor;
    if isfield(DXFrotor,'geometry')
        DXFRotorGeometry = DXFrotor.geometry;
    else
        DXFRotorGeometry = [];
    end
    geometry(abs(geometry)<10^-12)=0;
    [~, ~, nPolePairs, lag, ~, isstatorcorrect,Ns,Rs_inner,Rs_outer]=initgeom(Geometry,DXFRotorGeometry,geometry,Mesh,[],Geometry.dxfstator);
    if ~isstatorcorrect
        errordlg('Stator geometry you are trying to import is not correct!','Geometry Editor Error','modal');
        return
    end
    if isfield(DXFrotor,'nPolePairs')
        if ~isempty(nPolePairs)
            if isempty(Simulation.DXFrotor.nPolePairs)
                Simulation.DXFrotor.nPolePairs = nPolePairs;
                Mesh.nPolePairs = nPolePairs;
                if ~isempty(Ns)
                    if rem(Ns,2*nPolePairs)==0
                        Mesh.perbndcnd = 'Antiperiodic';
                    elseif rem(Ns,nPolePairs)==0
                        Mesh.perbndcnd = 'Periodic';
                    else
                        Mesh.perbndcnd = 'None';
                    end
                else
                    Mesh.perbndcnd = 'None';
                end
            end
        end
    end
    nSlotLayers=0;
    layerlist=[];
    for n=1:length(properties)
        ilayer=properties(n).layer;
        nSlotLayers=max([nSlotLayers ilayer]);
        layerlist=[layerlist ilayer];
    end
    layerlist=sort(layerlist);
    for i=1:nSlotLayers
        ind=find(layerlist==i);
        if isempty(ind)
            errordlg(['Winding layer number ' num2str(i) ' is missing'],'Geometry Editor Error','modal');
            return
        elseif length(ind)>1
            errordlg('Several subdomains with the same winding layer number are not allowed','Geometry Editor Error','modal');
            return
        end
    end
    Geometry.Ns=Ns;
    DXFstator.geometry = geometry;
    DXFstator.materials = materials;
    DXFstator.properties = properties;
    DXFstator.doublenlayers = doublenlayers;
    if doublenlayers    % if doublenlayers=1 - vertical slot divider
        nSlotLayers=nSlotLayers*2;
        Geometry.layerpos='Left/Right';
    else
        Geometry.layerpos='Upper/Lower';
    end
    if nSlotLayers>2
        Windings.layoutmethod='From file';
    elseif nSlotLayers==1
        Geometry.slotlayertype='Single layer';
    elseif nSlotLayers==2   
        Geometry.slotlayertype='Double layer';
    else
        error(' ');
    end
    Mesh.p=[]; Mesh.t=[]; Mesh.e=[]; Mesh.b=[]; Mesh.Rotate=[];    % delete mesh
    if ~isempty(lag)
        Geometry.lag = 1000*lag;
    end
    if ~isempty(Rs_inner)
        Geometry.D2s = Rs_inner*2*1000;
    end
    if ~isempty(Rs_outer)
        Geometry.D1s = Rs_outer*2*1000;
    end
    Simulation.DXFstator = DXFstator;
    Simulation.Geometry = Geometry;
    Simulation.Windings = Windings;
    Simulation.Mesh = Mesh;
    motoranalysishandles.Simulation = Simulation;
    motoranalysishandles.Saved = 0;
    guidata(handles.motoranalysis,motoranalysishandles);
    WindingEditor=motoranalysishandles.WindingEditor;
    WindingEditorHandles = guidata(WindingEditor);
    WindingEditorHandles.UpdateWindingEditor(WindingEditor,0,0);
end
UpdateGeometryEditor(hObject);

% --------------------------------------------------------------------
function dxfrotorimporthelp_Callback(hObject, eventdata, handles)
% hObject    handle to dxfrotorimporthelp (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
figure('Name','DXF rotor import directions')
axes('position', [0 0 1 1])
image(imread('DXF_rotor_import_help.bmp'));
axis image
axis off
truesize

% --------------------------------------------------------------------
function dxfstatorimporthelp_Callback(hObject, eventdata, handles)
% hObject    handle to dxfstatorimporthelp (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
figure('Name','DXF stator import directions')
axes('position', [0 0 1 1])
image(imread('DXF_stator_import_help.bmp'));
axis image
axis off
truesize


function g=normsdm(g)
% пронумеровать подъобласти без пропусков
sdm=g(6:7,:);
nsdmbefore=[sdm(1,:) sdm(2,:)];
nsdmbefore=sort(nsdmbefore);
nsdmbefore=nsdmbefore([find(diff(nsdmbefore)) length(nsdmbefore)]);
nsdm=0:length(nsdmbefore);
newsdm=0*sdm;
for i=1:length(nsdmbefore)
    newsdm(find(sdm==nsdmbefore(i)))=i-1;
end
g(6:7,:)=newsdm;

% --- Executes on selection change in pup_preview.
function pup_preview_Callback(hObject, eventdata, handles)
% hObject    handle to pup_preview (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
redrawgeometry(handles);

% --- Executes on button press in checkbox_showmagnet.
function checkbox_showmagnet_Callback(hObject, eventdata, handles)
% hObject    handle to checkbox_showmagnet (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
redrawgeometry(handles);

% --- Executes on button press in pushbutton_redraw.
function pushbutton_redraw_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_redraw (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
redrawgeometry(handles);

function redrawgeometry(handles)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Geometry = Simulation.Geometry;
Mesh = Simulation.Mesh;
DXFrotor = Simulation.DXFrotor;
set(handles.GeometryEditor,'Pointer','watch');drawnow;
if isfield(DXFrotor,'geometry')
    DXFRotorGeometry = DXFrotor.geometry;
else
    DXFRotorGeometry = [];
end
DXFstator = Simulation.DXFstator;
if isfield(DXFstator,'geometry')
    DXFStatorGeometry = DXFstator.geometry;
else
    DXFStatorGeometry = [];
end
index=get(handles.pup_preview,'Value');
showmagnet=get(handles.checkbox_showmagnet,'Value');
switch index
    case 1
        preview = 'radial';
    case 2
        preview = 'statorslot';
    otherwise
        error('Unexpected item in popup menu <pup_preview>: something goes wrong');
end
magneterrordlg=0;
try
    Visible = get(handles.GeometryEditor,'Visible');
    if strcmp(Visible,'on')         
        geom=initgeom(Geometry,DXFRotorGeometry,DXFStatorGeometry,[],preview,Geometry.dxfstator,[],DXFstator,DXFrotor);
        [geom_meshing, ~, ~, lag]=initgeom(Geometry,DXFRotorGeometry,DXFStatorGeometry,Mesh,[],Geometry.dxfstator);
        dmin=10^-5;
        errpoint=[];
        intersect=[];
        if ~isempty(geom_meshing)
            for i=1:size(geom_meshing,2)
                x1=geom_meshing(2,i);
                x2=geom_meshing(3,i);
                y1=geom_meshing(4,i);
                y2=geom_meshing(5,i);
                x1i=geom_meshing(2,i);
                x2i=geom_meshing(3,i);
                y1i=geom_meshing(4,i);
                y2i=geom_meshing(5,i);
                if geom_meshing(1,i)==2  % if line
                    for j=1:size(geom_meshing,2)
                        x1j=geom_meshing(2,j);
                        x2j=geom_meshing(3,j);
                        y1j=geom_meshing(4,j);
                        y2j=geom_meshing(5,j);
                        %                     if isempty(x1) && isempty(x2)
                        %                         break
                        %                     end
                        if i~=j
                            if ~isempty(x1)
                                if (abs(x1-x1j)<eps && abs(y1-y1j)<eps) || (abs(x1-x2j)<eps && abs(y1-y2j)<eps)
                                    x1=[]; y1=[];
                                end
                            end
                            if ~isempty(x2)
                                if (abs(x2-x1j)<eps && abs(y2-y1j)<eps) || (abs(x2-x2j)<eps && abs(y2-y2j)<eps)
                                    x2=[]; y2=[];
                                end
                            end
                            if geom_meshing(1,j)==2  % if line
                                % находим точку пересечения прямых
                                a=(y2i-y1i); b=(x2i-x1i); c=(y2j-y1j); d=(x2j-x1j);
                                A=a*x1i-b*y1i; B=c*x1j-d*y1j;
                                y=(B-c*A/a)/(c*b/a-d);
                                x=(A+b*y)/a;
                                if ~isinf(x) && ~isinf(y)
                                    if ((x>=x1i && x<=x2i) || (x>=x2i && x<=x1i)) && ((y>=y1i && y<=y2i) || (y>=y2i && y<=y1i)) && ...
                                            ((x>=x1j && x<=x2j) || (x>=x2j && x<=x1j)) && ((y>=y1j && y<=y2j) || (y>=y2j && y<=y1j))
                                        % отрезки пересеклись или пристыкованы друг к другу
                                        if (abs(x1i-x1j)<eps && abs(y1i-y1j)<eps) || ...
                                           (abs(x2i-x1j)<eps && abs(y2i-y1j)<eps) || ...
                                           (abs(x1i-x2j)<eps && abs(y1i-y2j)<eps) || ...
                                           (abs(x2i-x2j)<eps && abs(y2i-y2j)<eps)
                                            % один отрезок пристыкован к другому
                                            stop=1;
                                        else
                                            intersect=[intersect geom_meshing(:,i) geom_meshing(:,j)];
                                        end
                                    end
                                end
                            end
                        end
                    end
                    errpoint=[errpoint [x1; y1] [x2; y2]];
                end
                if geom_meshing(1,i)==1  % if circle
                    x1=geom_meshing(2,i);
                    x2=geom_meshing(3,i);
                    y1=geom_meshing(4,i);
                    y2=geom_meshing(5,i);
                    x0=geom_meshing(8,i);
                    y0=geom_meshing(9,i);
                    R=geom_meshing(10,i);
                    if abs(sqrt((x1-x0)^2+(y1-y0)^2)-R)>eps
                        errpoint=[errpoint [x1; y1]];
                    end
                    if abs(sqrt((x2-x0)^2+(y2-y0)^2)-R)>eps
                        errpoint=[errpoint [x2; y2]];
                    end                
                end
            end
            mesherr=0;
        else
            mesherr=1;
        end
        if ~isempty(geom_meshing)
            try
                [p,e,t]=createmesh(geom_meshing,Geometry,lag,3,'Low',1.9);
            catch
                mesherr=1;
            end
        end
        newplot(handles.axes_geometryeditor);
        axes(handles.axes_geometryeditor);
        hold on
        if (~isempty(errpoint) || ~isempty(intersect)) && mesherr
            geomplot(handles.axes_geometryeditor,geom_meshing);
            R=0.01*max(abs(ylim));
            t=0:pi/100:2*pi;
            for i=1:size(errpoint,2)
                xcircle=R*sin(t)+errpoint(1,i);
                ycircle=R*cos(t)+errpoint(2,i);
                plot(xcircle,ycircle,'-r');
            end
            if ~isempty(intersect)
                geomplot(handles.axes_geometryeditor,intersect,'r');
            end
            Xlim=xlim;
            Ylim=ylim;
            text(Xlim(1),Ylim(1),' Invalid geometry detected: points are possibly not connected properly','FontSize',10,'HorizontalAlignment','left','VerticalAlignment','bottom','Color','r');
            if showmagnet && strcmp(preview,'radial')
                magneterrordlg=1;
            end
        else
            geomplot(handles.axes_geometryeditor,geom);
            if showmagnet && strcmp(preview,'radial')
                if ~mesherr
                    if Geometry.dxfstator
                        SdmProperty=DXFstator.properties;
                        doublenlayers=DXFstator.doublenlayers;
                        nSlotLayers=0;
                        for n=1:length(SdmProperty)
                            ilayer=SdmProperty(n).layer;
                            nSlotLayers=max([nSlotLayers ilayer]);
                        end
                        if doublenlayers
                            nSlotLayers=2*nSlotLayers;
                        end
                    else
                        if strcmp(Geometry.slotlayertype,'Single layer')
                            nSlotLayers=1;
                        elseif strcmp(Geometry.slotlayertype,'Double layer')
                            nSlotLayers=2;
                        end
                    end
                    Windings=Simulation.Windings;
                    [p,t,e]=replicatemesh(p,e,t,Geometry,lag,3,2,nSlotLayers,1,1,Geometry.dxfstator,DXFstator);
                    Materials.statorwindingmaterial=[]; Materials.statorironmaterial=[]; Materials.k_st_stator=1; 
                    Materials.rotorironmaterial=[]; Materials.k_st_rotor=1; Materials.magnetmaterial=[]; Materials.Nmagnetsegments=1;
                    MaterialProperties=GetMaterialProperties(Windings,Materials);
                    Subdomains=GetSubdomains(Geometry,DXFrotor,DXFstator,Windings,Materials,1,Geometry.dxfstator,1);
                    BBr=getBr(p,t,Subdomains,MaterialProperties);                          % Permanent magnets remanence flux density
                    % triangle midpoint coordinates xm ym
                    xm=p(1,t(1,:))+((p(1,t(2,:))+p(1,t(3,:)))/2-p(1,t(1,:)))*2/3;
                    ym=p(2,t(1,:))+((p(2,t(2,:))+p(2,t(3,:)))/2-p(2,t(1,:)))*2/3;
                    ind=sqrt(BBr(1,:).^2+BBr(2,:).^2)>0;
                    quiver(1000*xm(ind),1000*ym(ind),BBr(1,ind),BBr(2,ind));
                else
                    magneterrordlg=1;
                end
            end
            if mesherr
                Xlim=xlim(handles.axes_geometryeditor); Ylim=ylim(handles.axes_geometryeditor);
                if isempty(DXFRotorGeometry)
                    text(Xlim(1),Ylim(1),' No rotor geometry imported (use right-click context menu to import rotor)','FontSize',10,'HorizontalAlignment','left','VerticalAlignment','bottom','Color','r');
                elseif Geometry.dxfstator && isempty(DXFStatorGeometry)
                    text(Xlim(1),Ylim(1),' No stator geometry imported (use right-click context menu to import stator)','FontSize',10,'HorizontalAlignment','left','VerticalAlignment','bottom','Color','r');
                else
                    text(Xlim(1),Ylim(1),' Incomplete or incorrect geometry','FontSize',10,'HorizontalAlignment','left','VerticalAlignment','bottom','Color','r');
                end
            end
        end
        hold off
    end
catch
    % incorrect geometry: no preview available
    Visible = get(handles.GeometryEditor,'Visible');
    if strcmp(Visible,'on')
        newplot(handles.axes_geometryeditor);
        axes(handles.axes_geometryeditor);
        hold on
        ylim([-10 10]);
        if Geometry.dxfstator && strcmp(preview,'statorslot')
            text(0,0,'Stator slot preview is not available','FontSize',18,'HorizontalAlignment','center');
        else
            text(0,0,'Incomplete or incorrect geometry','FontSize',18,'HorizontalAlignment','center');
        end
        axis equal 
        hold off        
    end
end
if magneterrordlg
    errordlg('Not able to show magnet magnetization because of incomplete or incorrect geometry.','Geometry Editor Error','modal');
    set(handles.checkbox_showmagnet,'Value',0);
end
set(handles.GeometryEditor,'Pointer','arrow');drawnow;
% preview = 'statorslot' - stator slot preview
%           'rotorslot' -  rotor slot preview
%           'radial' -  radial cross-section preview


function EnableGeometryEditor(handles,enable)
ItemList=findobj(get(handles.GeometryEditor,'Children'));
for i=1:length(ItemList)
    Tag = get(ItemList(i),'Tag');
    if length(Tag)>2
        if strcmp(Tag(1:3),'pup') || strcmp(Tag(1:4),'edit') || (length(Tag)>8 && strcmp(Tag(1:8),'checkbox'))
            if ~strcmp(Tag,'pup_preview') && ~strcmp(Tag,'checkbox_showmagnet')
                set(ItemList(i),'Enable',enable);
            end
        end
    end
end
set(handles.dxfrotorimport,'Enable',enable);
set(handles.dxfstatorimport,'Enable',enable);


% --------------------------------------------------------------------
function plot_newwnd_Callback(hObject, eventdata, handles)
% hObject    handle to plot_newwnd (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
%
% Displays contents of axes_geometryeditor in a new figure

strlist = get(handles.pup_preview,'String');          
index = get(handles.pup_preview,'Value');
Title = strlist{index};
% Create a figure to receive this axes' data
axes1fig = figure('Name',Title);
% Copy the axes and size it to the figure
axes1copy = copyobj(handles.axes_geometryeditor,axes1fig);
set(axes1copy,'Units','Normalized',...
              'Position',[0,0.05,1,0.9]);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% --- Executes during object creation, after setting all properties.
function edit_D1s_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_D1s (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_D2s_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_D2s (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Sds_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Sds (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Ws_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Ws (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_Ns_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_R2s (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Ods_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Ods (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Ows_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Ows (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Tas_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Tas (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Rcs_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Rcs (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_l_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_l (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% --- Executes during object creation, after setting all properties.
function pup_statorslottype_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_statorslottype (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function pup_slotlayertype_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_slotlayertype (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function pup_preview_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_preview (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --------------------------------------------------------------------
function plot_GeometryEditor_Callback(hObject, eventdata, handles)
% hObject    handle to plot_GeometryEditor (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes during object creation, after setting all properties.
function GeometryEditor_CreateFcn(hObject, eventdata, handles)
% hObject    handle to GeometryEditor (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called


% --- Executes on mouse press over axes background.
function axes_geometryeditor_ButtonDownFcn(hObject, eventdata, handles)
% hObject    handle to axes_geometryeditor (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
a=1;

% --- Executes during object creation, after setting all properties.
function axes_geometryeditor_CreateFcn(hObject, eventdata, handles)
% hObject    handle to axes_geometryeditor (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: place code in OpeningFcn to populate axes_geometryeditor

% --- Executes during object creation, after setting all properties.
function pup_statorslotcornertype_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_statorslotcornertype (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Rcs_ag_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Rcs_ag (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_Dch_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Dch (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Rch_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Rch (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Tach_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Tach (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_rotorskew_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_rotorskew (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_statorskew_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_statorskew (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_layerpos_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_layerpos (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_motortype_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_motortype (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
