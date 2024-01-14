#python
reference_frame = None
spherical_joint = None
body = None
front_motor = None
T = 0
yaw_setpoint=3
drive_speed = 0

prev_alpha = 0
prev_theta = 0
dt = 0.01

def sysCall_init():
    global reference_frame,spherical_joint,body,front_motor,drive_motor,yaw_setpoint
    front_motor = sim.getObject(".")
    drive_motor= sim.getObject("/drive_motor")
    body = sim.getObjectParent(front_motor)
    spherical_joint = sim.getObjectParent(body)
    reference_frame = sim.getObjectParent(spherical_joint)
    
    #sim.setJointMode(19, sim.jointdynctrl_force)
    
    '''print(front_motor)
    print(body)
    print(spherical_joint)
    print(reference_frame)'''
    pass

def sysCall_actuation():
    global prev_alpha,prev_theta
    
    orientation = sim.getObjectOrientation(reference_frame,body)
    theta = orientation[1]
    alpha = orientation[2]
    
    alpha_dot = (alpha-prev_alpha)/dt
    theta_dot = (theta-prev_theta)/dt
    
    prev_alpha = alpha
    prev_theta = theta
    
    #print(f"alpha_dot:{alpha_dot:.2f}  alpha:{alpha:.2f} theta_dot:{theta_dot:.2f}   theta:{theta:.2f}")
    
    k = [  23.20401403,   10.        ,   -7.24808332, -190.08161271]
    
    # Torque
    T = +k[0]*alpha_dot + k[1]*(alpha+yaw_setpoint) + k[2]*theta_dot + k[3]*theta;
    #print(T)
    sim.setJointTargetVelocity(front_motor, T)
    
    pass

def sysCall_sensing():
    
    ############### Keyboard Input ##############
    message,data,data2 = sim.getSimulatorMessage()
    global drive_speed
    if (message == sim.message_keypress):
        
        if (data[0]==2007): # forward up arrow
            drive_speed = 10 #add drive wheel speed here
        
        if (data[0]==2008): # backward down arrow
            drive_speed = -10#add drive wheel speed here
        
        if (data[0]==2009): # left arrow key
            yaw_setpoint = 3#change yaw_setpoint for required turning over here
        
        if (data[0]==2010): # right arrow key
            yaw_setpoint = -3#change yaw_setpoint for required turning over here
    else:
        drive_speed = 0 # This is an example, decide what's best
        yaw_setpoint = 0 # # This is an example, decide what's best
    #########################################
    yaw_setpoint = sim.getFloatSignal("yaw_setpoint")
    sim.setJointTargetVelocity(drive_motor, drive_speed)
    #print(sim.getJointTargetVelocity(drive_motor))
    
    pass

def sysCall_cleanup():
    # do some clean-up here
    pass

# See the user manual or the available code snippets for additional callback functions and detailsw