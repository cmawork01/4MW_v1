function PlotEfficiencyMap(EfficiencyMap,Pinput_max,Kmechloss,mode)

Speed=EfficiencyMap.Speed;
BorderTorque=EfficiencyMap.BorderTorque;
BorderInputPower=EfficiencyMap.BorderInputPower;
Struct_plot=EfficiencyMap.Struct_plot;
Speed_plot=Struct_plot.Speed_plot;
Torque_plot=Struct_plot.Torque_plot;
Efficiency_plot=Struct_plot.Efficiency_plot;
RMSCurrent_plot=Struct_plot.RMSCurrent_plot;
RMSVoltage_plot=Struct_plot.RMSVoltage_plot;
InputPower_plot=Struct_plot.InputPower_plot;
Gamma_plot=Struct_plot.Gamma_plot;
PowerFactor_plot=Struct_plot.PowerFactor_plot;
ReactivePower_plot=Struct_plot.ReactivePower_plot;
Ismax=EfficiencyMap.Ismax;
Vmax=EfficiencyMap.Vmax;
speedmax=EfficiencyMap.speedmax;

figure('Name',['Efficiency Map (Max RMS phase voltage ' num2str(Vmax) 'V, Max RMS phase current ' num2str(Ismax) 'A, ' mode 'mode)']); 
hold on
% MechLoss=polyval(Kmechloss,Speed_plot*2*pi/60);
MechLoss=polyval(Kmechloss,Speed_plot);          % speed in RPM
InputPower_plot(InputPower_plot==0)=eps;
if strcmp(mode,'motor')
    Pmech=Efficiency_plot.*InputPower_plot/100;
    Efficiency_plot=100*(Pmech-MechLoss)./InputPower_plot;
    Ylim=[0 1.1*max(BorderTorque)];
elseif strcmp(mode,'generator')
    Efficiency_plot(Efficiency_plot==0)=eps;
    Pmech=InputPower_plot./Efficiency_plot*100;
    Pmech(Pmech==0)=eps;
    Efficiency_plot=100*InputPower_plot./(Pmech-MechLoss);
    Ylim=[1.1*min(BorderTorque) 0];
end
Efficiency_plot((Struct_plot.Efficiency_plot>0 & Struct_plot.Efficiency_plot<100) & (Efficiency_plot<0 | Efficiency_plot>100))=0;

Efficiency_int=[];
RMSCurrent_int=[];
RMSVoltage_int=[];
InputPower_int=[];
Gamma_int=[];
PowerFactor_int=[];
ReactivePower_int=[];
Speed_int=[];
Torque_int=[];
for i=1:size(Efficiency_plot,1)
    Efficiency_int=[Efficiency_int Efficiency_plot(i,~isnan(Efficiency_plot(i,:)))];
    RMSCurrent_int=[RMSCurrent_int RMSCurrent_plot(i,~isnan(Efficiency_plot(i,:)))];
    RMSVoltage_int=[RMSVoltage_int RMSVoltage_plot(i,~isnan(Efficiency_plot(i,:)))];
    InputPower_int=[InputPower_int InputPower_plot(i,~isnan(Efficiency_plot(i,:)))];
    Gamma_int=[Gamma_int Gamma_plot(i,~isnan(Efficiency_plot(i,:)))];
    PowerFactor_int=[PowerFactor_int PowerFactor_plot(i,~isnan(Efficiency_plot(i,:)))];
    ReactivePower_int=[ReactivePower_int ReactivePower_plot(i,~isnan(Efficiency_plot(i,:)))];
    Speed_int=[Speed_int Speed_plot(i,~isnan(Efficiency_plot(i,:)))];
    Torque_int=[Torque_int Torque_plot(i,~isnan(Efficiency_plot(i,:)))];
end
nspeed=1000;
ntorque=1000;
Speed_q=linspace(Speed_plot(1,1),Speed_plot(end,end),nspeed);
Speed_q=ones(ntorque,1)*Speed_q;
Speed_q=Speed_q';
Torque_q=linspace(Torque_plot(1,1),Torque_plot(end,end),ntorque);
Torque_q=ones(nspeed,1)*Torque_q;
Torque_plot=Torque_q;
Speed_plot=Speed_q;
Efficiency_plot = griddata(Speed_int,Torque_int,Efficiency_int,Speed_plot,Torque_plot);
RMSCurrent_plot = griddata(Speed_int,Torque_int,RMSCurrent_int,Speed_plot,Torque_plot);
RMSVoltage_plot = griddata(Speed_int,Torque_int,RMSVoltage_int,Speed_plot,Torque_plot);
InputPower_plot = griddata(Speed_int,Torque_int,InputPower_int,Speed_plot,Torque_plot);
Gamma_plot = griddata(Speed_int,Torque_int,Gamma_int,Speed_plot,Torque_plot);
PowerFactor_plot = griddata(Speed_int,Torque_int,PowerFactor_int,Speed_plot,Torque_plot);
ReactivePower_plot = griddata(Speed_int,Torque_int,ReactivePower_int,Speed_plot,Torque_plot);
RMSCurrent_plot(Efficiency_plot<0 | Efficiency_plot>100)=NaN;
RMSVoltage_plot(Efficiency_plot<0 | Efficiency_plot>100)=NaN;

