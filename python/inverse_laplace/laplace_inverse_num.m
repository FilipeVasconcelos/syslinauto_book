## Copyright (C) 2019 Filipe Vasconcelos

pkg load control
clf;
clear;
s = tf('s');
g = 1/(2*s^2+3*s+4);
[y,t,x]=step(g,30,0.02)

plot(t,y)
title ("Step response of a PT2 transfer function");

format long
file_id = fopen('mydata.txt', 'w');
fdisp(file_id, y)
fclose(file_id)
