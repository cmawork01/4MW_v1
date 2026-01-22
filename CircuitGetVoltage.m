function V = CircuitGetVoltage(Circuit,node1,node2)
% return voltage between node1 and node2

Phi=Circuit.Phi;
if node1==0
    V=-Phi(node2);
elseif node2==0
    V=Phi(node1);
else
    V=Phi(node1)-Phi(node2);
end