if any(any(abs(InputPower_plot)>Pinput_max))
    PowerLimitPatch=contourf(Speed_plot,Torque_plot,abs(InputPower_plot),[0 Pinput_max]);
%     PowerLimitPatch(:,1:PowerLimitPatch(2,1)+2)=[];
    PowerLimitPatch=PowerLimitPatch(:,2:PowerLimitPatch(2,1)+1);
    PowerLimitPatch(:,isnan(PowerLimitPatch(1,:)))=[];
    cla; 
else
    PowerLimitPatch=[];
end

InputPower_plot(Efficiency_plot<0 | Efficiency_plot>100)=NaN;
Gamma_plot(Efficiency_plot<0 | Efficiency_plot>100)=NaN;
PowerFactor_plot(Efficiency_plot<0 | Efficiency_plot>100)=NaN;
ReactivePower_plot(Efficiency_plot<0 | Efficiency_plot>100)=NaN;
Efficiency_plot(Efficiency_plot<0 | Efficiency_plot>100)=NaN;

colormap jet
cntrs=1:round(max(max(Efficiency_plot)));
[C,h]=contourf(Speed_plot,Torque_plot,Efficiency_plot,cntrs);colorbar;caxis([0 100])
clabel(C,h); xlabel('Speed, RPM'); ylabel('Torque, N*m'); title('Efficiency, %')
set(gcf,'renderer','zbuffer');
if ~isempty(PowerLimitPatch)
    patch([PowerLimitPatch(1,:) max(PowerLimitPatch(1,:))],[PowerLimitPatch(2,:) max(PowerLimitPatch(2,:))],1*ones(1,length(PowerLimitPatch)+1),[1 1 1]);
end
if strcmp(mode,'motor')
    patch([Speed Speed(end) Speed(1)],[BorderTorque 1.1*max(BorderTorque) 1.1*max(BorderTorque)],2*ones(1,length(BorderTorque)+2),[1 1 1]); 
elseif strcmp(mode,'generator')
    patch([Speed Speed(end) Speed(1)],[BorderTorque 1.1*min(BorderTorque) 1.1*min(BorderTorque)],2*ones(1,length(BorderTorque)+2),[1 1 1]);
end
ylim(Ylim); 
hold off
figure('Name','Optimum Phase Current Map'); hold on
colormap jet
contourf(Speed_plot,Torque_plot,RMSCurrent_plot,20);colorbar;caxis([0 Ismax]); xlabel('Speed, RPM'); ylabel('Torque, N*m'); title('RMS phase current, A')
set(gcf,'renderer','zbuffer');
if ~isempty(PowerLimitPatch)
    patch([PowerLimitPatch(1,:) max(PowerLimitPatch(1,:))],[PowerLimitPatch(2,:) max(PowerLimitPatch(2,:))],1*ones(1,length(PowerLimitPatch)+1),[1 1 1]);
end
if strcmp(mode,'motor')
    patch([Speed Speed(end) Speed(1)],[BorderTorque 1.1*max(BorderTorque) 1.1*max(BorderTorque)],2*ones(1,length(BorderTorque)+2),[1 1 1]); 
elseif strcmp(mode,'generator')
    patch([Speed Speed(end) Speed(1)],[BorderTorque 1.1*min(BorderTorque) 1.1*min(BorderTorque)],2*ones(1,length(BorderTorque)+2),[1 1 1]);
end
ylim(Ylim); 
hold off
figure('Name','Optimum Phase Voltage Map'); hold on
colormap jet
contourf(Speed_plot,Torque_plot,RMSVoltage_plot,20);colorbar;caxis([0 Vmax]); xlabel('Speed, RPM'); ylabel('Torque, N*m'); title('RMS phase voltage, V')
set(gcf,'renderer','zbuffer');
if ~isempty(PowerLimitPatch)
    patch([PowerLimitPatch(1,:) max(PowerLimitPatch(1,:))],[PowerLimitPatch(2,:) max(PowerLimitPatch(2,:))],1*ones(1,length(PowerLimitPatch)+1),[1 1 1]);
end
if strcmp(mode,'motor')
    patch([Speed Speed(end) Speed(1)],[BorderTorque 1.1*max(BorderTorque) 1.1*max(BorderTorque)],2*ones(1,length(BorderTorque)+2),[1 1 1]); 
elseif strcmp(mode,'generator')
    patch([Speed Speed(end) Speed(1)],[BorderTorque 1.1*min(BorderTorque) 1.1*min(BorderTorque)],2*ones(1,length(BorderTorque)+2),[1 1 1]);
