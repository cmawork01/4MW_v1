function Value=ReadMaterialData(type,materialname,property)

Value=[];
if strcmp(materialname,'Not assigned')
    return
end
switch type
    case 'Conductor'
        filepath='Materials\Conductor\';
    case 'Iron'
        filepath='Materials\Iron\';
    case 'Magnet'
        filepath='Materials\Magnet\';
    otherwise
        error('Undefined material type')
end
fid = fopen([filepath materialname '.txt']);
if fid<0
    error([filepath materialname '.txt is not found.']);
%     errordlg(['Material ' MaterialsFieldValue ' is not found in Materials Library.'],'Materials Error','modal');
%     return
end
allData = textscan(fid,'%s','Delimiter','\n');
allData=allData{1};
reading=0;
for i=1:length(allData)
    txtLine=allData{i};
    if ~isempty(txtLine)
        icomment=strfind(txtLine, '%');
        if icomment
            icomment=icomment(1);
            txtLine=txtLine(1:icomment-1);
        end
        txtLine=strtrim(txtLine);
        if reading
            if ~isempty(txtLine)
                if strcmp(txtLine(1),'<')
                    break
                end
                [value, status]=str2num(txtLine);
                if ~status
                    error(['Error reading line ' num2str(i) ' from ' filepath materialname '.txt'])
                end
                try
                    Value=[Value; value];
                catch
                    error(['Error reading line ' num2str(i) ' from ' filepath materialname '.txt'])
                end
            end
        end
        if ~reading
            if strfind(txtLine, property)
                reading=1;
            end
        end
    end
end
fclose(fid);
% if ~reading
%     error(['Property ' property ' is not found'])
% end




