# Auto-generated from windingeditor.m
# NOTE: This is a placeholder stub. Manual translation required.

from __future__ import annotations

"""
Original MATLAB source:

function varargout = windingeditor(varargin)
% WINDINGEDITOR M-file for WindingEditor.fig
%      WINDINGEDITOR, by itself, creates a new WINDINGEDITOR or raises the existing
%      singleton*.
%
%      H = WINDINGEDITOR returns the handle to a new WINDINGEDITOR or the handle to
%      the existing singleton*.
%
%      WINDINGEDITOR('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in WINDINGEDITOR.M with the given input arguments.
%
%      WINDINGEDITOR('Property','Value',...) creates a new WINDINGEDITOR or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before WindingEditor_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to WindingEditor_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help WindingEditor

% Last Modified by GUIDE v2.5 25-Aug-2017 13:16:30

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @WindingEditor_OpeningFcn, ...
                   'gui_OutputFcn',  @WindingEditor_OutputFcn, ...
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


% --- Executes just before WindingEditor is made visible.
function WindingEditor_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to WindingEditor (see VARARGIN)

% Choose default command line output for WindingEditor
handles.output = hObject;

motoranalysisInput = find(strcmp(varargin, 'motoranalysis'));
if ~isempty(motoranalysisInput)
   handles.motoranalysis = varargin{motoranalysisInput+1};
end
% publish functions
handles.UpdateWindingEditor = @UpdateWindingEditor;
handles.GetStatorWinding=@GetStatorWinding;
data=cell(10,4);
for i=1:10
    data{i,1}=i;
end
set(handles.table_layout1,'Data',data);
set(handles.table_layout2,'Data',data);
set(handles.table_layout3,'Data',data);
set(handles.table_layout1, 'ColumnEditable', true);
set(handles.table_layout2, 'ColumnEditable', true);
set(handles.table_layout3, 'ColumnEditable', true);
columnformat = cell(1,4);
for i=1:10
    columnformat{1,i}='char';
end
set(handles.table_layout1,'ColumnFormat',columnformat);
set(handles.table_layout2,'ColumnFormat',columnformat);
set(handles.table_layout3,'ColumnFormat',columnformat);

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes WindingEditor wait for user response (see UIRESUME)
% uiwait(handles.WindingEditor);


% --- Outputs from this function are returned to the command line.
function varargout = WindingEditor_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;

% --- Executes when user attempts to close WindingEditor.
function WindingEditor_CloseRequestFcn(hObject, eventdata, handles)
% Don't close this figure. It must be deleted from motoranalysis
% Make it invisible then user tries to close it
set(hObject,'Visible','off');
motoranalysishandles = guidata(handles.motoranalysis);
set(motoranalysishandles.menuWindingEditor,'Checked','off');


function UpdateWindingEditor(hObject,layouterrdlg,RsLsewerrdlg)
handles = guidata(hObject);
set(handles.WindingEditor,'Pointer','watch'); drawnow;
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
% if strcmp(get(handles.WindingEditor,'Visible'),'off') && ~layouterrdlg && ~RsLsewerrdlg
%     return
% end
% update parameters defined in Geometry Editor first
Geometry = Simulation.Geometry;
Windings = Simulation.Windings;
Mesh = Simulation.Mesh;
GroupEnable(handles,'on');
Ns = Geometry.Ns;
set(handles.edit_Ns,'String',num2str(Ns));
if Geometry.dxfstator
    try
        SdmProperty=Simulation.DXFstator.properties;
        doublenlayers=Simulation.DXFstator.doublenlayers;
        nSlotLayers=0;
        for n=1:length(SdmProperty)
            ilayer=SdmProperty(n).layer;
            nSlotLayers=max([nSlotLayers ilayer]);
        end
        if doublenlayers
            nSlotLayers=2*nSlotLayers;
        end
        set(handles.edit_slotlayertype,'String',num2str(nSlotLayers));
    catch
        nSlotLayers=0;
        set(handles.edit_slotlayertype,'String','');
    end
    Windings.wiresizemethod='Slot fill factor';
    set(handles.pup_wiresizemethod,'Enable','off');
    set(handles.text_fillfactor,'String','Coil fill factor:');
    Tooltip=sprintf('Ratio of the area of all conductors (i.e. pure copper or aluminum) of a slot \nto the slot area occupied by the conductors not including slot isolation.');
    set(handles.text_fillfactor,'TooltipString',Tooltip);
    set(handles.edit_fillfactor,'TooltipString',Tooltip);
else
    if strcmp(Windings.layoutmethod,'From file')     % layout table from file
        set(handles.edit_slotlayertype,'String',[]);
        nSlotLayers=0;
    else
        slotlayertype = Geometry.slotlayertype;
        if strcmp(slotlayertype,'Single layer')
            set(handles.edit_slotlayertype,'String',num2str(1));
            nSlotLayers=1;
        elseif strcmp(slotlayertype,'Double layer')
            set(handles.edit_slotlayertype,'String',num2str(2));
            nSlotLayers=2;
        else
            error('Unexpected value for winding layer type: something goes wrong');
        end
    end
    set(handles.pup_wiresizemethod,'Enable','on');
    set(handles.text_fillfactor,'String','Slot fill factor:');
    Tooltip=sprintf('Ratio of the area of all conductors (i.e. pure copper or aluminum) \nof a slot to the total slot area (including slot isolation).');
    set(handles.text_fillfactor,'TooltipString',Tooltip);
    set(handles.edit_fillfactor,'TooltipString',Tooltip);
end
% update editbox values and table layout    
WindingsFields = fieldnames(Windings);
for i=1:length(WindingsFields)
    WindingsField = WindingsFields{i};
    editbox = ['edit_' WindingsField];
    if isfield(handles,editbox)           % if editbox
        if strcmp(WindingsField,'fillfactor')
            set(handles.edit_fillfactor,'Enable','on');
            if ~Geometry.dxfstator
                if strcmp(Windings.wiresizemethod,'Wire diameter') || strcmp(Windings.wiresizemethod,'AWG') || ...
                   strcmp(Windings.wiresizemethod,'SWG')
                    wirediameter=Windings.wirediameter/1000;   
                    conductorarea=Windings.W*Windings.nstrands*pi*(wirediameter/2)^2;
                    try
                        [~, Sss] = initgeom(Geometry,[],[],Mesh,[],Geometry.dxfstator,[]);   % stator slot area
                        Windings.fillfactor=conductorarea/Sss;
                    catch
                        Windings.fillfactor=[];
                    end
                    set(handles.edit_fillfactor,'Enable','off');
                end
            end
        end        
        WindingsFieldValue = getfield(Windings,WindingsField);
        if WindingsFieldValue<0.0001
            set(getfield(handles,editbox),'String',num2str(WindingsFieldValue,7));
        else
            set(getfield(handles,editbox),'String',num2str(WindingsFieldValue,10));
        end
        if strcmp(WindingsField,'fillfactor')
            if isempty(Windings.fillfactor) || Windings.fillfactor>1 || Windings.fillfactor<0
                if ~isempty(Windings.layout) && ~isempty(Windings.Npp) && ~isempty(Windings.W) && ~isempty(Ns)
                    set(getfield(handles,editbox),'ForegroundColor',[1 0 0]);     % mark red
                    if Geometry.dxfstator
                        set(handles.text_warning,'String','Empty or incorrect coil fill factor');
                    else
                        set(handles.text_warning,'String','Empty or incorrect slot fill factor');
                    end
                    set(handles.text_warning,'Visible','on');
                end
            else
                set(getfield(handles,editbox),'ForegroundColor',[0 0 0]);     % black color
                set(handles.text_warning,'Visible','off');
            end
        end
    end
    popup = ['pup_' WindingsField];
    if isfield(handles,popup)           % if popup menu
        if strcmp(WindingsField,'statorcircuit')
            FieldValue = getfield(Windings,WindingsField);
            SetStatorCircuit(handles,FieldValue);
        elseif strcmp(WindingsField,'wiresize')
            set(handles.pup_wiresize,'Visible','on');
            set(handles.text_wiresize,'Visible','on');
            set(handles.edit_wirediameter,'Visible','on');
            set(handles.text_wirediameter,'Visible','on');
            set(handles.text_wirediameter_units,'Visible','on');
            if strcmp(Windings.wiresizemethod,'AWG') || strcmp(Windings.wiresizemethod,'SWG')
                set(handles.edit_wirediameter,'Enable','off');
                strlist = get(getfield(handles,popup),'String');
                if strcmp(Windings.wiresizemethod,'AWG')
                    strlistawg={'4/0 AWG'; '3/0 AWG'; '2/0 AWG'; '1/0 AWG';
                                '1 AWG'; '2 AWG'; '3 AWG'; '4 AWG'; '5 AWG'; '6 AWG'; '7 AWG'; '8 AWG'; '9 AWG'; '10 AWG';
                                '11 AWG'; '12 AWG'; '13 AWG'; '14 AWG'; '15 AWG'; '16 AWG'; '17 AWG'; '18 AWG'; '19 AWG'; '20 AWG';
                                '21 AWG'; '22 AWG'; '23 AWG'; '24 AWG'; '25 AWG'; '26 AWG'; '27 AWG'; '28 AWG'; '29 AWG'; '30 AWG';
                                '31 AWG'; '32 AWG'; '33 AWG'; '34 AWG'; '35 AWG'; '36 AWG'; '37 AWG'; '38 AWG'; '39 AWG'; '40 AWG'};
                    if length(strlist)~=length(strlistawg)
                        set(handles.pup_wiresize,'Value',1);      % just in case Value>length(strlistawg)
                        set(getfield(handles,popup),'String',strlistawg);
                    end
                    if ~strcmp(Windings.wiresize(end-2:end),'AWG')
                        Windings.wiresize(end-2:end)='AWG';
                    end
                    wiresize=Windings.wiresize;
                    for n=1:length(strlistawg)
                        if strcmp(wiresize,strlistawg(n))
                            break;
                        elseif n==length(strlistawg)
                            n=24;
                            Windings.wiresize='20 AWG';
                            break;
                        end
                    end
                    diamawg=[11.684 10.405 9.266 8.251 7.348 6.544 5.827 5.189 4.621 4.115 3.665 3.264 2.906 2.588 2.305 2.053 1.828 1.628 ...
                             1.450 1.291 1.150 1.024 0.912 0.812 0.723 0.644 0.573 0.511 0.455 0.405 0.361 0.321 0.286 0.254 0.227 0.202 ...
                             0.180 0.160 0.143 0.127 0.113 0.101 0.0897 0.0799];
                    Windings.wirediameter=diamawg(n);
                elseif strcmp(Windings.wiresizemethod,'SWG')
                    strlistswg={'7/0 SWG'; '6/0 SWG'; '5/0 SWG'; '4/0 SWG'; '3/0 SWG'; '2/0 SWG'; '1/0 SWG';
                                '1 SWG'; '2 SWG'; '3 SWG'; '4 SWG'; '5 SWG'; '6 SWG'; '7 SWG'; '8 SWG'; '9 SWG'; '10 SWG';
                                '11 SWG'; '12 SWG'; '13 SWG'; '14 SWG'; '15 SWG'; '16 SWG'; '17 SWG'; '18 SWG'; '19 SWG'; '20 SWG';
                                '21 SWG'; '22 SWG'; '23 SWG'; '24 SWG'; '25 SWG'; '26 SWG'; '27 SWG'; '28 SWG'; '29 SWG'; '30 SWG';
                                '31 SWG'; '32 SWG'; '33 SWG'; '34 SWG'; '35 SWG'; '36 SWG'; '37 SWG'; '38 SWG'; '39 SWG'; '40 SWG';
                                '41 SWG'; '42 SWG'; '43 SWG'; '44 SWG'; '45 SWG'; '46 SWG'; '47 SWG'; '48 SWG'; '49 SWG'; '50 SWG'};     
                    if length(strlist)~=length(strlistswg)
                        set(getfield(handles,popup),'String',strlistswg);
                    end
                    if ~strcmp(Windings.wiresize(end-2:end),'SWG')
                        Windings.wiresize(end-2:end)='SWG';
                    end
                    wiresize=Windings.wiresize;
                    for n=1:length(strlistswg)
                        if strcmp(wiresize,strlistswg(n))
                            break;
                        elseif n==length(strlistswg)
                            n=27;
                            Windings.wiresize='20 SWG';
                            break;
                        end
                    end
                    diamswg=[12.700 11.786  10.973 10.160 9.449 8.839 8.230 7.620 7.010 6.401 5.893 5.385 4.877 4.470 4.064 3.658 3.251 2.946 ...
                             2.642 2.337 2.032 1.829 1.626 1.422 1.219 1.016 0.914 0.813 0.711 0.610 0.559 0.5080 0.4572 0.4166 0.3759 0.3454 ...
                             0.3150 0.2946 0.2743 0.2540 0.2337 0.2134 0.1930 0.1727 0.1524 0.1321 0.1219 0.1118 0.1016 0.0914 0.0813 0.0711 ...
                             0.0610 0.0508 0.0406 0.0305 0.0254];
                    Windings.wirediameter=diamswg(n);
                end
                set(handles.pup_wiresize,'Value',n);
                set(handles.pup_wiresize,'UserData',n);        % store item index in UserData
                set(handles.pup_wiresize,'Visible','on');
                set(handles.text_wiresize,'Visible','on');
            else      % wiresizemethod=='Wire diameter'  ||  wiresizemethod=='Slot fill factor'
                set(handles.pup_wiresize,'Value',1);     % just in case Value>length(String)
                set(handles.pup_wiresize,'Visible','off');
                set(handles.text_wiresize,'Visible','off');
                set(handles.edit_wirediameter,'Enable','on');
                if strcmp(Windings.wiresizemethod,'Slot fill factor')
                    set(handles.edit_wirediameter,'Visible','off');
                    set(handles.text_wirediameter,'Visible','off');
                    set(handles.text_wirediameter_units,'Visible','off');
                end
            end
        else
            WindingsFieldValue = getfield(Windings,WindingsField);
            strlist = get(getfield(handles,popup),'String');
            for n=1:length(strlist)
                if strcmp(WindingsFieldValue,strlist(n))
                    break;
                elseif n==length(strlist)
                    error(['Inappropriate value for <' WindingsField '>: something goes wrong']);
                    return;
                end
            end
            set(getfield(handles,popup),'Value',n);
            set(getfield(handles,popup),'UserData',n);        % store item index in UserData
        end
    end
    if strcmp(WindingsField,'layout')
        layout=Windings.layout;
        if strcmp(Windings.layoutmethod,'Automatic')    % if Automatic layout input method
            if nSlotLayers>2, error(' '); end
            set(handles.table_layout1,'Enable','on');
            set(handles.table_layout2,'Enable','on');
            set(handles.table_layout3,'Enable','on');
            set(handles.table_layout1,'ColumnEditable',false);
            set(handles.table_layout2,'ColumnEditable',false);
            set(handles.table_layout3,'ColumnEditable',false);
            set(handles.pup_windingtype,'Enable','on');
            set(handles.edit_nPolePairs,'Enable','on');
            set(handles.edit_coilspan,'Enable','on');
            set(handles.pushbutton_layoutfromfile,'Visible','off');
            set(handles.pup_Lsew_inputmethod,'Enable','on');
            set(handles.pup_Rs_inputmethod,'Enable','on');
            nPolePairs=Windings.nPolePairs;
            coilspan=Windings.coilspan;
            windingtype=Windings.windingtype;
            Npp=Windings.Npp;
            [layout1, layout2, layout3]=getlayout(Ns,nPolePairs,coilspan,windingtype,nSlotLayers,Npp,layouterrdlg,0);
            Windings.layout.layout1=layout1;
            Windings.layout.layout2=layout2;
            Windings.layout.layout3=layout3;
            Simulation.Windings=Windings;
            motoranalysishandles.Simulation=Simulation;
            guidata(handles.motoranalysis,motoranalysishandles);
        elseif strcmp(Windings.layoutmethod,'Manual')    % if Manual layout input method
            if nSlotLayers>2, error(' '); end
            set(handles.table_layout1,'Enable','on');
            set(handles.table_layout2,'Enable','on');
            set(handles.table_layout3,'Enable','on');
            set(handles.table_layout1,'ColumnEditable',true);
            set(handles.table_layout2,'ColumnEditable',true);
            set(handles.table_layout3,'ColumnEditable',true);
            set(handles.pup_windingtype,'Enable','off');
            set(handles.edit_nPolePairs,'Enable','off');
            set(handles.edit_coilspan,'Enable','off');
            set(handles.pushbutton_layoutfromfile,'Visible','off');
            set(handles.pup_Lsew_inputmethod,'Enable','on');
            set(handles.pup_Rs_inputmethod,'Enable','on');
            [layout1, layout2, layout3]=getlayout(Ns,[],[],[],nSlotLayers,[],0,1);
            if isfield(layout,'layout1') && ~isempty(layout.layout1)
                nr=size(layout.layout1,1);
                for j=1:size(layout1,1)
                    for k=2:4
                        if j<=nr
                            layout1{j,k}=layout.layout1{j,k};
                            layout2{j,k}=layout.layout2{j,k};
                            layout3{j,k}=layout.layout3{j,k};
                        else
                            layout1{j,k}=[];
                            layout2{j,k}=[];
                            layout3{j,k}=[];
                        end
                    end
                end
            end
        elseif strcmp(Windings.layoutmethod,'From file')    % if layout from file
            set(handles.table_layout1,'Enable','off');
            set(handles.table_layout2,'Enable','off');
            set(handles.table_layout3,'Enable','off');
            set(handles.pup_windingtype,'Enable','off');
            set(handles.edit_nPolePairs,'Enable','off');
            set(handles.edit_coilspan,'Enable','off');
            set(handles.pushbutton_layoutfromfile,'Visible','on');
            set(handles.pup_Lsew_inputmethod,'Enable','off');
            set(handles.pup_Rs_inputmethod,'Enable','off');
            layout1=[]; layout2=[]; layout3=[];
        end
        set(handles.table_layout1,'Data',layout1);
        set(handles.table_layout2,'Data',layout2);
        set(handles.table_layout3,'Data',layout3);
        if strcmp(Windings.Lsew_inputmethod,'Automatic') || strcmp(Windings.Rs_inputmethod,'Automatic')   % if automatic input method for Rs or Lsew
            D2s=Geometry.D2s/1000;
            Sds=Geometry.Sds/1000;
            l=Geometry.l/1000;
            W=Windings.W;
            Npp=Windings.Npp;
            Hsew=Windings.Hsew/1000;
            slotlayertype=Geometry.slotlayertype;
            fillfactor=Windings.fillfactor;
            ks=Windings.ks;
            Rs=[]; Lsew=[];
            if isempty(ks)
                if RsLsewerrdlg
                    errordlg('Stator conductor material is not assigned.','Materials Error','modal');
                end
            else
                try
                    if Hsew<=0, error(' '); end
                    [Rs, Lsew]=GetStatorWinding(Geometry,Mesh,Windings,layout1,layout2,layout3,Ns,D2s,Sds,Hsew,W,slotlayertype,ks,fillfactor,Npp,l,RsLsewerrdlg);
                catch
                    if RsLsewerrdlg
                        errordlg('Some parameters might be incorrect.','Winding Editor Error','modal');
                    end
                end
            end
            if strcmp(Windings.Lsew_inputmethod,'Automatic')
                set(handles.edit_Lsew,'Enable','off');
                Windings.Lsew=Lsew;
                Simulation.Windings=Windings;
                motoranalysishandles.Simulation=Simulation;
                guidata(handles.motoranalysis,motoranalysishandles);
            end
            if strcmp(Windings.Rs_inputmethod,'Automatic')
                set(handles.edit_Rs,'Enable','off');
                Windings.Rs=Rs;
                Simulation.Windings=Windings;
                motoranalysishandles.Simulation=Simulation;
                guidata(handles.motoranalysis,motoranalysishandles);
            end
        end
    end
end
if ~isempty(Simulation.Private)
    % lock Winding Editor
    GroupEnable(handles,'off');
end
set(handles.edit_Ns,'Enable','inactive');
set(handles.edit_slotlayertype,'Enable','inactive');
if isempty(Simulation.Private)
    if get(handles.pup_layoutmethod,'Value')==2    % if Automatic layout input method
        set(handles.table_layout1,'ColumnEditable',false);
        set(handles.table_layout2,'ColumnEditable',false);
        set(handles.table_layout3,'ColumnEditable',false);
    else
        set(handles.table_layout1,'ColumnEditable',true);
        set(handles.table_layout2,'ColumnEditable',true);
        set(handles.table_layout3,'ColumnEditable',true);
    end
    set(handles.pup_statorcircuit,'Enable','on');
    set(handles.pup_layoutmethod,'Enable','on');
    set(handles.pup_windingtype,'Enable','on');    
    set(handles.pup_Lsew_inputmethod,'Enable','on');
    set(handles.pup_Rs_inputmethod,'Enable','on');
    set(handles.pushbutton_layoutfromfile,'Enable','on');
else
    set(handles.table_layout1,'ColumnEditable',false);
    set(handles.table_layout2,'ColumnEditable',false);
    set(handles.table_layout3,'ColumnEditable',false);    
    set(handles.pup_statorcircuit,'Enable','off');
    set(handles.pup_layoutmethod,'Enable','off');
    set(handles.pup_windingtype,'Enable','off');  
    set(handles.pup_Lsew_inputmethod,'Enable','off');
    set(handles.pup_Rs_inputmethod,'Enable','off');
    set(handles.pushbutton_layoutfromfile,'Enable','off');
end
if get(handles.pup_layoutmethod,'Value')==3 || Simulation.Geometry.dxfstator    % if layout input method From file or stator geometry from dxf-file
    set(handles.pup_Lsew_inputmethod,'Enable','off');
    set(handles.pup_Rs_inputmethod,'Enable','off');
end
if get(handles.pup_layoutmethod,'Value')==3      % if layout input method From file
    set(handles.edit_Npp,'Enable','off');
end
if get(handles.pup_layoutmethod,'Value')==1 || get(handles.pup_layoutmethod,'Value')==3     % if Manual layout input method or layout From file
    set(handles.pup_windingtype,'Enable','off');
    set(handles.edit_nPolePairs,'Enable','off');
    set(handles.edit_coilspan,'Enable','off');
end
if nSlotLayers>2
    set(handles.pup_layoutmethod,'Enable','off');
end
guidata(hObject, handles);

Simulation.Windings = Windings;
motoranalysishandles.Simulation = Simulation;
guidata(handles.motoranalysis,motoranalysishandles);

redrawwindings(handles);
set(handles.WindingEditor,'Pointer','arrow');


function editWindingCallback(hObject, eventdata, handles)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Windings = Simulation.Windings;
layouterrdlg=0;
RsLsewerrdlg=0;
% editbox Tag
Tag = get(hObject,'Tag');
if strcmp(Tag(1:4),'edit')     % if editbox changed
    % editbox value
    String = get(hObject,'String');
    WindingsField = Tag(6:end);
    if isfield(Windings,WindingsField)
        if ~isempty(String)
            [WindingsFieldValue, status] = str2num(String);
            if length(WindingsFieldValue)>1
                status=0;
            end
            if status && isreal(WindingsFieldValue) && ~isinf(WindingsFieldValue) && ~isnan(WindingsFieldValue)
                Windings = setfield(Windings,WindingsField,WindingsFieldValue);
            else
                errordlg('Not a valid value.','Winding Editor Error','modal');
                editbox=['edit_' WindingsField];
                set(getfield(handles,editbox),'String','');
                return
            end
        else
            Windings = setfield(Windings,WindingsField,[]);
        end
    end
elseif strcmp(Tag(1:3),'pup')     % if popupmenu changed
    % popupmenu value
    index = get(hObject,'Value');
    strlist = get(hObject,'String');
    String = strlist{index,1};
    Field = Tag(5:end);
    if isfield(Windings,Field)
        if ~isempty(String)
            Windings = setfield(Windings,Field,String);
            if strcmp(Field,'layoutmethod')
                if strcmp(String,'Automatic')
                    layouterrdlg=1;
                elseif strcmp(String,'From file')
                    Windings.Lsew_inputmethod='Manual'; 
                    Windings.Rs_inputmethod='Manual';
                end
            end
            if strcmp(Field,'Lsew_inputmethod') || strcmp(Field,'Rs_inputmethod')
                if strcmp(String,'Automatic')
                    RsLsewerrdlg=1;
                end
            end
        else
            error('Something goes wrong');
        end
    end
else
    error('Undefined field');
end
Simulation.Windings = Windings;
motoranalysishandles.Simulation = Simulation;
motoranalysishandles.Saved = 0;
guidata(handles.motoranalysis,motoranalysishandles);
UpdateWindingEditor(hObject,layouterrdlg,RsLsewerrdlg);



function NotEditCallback(hObject, eventdata, handles)
if strcmp(get(hObject,'Enable'),'inactive')
    msgbox('Editing of this value is allowed only from Geometry Editor','Winding Editor Message','modal');
end


% --- Executes on button press in pushbutton_redraw.
function pushbutton_redraw_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_redraw (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
redrawwindings(handles);

% --- Executes on selection change in pup_preview.
function pup_preview_Callback(hObject, eventdata, handles)
% hObject    handle to pup_preview (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% Hints: contents = cellstr(get(hObject,'String')) returns pup_preview contents as cell array
%        contents{get(hObject,'Value')} returns selected item from pup_preview
redrawwindings(handles);

% --- Executes when entered data in editable cell(s) in table_layout.
function table_layout_CellEditCallback(hObject, eventdata, handles)
% hObject    handle to table_layout (see GCBO)
% eventdata  structure with the following fields (see UITABLE)
%	Indices: row and column indices of the cell(s) edited
%	PreviousData: previous data for the cell(s) edited
%	EditData: string(s) entered by the user
%	NewData: EditData or its converted form set on the Data property. Empty if Data was not changed
%	Error: error string when failed to convert EditData to appropriate value for Data
% handles    structure with handles and user data (see GUIDATA)

motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Windings = Simulation.Windings;
Geometry = Simulation.Geometry;
layout=Windings.layout;
Row = eventdata.Indices(1);
Col = eventdata.Indices(2);
EditData = eventdata.EditData;
Tag = get(hObject,'Tag');
Ns=Geometry.Ns;
Npp=Windings.Npp;
pass = checklayoutdata(eventdata,Ns,Npp);
if pass
    layout.layout1=layout2num(get(handles.table_layout1,'Data'));
    layout.layout2=layout2num(get(handles.table_layout2,'Data'));
    layout.layout3=layout2num(get(handles.table_layout3,'Data'));
    Windings.layout = layout;
    Simulation.Windings = Windings;
    motoranalysishandles.Simulation = Simulation;
    motoranalysishandles.Saved = 0;
    guidata(handles.motoranalysis,motoranalysishandles);
else
    % set previous value if entered data is not correct
    layoutdata=get(hObject,'Data');
    layoutdata{Row,Col}=eventdata.PreviousData;
    set(hObject,'Data',layoutdata);
end

function numlayout = layout2num(layout)
numlayout=cell(size(layout,1),size(layout,2));
for i=1:size(layout,1)
    for j=1:size(layout,2)
        if ischar(layout{i,j})
            numlayout{i,j}=str2num(layout{i,j});
        else
            numlayout{i,j}=layout{i,j};
        end
    end
end

function [pass] = checklayoutdata(eventdata,Ns,Npp)
pass=1;
Col = eventdata.Indices(2);
Data = eventdata.EditData;
if (Col==2 || Col==3) && isempty(Ns)
    errordlg('Specify number of stator slots first.','Winding Editor Error','modal');
    pass=0;
    return
end
if Col==4 && isempty(Npp)
    errordlg('Specify number of parallel paths first.','Winding Editor Error','modal');
    pass=0;
    return
end
if Col==1
    pass=0;
    return
end
[Data,status]=str2num(Data);
if ~status || ~isreal(Data) || isnan(Data) || isinf(Data) || length(Data)>1 || Data<1 || rem(Data,1)>0
    errordlg('Not a valid value!','Winding Editor Error','modal');
    pass=0;
    return
end
if (Col==2 || Col==3) && Data>Ns
    errordlg('Slot number cannot be larger than number of stator slots.','Winding Editor Error','modal');
    pass=0;
    return
end
if Col==4 && Data>Npp
    errordlg('Parallel path number cannot be larger than total number of parallel paths.','Winding Editor Error','modal');
    pass=0;
    return
end    


function redrawwindings(handles)
motoranalysishandles = guidata(handles.motoranalysis);
Simulation = motoranalysishandles.Simulation;
Windings = Simulation.Windings;
Geometry = Simulation.Geometry;
DXFstator = Simulation.DXFstator;
set(handles.WindingEditor,'Pointer','watch');drawnow;
index=get(getfield(handles,'pup_preview'),'Value');
switch index
    case 1
        preview = 'layout';
    otherwise
        error('Unexpected item in popup menu <pup_preview>: something goes wrong');
end
try
    layout1=Windings.layout.layout1;
    layout2=Windings.layout.layout2;
    layout3=Windings.layout.layout3;
    layout = layoutasonetable(layout1,layout2,layout3,Windings.layoutmethod,Geometry.slotlayertype,Geometry.layerpos,Geometry.Ns);
    Visible = get(handles.WindingEditor,'Visible');
    if strcmp(Visible,'on')
        newplot(handles.axes_windingeditor);
        axes(handles.axes_windingeditor);
        if isfield(DXFstator,'geometry')
            StatorGeometry = DXFstator.geometry;
        else
            StatorGeometry = [];
        end
        geom=initgeom(Geometry,[],StatorGeometry,[],preview,Geometry.dxfstator,layout,DXFstator);
    end
catch
    % incorrect geometry: no preview available
    Visible = get(handles.WindingEditor,'Visible');
    if strcmp(Visible,'on')
        if ishold
            hold off
        end
        newplot(handles.axes_windingeditor);
        axes(handles.axes_windingeditor);
        hold on
        ylim([-10 10]);
        text(0,0,'Incorrect winding layout','FontSize',18,'HorizontalAlignment','center');
        axis equal 
        hold off
    end
end
set(handles.WindingEditor,'Pointer','arrow');drawnow;


function GroupEnable(handles,enable)
ItemList=findobj(get(handles.WindingEditor,'Children'));
for i=1:length(ItemList)
    Tag = get(ItemList(i),'Tag');
    if length(Tag)>3
        if strcmp(Tag(1:4),'edit') || strcmp(Tag(1:3),'pup')
            set(ItemList(i),'Enable',enable);
        end
    end
end


function [cell_layout1, cell_layout2, cell_layout3]=getlayout(Ns,nPolePairs,coilspan,windingtype,nslotlayers,Npp,errdlg,emptylayout)

if isempty(Ns) || Ns<6 || rem(Ns,6/nslotlayers)~=0
    data=cell(10,4);
    for i=1:10
        data{i,1}=i;
    end
    cell_layout1=data; cell_layout2=data; cell_layout3=data;
    if ~isempty(Ns)
        errordlg('Incorrect number of slots or winding layers','Winding layout error','modal');
    end
    return;
else
    data=cell(Ns/(6/nslotlayers),4);
    for i=1:Ns/(6/nslotlayers)
        data{i,1}=i;
    end
    cell_layout1=data; cell_layout2=data; cell_layout3=data;
end
if emptylayout, return; end
if isempty(nPolePairs) || nPolePairs<1
    if errdlg
        errordlg('Incorrect number of pole pairs','Winding layout error','modal');
    end
    return 
end
if isempty(Npp) || Npp>2*nPolePairs || Npp<1
    if errdlg
        errordlg('Incorrect number of parallel paths','Winding layout error','modal');
    end
    return 
end
if rem(Ns,6*nPolePairs)~=0
    if errdlg
        errordlg('Only integer slot winding is supported. Chose ''Manual'' layout input method to define layout manually','Winding layout error','modal');
    end
    return
end
q=Ns/3/(2*nPolePairs);                                                % slots per pole per phase
if nslotlayers==2
    if coilspan<1 || coilspan>Ns/2/nPolePairs
        if errdlg
            errordlg('Incorrect coil span','Winding layout error','modal');
        end
        return
    end
    layout=[];
    layout_=[1:q;
             (1:q)+coilspan];
    if strcmp(windingtype,'Concentric')
        layout_(2,:)=fliplr(layout_(2,:));
    end
    parpath=1;                                                        % number of parallel path
    for i=1:2*nPolePairs
        cor=0*layout_;
        cor(find(layout_>Ns))=Ns;
        layout_=layout_-cor;
        layout=[layout [layout_; ones(1,q)*parpath]];
        layout_=layout_+Ns/2/nPolePairs;
        layout_=layout_([2 1],:);
        parpath=parpath+1;
        if parpath>Npp
            parpath=1;
        end
    end
else
    layout=[];
    layout_=[1:q;
             (1:q)+Ns/2/nPolePairs];
    if strcmp(windingtype,'Concentric')
        layout_(2,:)=fliplr(layout_(2,:));
    end
    parpath=1;                                                        % number of parallel path
    for i=1:nPolePairs
        cor=0*layout_;
        cor(find(layout_>Ns))=Ns;
        layout_=layout_-cor;
        layout=[layout [layout_; ones(1,q)*parpath]];
        layout_=layout_+Ns/nPolePairs;
        parpath=parpath+1;
        if parpath>Npp
            parpath=1;
        end
    end
end
layout1=layout;
layout2=layout;
layout2(1:2,:)=layout2(1:2,:)+q;
layout2=layout2([2 1 3],:);
cor=0*layout2;
cor(find(layout2>Ns))=Ns;
layout2=layout2-cor;
layout3=layout;
layout3(1:2,:)=layout3(1:2,:)+2*q;
cor=0*layout3;
cor(find(layout3>Ns))=Ns;
layout3=layout3-cor;
layout1=layout1';
layout2=layout2';
layout3=layout3';
for i=1:size(layout1,1)
    for j=1:3
        cell_layout1{i,j+1}=layout1(i,j);
        cell_layout2{i,j+1}=layout2(i,j);
        cell_layout3{i,j+1}=layout3(i,j);
    end
end


function SetStatorCircuit(handles,StatorCircuit)
List = get(handles.pup_statorcircuit,'String');
for i=1:length(List)
    if strcmp(StatorCircuit,List(i))
        break;
    elseif i==length(List)  % if thire is no StatorCircuit in the List then add it
        List_ = List;
        List = cell(length(List)+1,1);
        for j=1:length(List_)
            List{j,1}=List_{j,1};
        end
        i = i+1;
        List{i,1} = StatorCircuit;
        set(handles.pup_statorcircuit,'String',List);
        break;
    end
end
set(handles.pup_statorcircuit,'Value',i);
set(handles.pup_statorcircuit,'UserData',i);        % store item index in UserData


% --- Executes on button press in pushbutton_layoutfromfile.
function pushbutton_layoutfromfile_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton_layoutfromfile (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% Allow the user to select a winding layout file
[filename, pathname] = uigetfile( ...
    {'*.txt'}, ...
    'Select a winding layout file');
% If 'Cancel' was selected then return
if isequal([filename,pathname],[0,0])
    return
else
    if ~strcmp(filename(end-2:end),'txt')
        errordlg('Winding layout should be a text file','Winding Editor Error','modal');
        return
    end
    fileID = fopen(filename,'r'); 
    try
        Layout = fscanf(fileID,'%i'); 
        Layout=reshape(Layout,6,length(Layout)/6);
        Layout=Layout';
        if rem(size(Layout,1),3)
            error(' ');
        end
        layout1=Layout(1:size(Layout,1)/3,:);
        layout2=Layout(size(Layout,1)/3+1:2*size(Layout,1)/3,:);
        layout3=Layout(2*size(Layout,1)/3+1:end,:);
        Npp1=max(layout1(:,6)); Npp2=max(layout2(:,6)); Npp3=max(layout3(:,6));
        if Npp1~=Npp2 || Npp2~=Npp3 || Npp1~=Npp3
            error(' ');
        end
        Npp=Npp1;
    catch
        errordlg('Incorrect winding layout file','Winding Editor Error','modal');
        fclose(fileID);
        return
    end
    fclose(fileID);
    cell_layout1=cell(size(layout1));
    cell_layout2=cell(size(layout2));
    cell_layout3=cell(size(layout3));
    for i=1:size(layout1,1)
        for j=1:6
            cell_layout1{i,j}=layout1(i,j);
            cell_layout2{i,j}=layout2(i,j);
            cell_layout3{i,j}=layout3(i,j);
        end
    end
    motoranalysishandles = guidata(handles.motoranalysis);
    Simulation = motoranalysishandles.Simulation;
    Windings = Simulation.Windings;
    Windings.layout.layout1=cell_layout1;
    Windings.layout.layout2=cell_layout2;
    Windings.layout.layout3=cell_layout3;
    Windings.Npp=Npp;
    Simulation.Windings=Windings;
    motoranalysishandles.Simulation=Simulation;
    motoranalysishandles.Saved = 0;
    guidata(handles.motoranalysis,motoranalysishandles);
    UpdateWindingEditor(hObject,0,0);
end


function [Rs, Lsew, WireLength]=GetStatorWinding(Geometry,Mesh,Windings,cell_layout1,cell_layout2,cell_layout3,Ns,D2s,Sds,Hsew,W,slotlayertype,ks,fillfactor,Npp,l,errdlg)
% return stator phase resistance Rs and end turn inductance Lsew
Rs=[]; Lsew=[]; WireLength=[];
layout1=[];
layout2=[];
layout3=[];
if size(cell_layout1,1)~=size(cell_layout2,1) || size(cell_layout2,1)~=size(cell_layout3,1)
    if errdlg
        errordlg('Incorrect winding layout','Winding Editor Error','modal');
    end
    return
end
for i=1:size(cell_layout1,1)
    if isempty(cell_layout1{i,2}) || isempty(cell_layout1{i,3})
        if errdlg
            errordlg('Incorrect winding layout','Winding Editor Error','modal');
        end
        return
    else
        layout1=[layout1 [cell_layout1{i,2}; cell_layout1{i,3}]];
    end
    if isempty(cell_layout2{i,2}) || isempty(cell_layout2{i,3})
        if errdlg
            errordlg('Incorrect winding layout','Winding Editor Error','modal');
        end
        return
    else
        layout2=[layout2 [cell_layout2{i,2}; cell_layout2{i,3}]];
    end
    if isempty(cell_layout3{i,2}) || isempty(cell_layout3{i,3})
        if errdlg
            errordlg('Incorrect winding layout','Winding Editor Error','modal');
        end
        return
    else
        layout3=[layout3 [cell_layout3{i,2}; cell_layout3{i,3}]];
    end    
end
[~, Sss] = initgeom(Geometry,[],[],Mesh,[],Geometry.dxfstator,[]);
nslotlayers=1;
if isempty(Sss)
    e=0;
else
    if strcmp(slotlayertype,'Double layer')
        e=2*sqrt(Sss/pi/2);                                                % end turn bundle diameter
        nslotlayers=2;
    else
        e=2*sqrt(Sss/pi);  
    end
end
[Rs1, Lsew1, WireLength1]=getwinding(layout1,Ns,D2s,Sds,Hsew,e,W,nslotlayers,ks,Sss,fillfactor,Npp,l,Geometry.statorskew);
[Rs2, Lsew2, WireLength2]=getwinding(layout2,Ns,D2s,Sds,Hsew,e,W,nslotlayers,ks,Sss,fillfactor,Npp,l,Geometry.statorskew);
[Rs3, Lsew3, WireLength3]=getwinding(layout3,Ns,D2s,Sds,Hsew,e,W,nslotlayers,ks,Sss,fillfactor,Npp,l,Geometry.statorskew);
if abs(Lsew1-Lsew2)<eps   % Lsew1==Lsew2
    Lsew=Lsew1;
elseif abs(Lsew2-Lsew3)<eps   % Lsew2==Lsew3
    Lsew=Lsew2;
elseif abs(Lsew1-Lsew3)<eps   % Lsew1==Lsew3
    Lsew=Lsew3;    
else
    Lsew=(Lsew1+Lsew2+Lsew3)/3;
    if errdlg
        errordlg('Stator end winding inductance may be incorrect','Winding Editor Error','modal');
    end
end
if Lsew<=0 && strcmp(Windings.Lsew_inputmethod,'Automatic')
    if errdlg
        errordlg('End winding axial overhang is too small for this slot area','Winding Editor Error','modal');
    end
end
if ~isempty(Rs1) && ~isempty(Rs2) && ~isempty(Rs3)
    if abs(Rs1-Rs2)>eps || abs(Rs2-Rs3)>eps
        if errdlg
            errordlg('Unbalanced stator winding','Winding Editor Error','modal');
        end
        return
    end
end
Rs=Rs1;
WireLength=WireLength1+WireLength2+WireLength3;


function [Rs, Lsew, WireLength]=getwinding(layout,Ns,D2s,Sds,Hsew,e,W,nslotlayers,ks,Sss,fillfactor,Npp,l,skew)
EndTurn=[];
WireLength=0;
for i=1:length(layout)    
    endturn=getendturn(layout(1,i),layout(2,i),Ns,D2s,Sds,Hsew,e,W/nslotlayers);
    EndTurn=[EndTurn endturn];
    WireLength=WireLength+endturn.let*W/nslotlayers;
end
slotpitch=(D2s+Sds)*pi/Ns;                 % arc length of slot pitch
Lsew=0;
Rsew=0;

% Lmutij_test=[];
for i=1:length(EndTurn)
    Lsew=Lsew+EndTurn(i).Let;
    if isempty(Sss)
        Rsew=[];
    else
        Rsew=Rsew+EndTurn(i).let*W/nslotlayers*(1/ks)/(Sss*fillfactor/W);
    end
    d=0;
    for j=i+1:length(EndTurn)
        Lmutij=getmutualinductance(EndTurn(i),EndTurn(j),slotpitch,(Hsew-e/2));
        if Lmutij>eps
            if EndTurn(i).clockwise*EndTurn(j).clockwise>0   % end turns have the same direction
                d=d+1;     % distance coefficient (distance between two end turn bundles devided by bundle diameter)
                Lmutij=Lmutij/d;
            end
        end
%         Lmutij_test=[Lmutij_test; [Lmutij d EndTurn(i).slots(1) EndTurn(i).slots(end) EndTurn(j).slots(1) EndTurn(j).slots(end)]];
        Lsew=Lsew+2*Lmutij;
%         disp([Lmutij*10^6 d i j]);
    end
end
Lsew=Lsew/(Npp^2);
if isempty(Sss)
    Rsin=[];
else
    Rsin=Ns/3*(l/cos(skew*pi/180))*W*(1/ks)/(Sss*fillfactor/W);      % stator resistance inside slots
end
Rs=(Rsin+Rsew)/(Npp^2);
WireLength=WireLength+Ns/3*(l/cos(skew*pi/180))*W;


function endturn=getendturn(nslotbeg,nslotret,Ns,D2s,Sds,Hsew,e,N)    
% nslotbeg     start slot
% nslotret     return slot
% Ns
% D2s
% Sds
% nPolePairs
% Hsew             stator end winding axial overhang
% e             
% N             number of conductors 

mu0 = 4*pi*(10.^(-7));     % permeability of free space
if nslotbeg<nslotret
    slots=nslotbeg:nslotret;
    clockwise=1;
    if length(slots)>Ns/2
        slots=[fliplr(1:nslotbeg) fliplr(nslotret:Ns)];
        clockwise=-1;
    end
else
    slots=fliplr(nslotret:nslotbeg);
    clockwise=-1;
    if length(slots)>Ns/2
        slots=[nslotbeg:Ns 1:nslotret];
        clockwise=1;
    end
end
coilspan=length(slots)-1;                                             % end turn span
b=(D2s+Sds)*pi*(coilspan/Ns);                                         % arc length of end turn span
if (Hsew-e/2)<=b/2
    R=(b^2/4+(Hsew-e/2)^2)/2/(Hsew-e/2);                              % end turn radius
    alfa=asin(b/2/R);
    let=2*alfa*R*2;                                                   % end turn length (both end sides)
    Aet=alfa*R^2-b/2*(R-(Hsew-e/2));                                  % end turn contour area 
else   % end turn forms a half of ellipse
    R=(b/2+(Hsew-e/2))/2;
    let=2*pi*R;
    Aet=((b/2)^2+(Hsew-e/2)^2)*pi/4;
end
Let=mu0*let*N^2*log((Hsew-e/2)/(e/2))/2/pi;                           % end turn inductance (both end sides)
endturn.slots=slots;
endturn.clockwise=clockwise;
endturn.b=b;
endturn.R=R;
endturn.let=let;
endturn.Let=Let;
endturn.Aet=Aet;


function Lmut=getmutualinductance(endturn1,endturn2,slotpitch,overhang)

slots1=endturn1.slots;
slots2=endturn2.slots;
if sum(diff(slots1)./abs(diff(slots1)))<0
    slots1=fliplr(slots1);
end
if sum(diff(slots2)./abs(diff(slots2)))<0
    slots2=fliplr(slots2);
end
slotsmut=[];
for i=1:length(slots1)
    if any(slots2==slots1(i))
        slotsmut=[slotsmut slots1(i)];
    end
end
h0=0;
Amut=0;       % mutual area of two end turns
if length(slotsmut)>1
    for i1=1:length(slots1)
        i2=find(slots2==slots1(i1));
        if ~isempty(i2) && slotsmut(end)~=slots2(i2)
            for j=1:10
                d1=slotpitch*(i1-1+(j-1)/10);
                d2=slotpitch*(i2-1+(j-1)/10);
                h1=sqrt(endturn1.R^2-(endturn1.b/2-d1).^2)-(endturn1.R-overhang);
                h2=sqrt(endturn2.R^2-(endturn2.b/2-d2).^2)-(endturn2.R-overhang);
                % h=sqrt(R^2-(b/2-d).^2)-(R-Hsew);
                h=min([h1 h2]);
                if h<-eps
                    disp('getmutualinductance error');
                    error('getmutualinductance error');
                end
                if abs(h)<eps
                    h=0;
                end
                Amut=Amut+(h+h0)/2*slotpitch/10;
                h0=h;
            end
        end
    end
end
Lmut1=endturn1.Let*Amut/endturn1.Aet;
Lmut2=endturn2.Let*Amut/endturn2.Aet;
Lmut=sqrt(Lmut1*Lmut2);
if 2*abs(Lmut1-Lmut2)/(Lmut1+Lmut2)>0.1               % if difference more than 10%
    disp('getmutualinductance error');
    error('getmutualinductance error');
end
Lmut=Lmut*endturn1.clockwise*endturn2.clockwise;


function plot_newwnd_Callback(hObject, eventdata, handles)
% hObject    handle to plot_newwnd (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
%
% Displays contents of axes_geometryeditor in a new figure

% Create a figure to receive this axes' data
axes1fig = figure('Name','Stator winding layout');
% Copy the axes and size it to the figure
axes1copy = copyobj(handles.axes_windingeditor,axes1fig);
set(axes1copy,'Units','Normalized',...
              'Position',[0,0.05,1,0.9]);
          
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

% --- Executes during object creation, after setting all properties.
function table_layout_CreateFcn(hObject, eventdata, handles)
% hObject    handle to table_layout (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% --- Executes during object creation, after setting all properties.
function edit_slotlayertype_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_slotlayertype (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Ns_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Ns (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Npp_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Npp (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Lsew_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Lsew (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_Rs_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Rs (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function pup_statorcircuit_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_statorcircuit (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function edit_W_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_W (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_fillfactor_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_fillfactor (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_ks_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_ks (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function pup_layoutmethod_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_layoutmethod (see GCBO)
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
function edit_coilspan_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_coilspan (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_Hsew_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_Hsew (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_windingtype_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_windingtype (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function table_layout1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to table_layout1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called


% --- Executes during object creation, after setting all properties.
function table_layout2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to table_layout2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called


% --- Executes during object creation, after setting all properties.
function table_layout3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to table_layout3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called


% --- Executes during object creation, after setting all properties.
function pup_Lsew_inputmethod_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_Lsew_inputmethod (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_Rs_inputmethod_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_Rs_inputmethod (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --------------------------------------------------------------------
function plot_WindingLayout_Callback(hObject, eventdata, handles)
% hObject    handle to plot_WindingLayout (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------


% --- Executes during object creation, after setting all properties.
function pup_wiresizemethod_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_wiresizemethod (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function pup_wiresize_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pup_wiresize (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_wirediameter_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_wirediameter (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function edit_nstrands_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit_nstrands (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

"""

def windingeditor(*args, **kwargs):
    """Placeholder for translated MATLAB function."""
    raise NotImplementedError(
        "This function requires manual translation from MATLAB."
    )
