function str = timestr(time)
    % dd:hh:mm:ss
    dd=floor(time/(24*60*60));
    time=rem(time,(24*60*60));
    hh=floor(time/(60*60));
    time=rem(time,(60*60));
    mm=floor(time/60);
    time=rem(time,60);
    ss=floor(time);
    dd=num2str(dd);
    hh=num2str(hh,'%02d');
    mm=num2str(mm,'%02d');
    ss=num2str(ss,'%02d');
    str=[dd ':' hh ':' mm ':' ss];
end
