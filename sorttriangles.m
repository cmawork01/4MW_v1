function tbyp = sorttriangles(p,t)

tbyp=[];
for i=1:size(p,2)
    tinds=[find(t(1,:)==i) find(t(2,:)==i) find(t(3,:)==i)];
    if isempty(tinds)
        tinds=0;
    else
        tinds=sort(tinds);
        tinds=tinds([find(diff(tinds)) length(tinds)]);
    end
    if size(tbyp,2)<length(tinds)
        tbyp=[tbyp zeros(size(tbyp,1),length(tinds)-size(tbyp,2))];
    elseif length(tinds)<size(tbyp,2)
        tinds=[tinds zeros(1,size(tbyp,2)-length(tinds))];
    end
    tbyp=[tbyp;
          tinds];
end


