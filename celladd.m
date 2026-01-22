function CellArray = celladd(CellArray,addon,maxsize)

if exist('maxsize','var')
    if maxsize==length(CellArray)
        CellArray_=cell(length(CellArray)-1,1);
        for i=2:length(CellArray)
            CellArray_{i-1,1}=CellArray{i,1};
        end
        CellArray=CellArray_;
    end
end

CellArray_=cell(length(CellArray)+1,1);
for i=1:length(CellArray)
    CellArray_{i,1}=CellArray{i,1};
end
CellArray_{end,1}=addon;
CellArray=CellArray_;