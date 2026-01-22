function DispEfficiencyMap(EfficiencyMap,Pinputmax,Kmechloss,mode,index)


if index==8       % Display efficiency map details
    disp('Efficiency map details:')
    disp(['Advance angle values (el.deg.):   ' num2str(EfficiencyMap.strGamma)]);
    disp(['Maximum RMS phase voltage (V):    ' num2str(EfficiencyMap.Vmax)]);
    disp(['Maximum RMS phase current (A):    ' num2str(EfficiencyMap.Ismax)]);
    disp(['Maximum speed (RPM):              ' num2str(EfficiencyMap.speedmax)]);
    disp(['Torque step (N*m):                ' num2str(EfficiencyMap.torquestep)]);
    disp(['Speed step (RPM):                 ' num2str(EfficiencyMap.speedstep)]);
    disp(['Interpolation method:             ' EfficiencyMap.interpmethod]);
else
    Speed=EfficiencyMap.Speed;
    Torque=EfficiencyMap.Torque;
    Torque=Torque(1:end-5);
    Efficiency_tbl=EfficiencyMap.Struct_tbl.Efficiency_tbl;
    RMSCurrent_tbl=EfficiencyMap.Struct_tbl.RMSCurrent_tbl;
    RMSVoltage_tbl=EfficiencyMap.Struct_tbl.RMSVoltage_tbl;
    InputPower_tbl=EfficiencyMap.Struct_tbl.InputPower_tbl;
    Gamma_tbl=EfficiencyMap.Struct_tbl.Gamma_tbl;
    PowerFactor_tbl=EfficiencyMap.Struct_tbl.PowerFactor_tbl;
    ReactivePower_tbl=EfficiencyMap.Struct_tbl.ReactivePower_tbl;
    Nonconv_tbl=EfficiencyMap.Struct_tbl.Nonconv_tbl;
    Efficiency_tbl=fliplr(Efficiency_tbl');
    RMSCurrent_tbl=fliplr(RMSCurrent_tbl');
    RMSVoltage_tbl=fliplr(RMSVoltage_tbl');
    InputPower_tbl=fliplr(InputPower_tbl');
    Gamma_tbl=fliplr(Gamma_tbl');
    PowerFactor_tbl=fliplr(PowerFactor_tbl');
    ReactivePower_tbl=fliplr(ReactivePower_tbl');
    Nonconv_tbl=fliplr(Nonconv_tbl');
    Speed_tbl=ones(length(Torque),1)*Speed;
    Speed_tbl=Speed_tbl';
    MechLoss=polyval(Kmechloss,Speed_tbl);     % speed in RPM
    if strcmp(mode,'motor')
        InputPower=InputPower_tbl;
        InputPower(InputPower==0)=eps;
        Pmech=Efficiency_tbl.*InputPower/100;
        Efficiency_tbl=100*(Pmech-MechLoss)./InputPower;
    elseif strcmp(mode,'generator')
        Efficiency=Efficiency_tbl;
        Efficiency(Efficiency==0)=eps;
        Pmech=InputPower_tbl./Efficiency*100;
        Pmech(Pmech==0)=eps;
        Efficiency_tbl=100*InputPower_tbl./(Pmech-MechLoss);
    end
    Efficiency_tbl(Efficiency_tbl<0 | Efficiency_tbl>100)=0;
    Efficiency_tbl(abs(InputPower_tbl)>Pinputmax)=NaN;
    RMSCurrent_tbl(abs(InputPower_tbl)>Pinputmax)=NaN;
    RMSVoltage_tbl(abs(InputPower_tbl)>Pinputmax)=NaN;
    InputPower_tbl(abs(InputPower_tbl)>Pinputmax)=NaN;
    Gamma_tbl(abs(InputPower_tbl)>Pinputmax)=NaN;
    PowerFactor_tbl(abs(InputPower_tbl)>Pinputmax)=NaN;
    ReactivePower_tbl(abs(InputPower_tbl)>Pinputmax)=NaN;
    formatstr='%s';
    line_=[];
    for i=1:length(Torque)
        formatstr=[formatstr '%11.3f'];
        line_=[line_ '-----------'];
    end
    if index==1   % Display efficiency table
        disp('Efficiency table (%):');
        Table=Efficiency_tbl;
        prec=2;
    elseif index==2    % Display phase current table
        disp('RMS phase current table (A):');
        Table=RMSCurrent_tbl;
        prec=getprec(Table);
    elseif index==3    % Display phase voltage table
        disp('RMS phase voltage table (V):');
        Table=RMSVoltage_tbl;
        prec=getprec(Table);
    elseif index==4    % Display input power table
        disp('Input power table (kW):');
        Table=InputPower_tbl/1000;
        prec=getprec(Table);
    elseif index==5    % Display power factor table
        disp('Power factor table:');
        Table=PowerFactor_tbl;
        prec=3;    
    elseif index==6    % Display advance angle table
        disp('Advance angle table (electrical degrees):');
        Table=Gamma_tbl;
        GammaValues=str2num(EfficiencyMap.strGamma);
        gammastep=min(diff(GammaValues));
        prec=0;
        while abs((gammastep*10^prec-round(gammastep*10^prec))/(gammastep*10^prec))>0.001
            prec=prec+1;  
        end
    elseif index==7    % Display reactive power table
        disp('Reactive power table (kW):');
        Table=ReactivePower_tbl/1000;
        prec=getprec(Table);       
    end
    disp(sprintf(formatstr,'Torque (N*m) ->   ',Torque));
    disp(['------------------' line_]);
    for i=1:length(Speed)
        formatstr='%9.2f%s';
        str=sprintf(formatstr,Speed(i),'RPM     |');
        for j=1:length(Torque)
            if isnan(Nonconv_tbl(i,j)) || isnan(Table(i,j))
                str=[str blanks(11)];
            else
                if Nonconv_tbl(i,j)
                    str=[str sprintf(['%7.' num2str(prec) 'f%s%i%s'],Table(i,j),'(?',Nonconv_tbl(i,j),')')];
                else
                    str=[str sprintf(['%11.' num2str(prec) 'f'],Table(i,j))];
                end
            end
        end
        disp(str);
    end
end


function prec=getprec(Table)
if max(max(Table))>1000
    prec=1;
elseif max(max(Table))>100
    prec=2;
elseif max(max(Table))>10
    prec=3;
elseif max(max(Table))>1
    prec=4;
elseif max(max(Table))>0.1
    prec=5;
else
    prec=6;
end