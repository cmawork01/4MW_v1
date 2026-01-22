function [Pinput, Pcons, Ps, Pr, Pmf, Pmech]=PowerBalance(delta_t,Circuit,dWmf,torque,speed)
% Power balance

[Pinput, Ps, Pr]=CircuitGetPower(Circuit);
Pmf=dWmf/delta_t;
Pmech=torque*speed;
Pcons=Ps+Pr+Pmf+Pmech;











