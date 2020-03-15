% by jake suddreth
warning('off');
clc;
% time-step 
time = 0:0.0000001:30;
% constants 
G = 6.674 * (10^-11); % N*m^2/kg^2
m1 = 1; % kg
m2 = 1; % kg
% r-double-dot equation
f = @(t, n) [n(2); (G*m1*m2)/(n(1)^2) - (n(1)*(n(4)^2)); n(4); (-2*n(2)*n(4))/n(1)];
% initial conditions
IC = [500, 0, 0, 100];
% solve using ode45
[t, n] = ode45(f, time, IC);
% polar coordinates
r = n(:,1);
theta = n(:,3);
% cartesian coordinates
x = r.*cos(theta);
y = r.*sin(theta);
% write to files
x_file = fopen('x_values.txt', 'w');
fprintf(x_file, '%12.16f\n', x);
fclose(x_file);
y_file = fopen('y_values.txt', 'w');
fprintf(y_file, '%12.16f\n', y);
fclose(y_file);