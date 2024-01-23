import matplotlib.pyplot as plt
from space_base import GravBody, Probe
from numpy import max, argmax

def projectile(t, posvel):
    current_gravity = gravity
    return posvel[1], -current_gravity


# Constants
G = 6.67e-11  # Gravitational constant
earth = GravBody.earth()  # Earth as an object with mass and radius
gravity = 9.81  # simple gravity
print(f"Gravity: {gravity}")

# Initial Conditions
x0 = 0  # start position
vx0 = 850  # start speed
t_final = (2*vx0) / gravity  # time of trajectory given
t_num = 1400  # number of steps in trajectory

# Running Solver
probe = Probe(projectile, t_final, t_num, x0=x0, vx0=vx0, event=0)  # probe as an object
in_energy = 0.5 * probe.mass * probe.posvel0[1] ** 2 + probe.mass * gravity * x0  # initial energy
t, posvel = probe.odesolve()  # solve the differential equations

# Solver Results
t_end = len(t) - 1  # last value of array
fin_energy = 0.5 * probe.mass * posvel[t_end][1] ** 2 + probe.mass * gravity * posvel[t_end][0]  # final energy
max_height = max(posvel, axis=0)[0]
print(f"Flight time: {t_final}")
print(f"Max height: {max_height}")
accuracy = (fin_energy - in_energy) / in_energy  # accuracy of solver
print(f'Accuracy is {accuracy}')


def projectile_with_gravity(t, posvel):
    current_gravity = G * earth.mass / (earth.radius + posvel[0])**2
    return posvel[1], -current_gravity

# Initial Conditions
x0 = 0  # start position
vx0 = 850  # start speed
t_final = 100 # time of trajectory given
t_num = 1400  # number of steps in trajectory

last_altitude = 1
while last_altitude > 0:
    # Running Solver
    probe = Probe(projectile_with_gravity, t_final, t_num, x0=x0, vx0=vx0, event=0)  # probe as an object
    in_energy = 0.5 * probe.mass * probe.posvel0[1] ** 2 - G * earth.mass * probe.mass  / (earth.radius + x0)  # initial energy
    t, posvel = probe.odesolve()  # solve the differential equations
    t_final += 100
    last_altitude = posvel[len(t) - 1][0]

# Solver Results
t_end = len(t) - 1  # last value of array
fin_energy = 0.5 * probe.mass * posvel[t_end][1] ** 2 - G * earth.mass * probe.mass  / (earth.radius + posvel[t_end][0])  # final energy
max_height_with_gravity = max(posvel, axis=0)[0]
t_final_index = argmax(posvel[1:, 0]<=0)
t_final = t[t_final_index]
print(f"Flight time: {t_final}")
print(f"Max height: {max_height_with_gravity}")
diff = max_height_with_gravity - max_height
print(f"Diff between: {diff}")
accuracy = (fin_energy - in_energy) / in_energy  # accuracy of solver
print(f'Accuracy is {accuracy}')

# Plotting
plt.figure(figsize=(8, 5))  # create figure, figsize can be changed as preferred
plt.plot(t, posvel[:, 0])  # plot time against height
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.show()  # make plot appear
