function varargout = materials(varargin)
% MATERIALS MATLAB code for materials.fig
%      MATERIALS, by itself, creates a new MATERIALS or raises the existing
%      singleton*.
%
%      H = MATERIALS returns the handle to a new MATERIALS or the handle to
%      the existing singleton*.
%
%      MATERIALS('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in MATERIALS.M with the given input arguments.
%
%      MATERIALS('Property','Value',...) creates a new MATERIALS or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Materials_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Materials_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help materials

% Last Modified by GUIDE v2.5 01-Feb-2018 17:07:39

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Materials_OpeningFcn, ...
                   'gui_OutputFcn',  @Materials_OutputFcn, ...
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


% --- Executes just before materials is made visible.
function Materials_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to materials (see VARARGIN)

% Choose default command line output for materials
handles.output = hObject;

motoranalysisInput = find(strcmp(varargin, 'motoranalysis'));
if ~isempty(motoranalysisInput)
   handles.motoranalysis = varargin{motoranalysisInput+1};
end
% publish function UpdateMaterials
handles.UpdateMaterials = @UpdateMaterials;

UpdateMaterialList(handles);

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes materials wait for user response (see UIRESUME)
% uiwait(handles.materials);


% --- Outputs from this function are returned to the command line.
function varargout = Materials_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes when user attempts to close materials.
function materials_CloseRequestFcn(hObject, eventdata, handles)
% Don't close this figure. It must be deleted from motoranalysis
% Make it invisible then user tries to close it
set(hObject,'Visible','off');
motoranalysishandles = guidata(handles.motoranalysis);
set(motoranalysishandles.menuMaterials,'Checked','off');


function UpdateMaterials(hObject)
handles = guidata(hObject);
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Materials = Simulation.Materials;
Windings = Simulation.Windings;
MaterialsFields = fieldnames(Materials);
for i=1:length(MaterialsFields)
    MaterialsField = MaterialsFields{i};
    editbox = ['edit_' MaterialsField];
    if isfield(handles,editbox)           % if editbox
        MaterialsFieldValue = Materials.(MaterialsField);
        set(handles.(editbox),'String',num2str(MaterialsFieldValue,10));
        if strcmp(MaterialsField,'Tsw')
            Tsw=MaterialsFieldValue;  % stator winding temperature
        end
    end
    popup = ['pup_' MaterialsField];
    if isfield(handles,popup)           % if popup menu
        set(handles.(popup),'ForegroundColor',[0 0 0]);    % black color
        MaterialsFieldValue = Materials.(MaterialsField);
        strlist = get(handles.(popup),'String');
        for n=1:length(strlist)
            if strcmp(MaterialsFieldValue,strlist{n})
                break;
            elseif n==length(strlist)
                errordlg(['Material ' MaterialsFieldValue ' is not found in Materials Library.'],'Materials Error','modal');
                set(handles.(popup),'ForegroundColor',[1 0 0]);     % mark red
                return;
            end
        end
        set(handles.(popup),'Value',n);
        set(handles.(popup),'UserData',n);        % store item index in UserData
        if strcmp(MaterialsField,'statorwindingmaterial')
            resistivity=ReadMaterialData('Conductor',MaterialsFieldValue,'<Electric resistivity>');               % stator winding material resistivity
            alfa_s=ReadMaterialData('Conductor',MaterialsFieldValue,'<Temperature coefficient of resistance>');   % stator winding material temperature coefficient of resistance
        end
    end
end
% update Windings
if ~isempty(resistivity) && ~isempty(alfa_s)
    if isempty(Simulation.Private)    % if simulation file is not locked
        ks=1/resistivity;
        ks=ks/(1+alfa_s*(Tsw-20));
        if isempty(Windings.ks) || Windings.ks~=ks
            Windings.ks=ks;
            Simulation.Windings = Windings;
            motoranalysishandles.Simulation = Simulation;
            motoranalysishandles.Saved = 0;
            guidata(handles.motoranalysis,motoranalysishandles);
            WindingEditor=motoranalysishandles.WindingEditor;
            WindingEditorHandles = guidata(WindingEditor);
            WindingEditorHandles.UpdateWindingEditor(WindingEditor,0,0);
        end
    end
end
EnableMaterials(handles);


function editMaterials_Callback(hObject, eventdata, handles)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Materials = Simulation.Materials;
% editbox Tag
Tag = get(hObject,'Tag');
if strcmp(Tag(1:4),'edit')     % if editbox changed
    % editbox value
    String = get(hObject,'String');
    MaterialsField = Tag(6:end);
    if isfield(Materials,MaterialsField)
        [MaterialsFieldValue, status] = str2num(String);
        ok=0;
        showerrdlg=1;
        if status && isreal(MaterialsFieldValue) && ~isinf(MaterialsFieldValue) && ~isnan(MaterialsFieldValue) && length(MaterialsFieldValue)==1
            ok=1;
            if (strcmp(MaterialsField,'k_st_stator') || strcmp(MaterialsField,'k_st_rotor'))
                if MaterialsFieldValue<=0 || MaterialsFieldValue>1
                    ok=0;
                    showerrdlg=0;
                    errordlg('Stacking factor should be more than 0 and less than or equal to 1.','Materials Error','modal');
                end
            elseif (strcmp(MaterialsField,'Nmagnetsegments'))
                if MaterialsFieldValue<=0
                    ok=0;
                    showerrdlg=0;
                    errordlg('Number of magnet segments should be more than 0.','Materials Error','modal');
                end    
            end
        end
        if ok
            Materials.(MaterialsField)=MaterialsFieldValue;
        else
            if showerrdlg
                errordlg('Not a valid value.','Materials Error','modal');
            end
            editbox=['edit_' MaterialsField];
            set(handles.(editbox),'String',num2str(Materials.(MaterialsField)));
            return
        end
    end
elseif strcmp(Tag(1:3),'pup')     % if popupmenu changed
    % popupmenu value
    index = get(hObject,'Value');
    strlist = get(hObject,'String');
    str = strlist{index,1};
    Field = Tag(5:end);
    if isfield(Materials,Field)
        if ~isempty(str)
            Materials.(Field)=str;
        else
            error('Something goes wrong');
        end
    end
else
    error('Undefined field');
end
Simulation.Materials = Materials;
motoranalysishandles.Simulation = Simulation;
motoranalysishandles.Saved = 0;
guidata(handles.motoranalysis,motoranalysishandles);
UpdateMaterials(hObject);

function EnableMaterials(handles)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
if isempty(Simulation.Private)
    enable = 'on';
else
    enable = 'off';
end
set(handles.pup_statorwindingmaterial,'Enable',enable);
set(handles.pup_statorironmaterial,'Enable',enable);
set(handles.edit_k_st_stator,'Enable',enable);
set(handles.pup_rotorironmaterial,'Enable',enable);
set(handles.edit_k_st_rotor,'Enable',enable);
set(handles.pup_magnetmaterial,'Enable',enable);
set(handles.edit_Tsw,'Enable',enable);
set(handles.edit_Tpm,'Enable',enable);
set(handles.edit_Nmagnetsegments,'Enable',enable);



% --- Executes on button press in pushbutton_updatematerials.
function pushbutton_updatematerials_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_updatematerials (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
UpdateMaterialList(handles);
UpdateMaterials(hObject);


function MaterialList=GetMaterialList(Type)
% List of available materials
MaterialList=[];
switch Type
    case 'Conductor'
        list=dir('Materials\Conductor');
    case 'Iron'
        list=dir('Materials\Iron');
    case 'Magnet'
        list=dir('Materials\Magnet');
end
if isempty(list)
    return
end
MaterialList={'Not assigned'};
for i=1:length(list)
    if length(list(i).name)>4 && strcmp(list(i).name(end-3:end),'.txt')
        MaterialList=celladd(MaterialList,list(i).name(1:end-4));
    end
end


function UpdateMaterialList(handles)
MaterialList=GetMaterialList('Conductor');
if isempty(MaterialList)
    error('Materials Library not found')
end
set(handles.pup_statorwindingmaterial,'String',MaterialList);

MaterialList=GetMaterialList('Iron');
if isempty(MaterialList)
    error('Materials Library not found')
end
set(handles.pup_statorironmaterial,'String',MaterialList);
set(handles.pup_rotorironmaterial,'String',MaterialList);

MaterialList=GetMaterialList('Magnet');
if isempty(MaterialList)
    error('Materials Library not found')
end
set(handles.pup_magnetmaterial,'String',MaterialList);



% --- Executes on button press in pushbutton_plotBHcurve_stator.
function pushbutton_plotBHcurve_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_plotBHcurve_stator (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Materials = Simulation.Materials;
Tag = get(hObject,'Tag');
if strcmp(Tag,'pushbutton_plotBHcurve_stator')
    materialname=Materials.statorironmaterial;
elseif strcmp(Tag,'pushbutton_plotBHcurve_rotor')
    materialname=Materials.rotorironmaterial;
else
    error('Something goes wrong!')
end
if strcmp(materialname,'Not assigned')
    errordlg('Material is not assigned.','Materials Error','modal');
    return
end
set(handles.materials,'Pointer','watch'); drawnow;
filepath='Materials\Iron\';
if exist([filepath materialname '.txt'],'file')
    BHcurve=ReadMaterialData('Iron',materialname,'<B-H curve>');
    if isempty(BHcurve)
        errordlg('No B-H curve available.','Materials Error','modal');
        set(handles.materials,'Pointer','arrow');
        return
    end
    B=BHcurve(:,2); H=BHcurve(:,1);
    if H(1)~=0
        H = [0; H];
        B = [0; B];
    end
    BB=linspace(B(1),B(end),100000);
    HH = spline(B,H,BB);
    Hmin=1.1*min(HH);
    if Hmin>0, Hmin=0; end
    inds_incorrect=find(diff(HH)<0);
    figure('Name',[ 'B-H curve (' materialname ')']);
    hold on
    plot(HH,BB);grid; axis([Hmin max(HH) 0 1.1*B(end)]);
    xlabel('Magnetic field intensity, A/m');
    ylabel('Magnetic flux density, T');
    scatter(H,B,30,'filled','k');
    if ~isempty(inds_incorrect)
        scatter(HH(inds_incorrect),BB(inds_incorrect),5,'filled','r');
    end
    hold off
else
    errordlg([filepath materialname '.txt is not found.'],'Materials Error','modal');
end
set(handles.materials,'Pointer','arrow');drawnow;


% --- Executes on button press in pushbutton_plotIronLoss_stator.
function pushbutton_plotIronLoss_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_plotIronLoss_stator (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Materials = Simulation.Materials;
Tag = get(hObject,'Tag');
if strcmp(Tag,'pushbutton_plotIronLoss_stator')
    materialname=Materials.statorironmaterial;
elseif strcmp(Tag,'pushbutton_plotIronLoss_rotor')
    materialname=Materials.rotorironmaterial;
else
    error('Something goes wrong!')
end
if strcmp(materialname,'Not assigned')
    errordlg('Material is not assigned.','Materials Error','modal');
    return
end
set(handles.materials,'Pointer','watch'); drawnow;
filepath='Materials\Iron\';
if exist([filepath materialname '.txt'],'file')
    ironloss=ReadMaterialData('Iron',materialname,'<Iron loss>');
    if isempty(ironloss)
        errordlg('No iron loss data available. Iron loss will not be computed.','Materials Error','modal');
        set(handles.materials,'Pointer','arrow');
        return
    else
        [Steinmetz, frq, Bpeak, IronLoss]=Ironloss2Steinmetz(ironloss);
        if isempty(Steinmetz)
            errordlg('Iron loss data format is not correct. Iron loss will not be computed.','Materials Error','modal');
            set(handles.materials,'Pointer','arrow');    
            return
        end
    end
    Colorrgb=[[0 0 255]; [0 255 0]; [255 0 0]; [0 255 255]; [255 0 255]; [134 0 134]; [0 139 139]; [154 205 50]; 
              [139 0 0]; [255 69 0]; [32 178 170]; [255 165 0]; [233 150 122]; [173 255 47]]/255;
    Leg={};
    h=figure('Name',[ 'Iron loss (' materialname ')']);
    set(0,'Units','pixels') 
    scnsize = get(0,'ScreenSize');
    set(h,'OuterPosition',scnsize);
    ax1 = axes('Position',[0 0 1 1],'Visible','off');
    ax2 = axes('Position',[.2 .1 .7 .8]);
    hold on
    if ~isempty(frq) && ~isempty(Bpeak) && ~isempty(IronLoss)
        if Bpeak(1)>0
            Bpeak=[0 Bpeak];
            IronLoss=[zeros(1,length(frq));
                      IronLoss];
        end
        bpeak=linspace(Bpeak(1),Bpeak(end),1000);
        icolor=1;
        for i=1:length(frq)
            ironlosspoints=IronLoss(:,i);
            Bpeakmax=max(Bpeak(~isnan(ironlosspoints)));
            ironloss=spline(Bpeak(~isnan(ironlosspoints)),ironlosspoints(~isnan(ironlosspoints)),bpeak(bpeak<Bpeakmax));
            plot(ax2,bpeak(bpeak<Bpeakmax),ironloss,'Color',Colorrgb(icolor,:));
            Leg=celladd(Leg,[num2str(frq(i)) ' Hz']);
            icolor=icolor+1;
            if icolor>length(Colorrgb)
                icolor=1;
            end
        end
    else
        frq=[20 50 100 200 500 1000 2500 5000 10000];
        bpeak=linspace(0,2,1000);
    end
    Kh=Steinmetz.Kh;
    alfa=Steinmetz.alfa;
    beta=Steinmetz.beta;
    Ke=Steinmetz.Ke;
    icolor=1;
    if ~isempty(frq) && ~isempty(Bpeak) && ~isempty(IronLoss)
        linestyle='--';
    else
        linestyle='-';
    end
    for i=1:length(frq)
        ironloss=Kh*(frq(i)^alfa)*(bpeak.^beta)+Ke*(frq(i)*bpeak).^2;
        plot(ax2,bpeak,ironloss,'Color',Colorrgb(icolor,:),'LineStyle',linestyle); 
        Leg=celladd(Leg,[num2str(frq(i)) ' Hz (Steinmetz fitted)']);
        icolor=icolor+1;
        if icolor>length(Colorrgb)
            icolor=1;
        end
    end
    if ~isempty(frq) && ~isempty(Bpeak) && ~isempty(IronLoss)
        for i=1:length(frq)
            ironlosspoints=IronLoss(:,i);
            scatter(ax2,Bpeak,ironlosspoints,30,'filled','k');
        end
    end
    grid;legend(Leg,'Location','NorthWest');
    xlabel('Peak magnetic flux density, T');
    ylabel('Iron loss, W/kg');
    hold off
    descr={'Iron loss Steinmetz equation:';
           'Pil=Kh*(f ^a)*(Bm^b)+Ke*(f*Bm)^2';
           ' ';
           ['Kh = ' num2str(Kh)];
           ['a = ' num2str(alfa)];
           ['Ke = ' num2str(Ke)];
           ['b = ' num2str(beta)];};
    axes(ax1); % sets ax1 to current axes
    text(.025,0.6,descr)       
    axes(ax2);       
%     text(['Iron loss Steinmetz equation: P=Kh*(f^alfa)*(Bm^beta)+Ke*(f*Bm)^2 (Kh=' num2str(Kh) ', alfa=' num2str(alfa) ', Ke=' num2str(Ke) ', beta=' num2str(beta)]);
    
else
    errordlg([filepath materialname '.txt is not found.'],'Materials Error','modal');
end
set(handles.materials,'Pointer','arrow');drawnow;


% --- Executes on button press in pushbutton_statorwindingmaterialproperties.
function pushbutton_viewproperties_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_statorwindingmaterialproperties (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Materials = Simulation.Materials;
Tag = get(hObject,'Tag');
if strcmp(Tag,'pushbutton_statorwindingmaterialproperties')
    filename=Materials.statorwindingmaterial;
    filepath='Materials\Conductor\';
elseif strcmp(Tag,'pushbutton_statorironmaterialproperties')
    filename=Materials.statorironmaterial;
    filepath='Materials\Iron\';
elseif strcmp(Tag,'pushbutton_rotorironmaterialproperties')
    filename=Materials.rotorironmaterial;
    filepath='Materials\Iron\';
elseif strcmp(Tag,'pushbutton_magnetmaterialproperties')
    filename=Materials.magnetmaterial;
    filepath='Materials\Magnet\';
else
    error('Something goes wrong!')
end
if strcmp(filename,'Not assigned')
    errordlg('Material is not assigned.','Materials Error','modal');
    return
end
if exist([filepath filename '.txt'],'file')
    eval(['!notepad ' filepath filename '.txt &']);
else
    errordlg([filepath filename '.txt is not found.'],'Materials Error','modal');
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% --- Executes during object creation, after setting all properties.
function pup_magnetmaterial_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_magnetmaterial (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_rotorironmaterial_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_rotorironmaterial (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_k_st_rotor_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_k_st_rotor (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_statorironmaterial_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_statorironmaterial (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_k_st_stator_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_k_st_stator (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_statorwindingmaterial_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_statorwindingmaterial (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_Tpm_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Tpm (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_Tsw_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Tsw (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_Nmagnetsegments_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Nmagnetsegments (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
