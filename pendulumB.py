# Once the CoppeliaSim ChildScripts are working, copy the child script for "Pendulum B" and paste it here.
-- Define global variables here

--base = sim.getObject("Base_A")
motor = sim.getObject("/Elbow_motor_B")
arm = sim.getObject("/Arm_B")
pendulum = sim.getObject("/Pendulum_B")
elbow = sim.getObject("/Elbow_free_B")
wheel = sim.getObject("/wheel_B")

-- You can add variables here as required by your implementation.

function sysCall_init()
    -- Initialize scene objects and algorithm-related variables here
    
    setpoint = math.rad(0)
    Kp = -500
    Ki = -500
    Kd = -350
    
     
end

function sysCall_actuation()
    -- Implement actuation code here
    -- Calculate control signal using a PID controller and apply it to the actuator joint
    currentAngle = sim.getJointPosition(elbow)
    --omega_not=0
    lastError = 0
    integral = 0
    error = setpoint - currentAngle
    integral = integral + error
    derivative = error - lastError
    lastError = error
    controlSignal = Kp * error + Ki * integral + Kd * derivative
    sim.setJointTargetVelocity(motor,controlSignal)
    --omega=sim.getJointTargetVelocity(motor)
    --omega_not=omega
    
    
    print("error")
    print(error)
    print("control")
    print(controlSignal)
    
end

function sysCall_sensing()
    -- Implement sensing code here
    -- Calculate errors and feedback
    
end

function sysCall_cleanup()
    -- Implement any required cleanup here
end
