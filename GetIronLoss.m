function [arr_ironloss, arr_ironloss_hyst, arr_ironloss_eddy] = GetIronLoss(material,f1,Bm)

arr_ironloss=0; arr_ironloss_hyst=0; arr_ironloss_eddy=0;
Steinmetz=material.ironloss;
if isempty(Steinmetz)
    return
end
Kh=Steinmetz.Kh;
alfa=Steinmetz.alfa;
beta=Steinmetz.beta;
Ke=Steinmetz.Ke;
arr_ironloss=Kh*(f1^alfa)*(Bm.^beta)+Ke*(f1*Bm).^2;
arr_ironloss_hyst=Kh*(f1^alfa)*(Bm.^beta);     % hysteresis loss
arr_ironloss_eddy=Ke*(f1*Bm).^2;               % eddy current loss