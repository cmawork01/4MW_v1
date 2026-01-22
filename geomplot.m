function geomplot(h,g,color)

% 1  type: 1-circle; 2-line
% 2  x_start  
% 3  x_end  
% 4  y_start  
% 5  y_end  
% 6  left_sdm  
% 7  right_sdm  
% 8  x_cen 
% 9  y_cen 
% 10 radius

X=[]; Y=[];
for i=1:size(g,2)
    coli=g(:,i);
    if coli(1)==2    % line
        x=coli(2:3)';
        y=coli(4:5)';
        X=[X x]; Y=[Y y];
    elseif coli(1)==1    % circle
        ang1=atan2(coli(4)-coli(9),coli(2)-coli(8));
        ang2=atan2(coli(5)-coli(9),coli(3)-coli(8));
        if ang1<0
            ang1=ang1+2*pi;
        end
        if ang2<0
            ang2=ang2+2*pi;
        end        
        if ang2>ang1
            n=round((ang2-ang1)/(2*pi)*5000);
            t=linspace(ang1,ang2,n);
        else % ang2<ang1
            n=round((2*pi-(ang1-ang2))/(2*pi)*1000);
            t=linspace(ang1,ang2+2*pi,n);
            t(t>2*pi)=t(t>2*pi)-2*pi;
        end
        x=coli(10)*cos(t)+coli(8); 
        y=coli(10)*sin(t)+coli(9);
        X=[X x]; Y=[Y y];
    end
    X=[X NaN]; Y=[Y NaN];
end
if exist('color','var')
    plot(h,X,Y,'Color',color);axis(h,'equal');
else
    plot(h,X,Y);axis(h,'equal');
end