end
ylim(Ylim); 
hold off
figure('Name','Input Power Map'); hold on
colormap jet
contourf(Speed_plot,Torque_plot,InputPower_plot/1000,20);colorbar; xlabel('Speed, RPM'); ylabel('Torque, N*m'); title('Input power, kW'); %caxis([0 3*Vmax*Ismax/1000])
set(gcf,'renderer','zbuffer');
if ~isempty(PowerLimitPatch)
    patch([PowerLimitPatch(1,:) max(PowerLimitPatch(1,:))],[PowerLimitPatch(2,:) max(PowerLimitPatch(2,:))],1*ones(1,length(PowerLimitPatch)+1),[1 1 1]);
end
if strcmp(mode,'motor')
    patch([Speed Speed(end) Speed(1)],[BorderTorque 1.1*max(BorderTorque) 1.1*max(BorderTorque)],2*ones(1,length(BorderTorque)+2),[1 1 1]); 
elseif strcmp(mode,'generator')
    patch([Speed Speed(end) Speed(1)],[BorderTorque 1.1*min(BorderTorque) 1.1*min(BorderTorque)],2*ones(1,length(BorderTorque)+2),[1 1 1]);
end
ylim(Ylim); 
hold off
figure('Name','Optimum Advance Angle Map'); hold on
colormap jet
contourf(Speed_plot,Torque_plot,Gamma_plot,20);colorbar; xlabel('Speed, RPM'); ylabel('Torque, N*m'); title('Advance angle, electrical degrees');
set(gcf,'renderer','zbuffer');
if ~isempty(PowerLimitPatch)
    patch([PowerLimitPatch(1,:) max(PowerLimitPatch(1,:))],[PowerLimitPatch(2,:) max(PowerLimitPatch(2,:))],1*ones(1,length(PowerLimitPatch)+1),[1 1 1]);
end
if strcmp(mode,'motor')
    patch([Speed Speed(end) Speed(1)],[BorderTorque 1.1*max(BorderTorque) 1.1*max(BorderTorque)],2*ones(1,length(BorderTorque)+2),[1 1 1]); 
elseif strcmp(mode,'generator')
    patch([Speed Speed(end) Speed(1)],[BorderTorque 1.1*min(BorderTorque) 1.1*min(BorderTorque)],2*ones(1,length(BorderTorque)+2),[1 1 1]);
end
ylim(Ylim); 
hold off
figure('Name','Power Factor Map'); hold on
colormap jet
contourf(Speed_plot,Torque_plot,PowerFactor_plot,20);colorbar;caxis([min(min(PowerFactor_plot)) 1]); xlabel('Speed, RPM'); ylabel('Torque, N*m'); title('Power factor')
set(gcf,'renderer','zbuffer');
if ~isempty(PowerLimitPatch)
    patch([PowerLimitPatch(1,:) max(PowerLimitPatch(1,:))],[PowerLimitPatch(2,:) max(PowerLimitPatch(2,:))],1*ones(1,length(PowerLimitPatch)+1),[1 1 1]);
end
if strcmp(mode,'motor')
    patch([Speed Speed(end) Speed(1)],[BorderTorque 1.1*max(BorderTorque) 1.1*max(BorderTorque)],2*ones(1,length(BorderTorque)+2),[1 1 1]); 
elseif strcmp(mode,'generator')
    patch([Speed Speed(end) Speed(1)],[BorderTorque 1.1*min(BorderTorque) 1.1*min(BorderTorque)],2*ones(1,length(BorderTorque)+2),[1 1 1]);
end
ylim(Ylim); 
hold off
figure('Name','Reactive Power Map'); hold on
colormap jet
contourf(Speed_plot,Torque_plot,ReactivePower_plot/1000,20);colorbar; xlabel('Speed, RPM'); ylabel('Torque, N*m'); title('Reactive Power, kvar');
set(gcf,'renderer','zbuffer');
if ~isempty(PowerLimitPatch)
    patch([PowerLimitPatch(1,:) max(PowerLimitPatch(1,:))],[PowerLimitPatch(2,:) max(PowerLimitPatch(2,:))],1*ones(1,length(PowerLimitPatch)+1),[1 1 1]);
end
if strcmp(mode,'motor')
    patch([Speed Speed(end) Speed(1)],[BorderTorque 1.1*max(BorderTorque) 1.1*max(BorderTorque)],2*ones(1,length(BorderTorque)+2),[1 1 1]); 
elseif strcmp(mode,'generator')
    patch([Speed Speed(end) Speed(1)],[BorderTorque 1.1*min(BorderTorque) 1.1*min(BorderTorque)],2*ones(1,length(BorderTorque)+2),[1 1 1]);
end
ylim(Ylim); 
hold off
if strcmp(mode,'motor')
    BorderInputPower(BorderInputPower>Pinput_max)=Pinput_max;
elseif strcmp(mode,'generator')
    BorderInputPower(abs(BorderInputPower)>Pinput_max)=-Pinput_max;
end
figure('Name',['Input Power Envelope (' mode ' mode)']);plot(Speed,BorderInputPower/1000);grid; xlabel('Speed, RPM'); ylabel('Input power, kW')

