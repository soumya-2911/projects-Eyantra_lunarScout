# Once the CoppeliaSim ChildScripts are working, copy the child script for "Pendulum A" and paste it here.
-- Define global variables here

--base = sim.getObject("Base_A")
motor = sim.getObject("/Motor_A")
arm = sim.getObject("/Arm_A")
pendulum = sim.getObject("/Pendulum_A")
elbow = sim.getObject("/Elbow_A")

-- You can add variables here as required by your implementation.

function sysCall_init()
    -- Initialize scene objects and algorithm-related variables here
    
    setpoint = math.rad(0)
    Kp = -20.0
    Ki = -0.01
    Kd = -0.06
    --m=sim.computeMassAndInertia(motor,)
    
    
end

function sysCall_actuation()
    -- Implement actuation code here
    -- Calculate control signal using a PID controller and apply it to the actuator joint
    currentAngle = sim.getJointPosition(elbow)
    lastError = 0
    integral = 0
    error = setpoint - currentAngle
    integral = integral + error
    derivative = error - lastError
    lastError = error
    controlSignal = Kp * error + Ki * integral + Kd * derivative
    sim.setJointTargetForce(motor,controlSignal)
    
    
    
    
    --print(controlSignal)
    
end

function sysCall_sensing()
    -- Implement sensing code here
    -- Calculate errors and feedback
    
end

function sysCall_cleanup()
    -- Implement any required cleanup here
end