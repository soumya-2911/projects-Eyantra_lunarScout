% Pendulum parameters
L = 1;          % Length of the pendulum
g = 9.81;       % Acceleration due to gravity
theta0 = pi/4;  % Initial angle (45 degrees)
tspan = [0 10]; % Time span for simulation

% Define the time vector
t = linspace(tspan(1), tspan(2), 200);

% Initialize arrays to store pendulum positions
theta = zeros(size(t));
theta(1)=theta0;
theta_dot = zeros(size(t));


%x = zeros(size(t));

% Simulate the pendulum motion
for i = 1:length(t)
    % Calculate angular acceleration
    alpha = -g/L * sin(theta(i));
    
    % Update angular velocity and angle using Euler's method
    if i < length(t)
        dt = t(i+1) - t(i);
        theta_dot(i+1) = theta_dot(i) + dt * (alpha); % Semi-implicit Euler
        theta(i+1) = theta(i) + dt * (theta_dot(i));
        
    end
    
    % Calculate x and y positions of the pendulum bob
    %x(i) = L * sin(theta(i));
end

% Create an animation
%figure;
for i = 1:length(t)
    % Plot the pendulum
    plot([0, L * sin(theta(i))], [0, -L * cos(theta(i))], 'b', 'LineWidth', 2);
    axis([-1.2*L 1.2*L -1.2*L 0.2*L]); % Set axis limits
    xlabel('X-axis');
    ylabel('Y-axis');
    title('Simple Pendulum Animation');
    grid on;
    
    % Pause to control the animation speed
    pause(0.01);
    
    % Clear the current plot to update the animation
    if i < length(t)
        clf;
    end
end
