function [nper, periodicity] = VerifyPerBndCnd(Ns,nPolePairs,perbndcnd)
% verify periodic/antiperiodic boundary conditions

nper=[]; periodicity=[];
if strcmp(perbndcnd,'Periodic') || strcmp(perbndcnd,'Antiperiodic')
    if isempty(nPolePairs)
        errordlg('To use periodic/antiperiodic boundary conditions you should specify periodicity factor (number of pole pairs)','Mesh Editor Message','modal');
        return
    elseif isempty(Ns)
        errordlg('To use periodic/antiperiodic boundary conditions you should specify number of stator slots','Mesh Editor Message','modal');
        return                                        
    elseif strcmp(perbndcnd,'Periodic')
        if rem(Ns,nPolePairs)
            errordlg('Periodic boundary conditions are not allowed for this combination of number of stator slots and number of pole pairs','Mesh Editor Message','modal');
            return    
        end

        nper=nPolePairs; periodicity=1;
    elseif strcmp(perbndcnd,'Antiperiodic')
        if rem(Ns,2*nPolePairs)
            errordlg('Antiperiodic boundary conditions are not allowed for this combination of number of stator slots and number of pole pairs','Mesh Editor Message','modal');
            return    
        end

        nper=2*nPolePairs; periodicity=-1;
    end
elseif strcmp(perbndcnd,'None')
    nper=1; periodicity=1;
else
    error('Undefined type of boundary conditions');
end


