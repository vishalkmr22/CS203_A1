import matplotlib.pyplot as plt
import random
import math

#Plots point 
def points_plotter(points_in,points_out):
    fig, axis = plt.subplots()
    axis.set_aspect("equal", adjustable="box")
    circle = plt.Circle((0, 0),1,fill=False,color="r")
    axis.add_artist(circle)
    in_x, in_y = zip(*points_in)
    out_x, out_y = zip(*points_out)
    plt.scatter(in_x, in_y, color='y', label="Points inside circle of radius 0.5")  #inside points are yellow coloured
    plt.scatter(out_x, out_y, color='g', label="Points outside circle of radius 0.5")  #outside points are blue coloured
    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.title("chords\' midpoint")  #Plot's title
    plt.xlabel("x-coordinate")
    plt.ylabel("y-coordinate")
    plt.legend()

    plt.show()

#Plots chord
def chords_plotter(selected_chords, plot_title):
    fig,axis = plt.subplots()
    axis.set_aspect("equal", adjustable="box")
    circle = plt.Circle((0, 0),1,fill=False,color="r")
    axis.add_artist(circle)
    for chord in selected_chords:
        first_point,second_point = chord
        length = math.sqrt((first_point[0] - second_point[0])**2 + (first_point[1] - second_point[1])**2)
        if length > math.sqrt(3):
            plt.plot([first_point[0], second_point[0]], [first_point[1], second_point[1]], color="y")
        else:
            plt.plot([first_point[0], second_point[0]], [first_point[1], second_point[1]], color="g")
    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.title(plot_title)
    plt.xlabel("x-coordinate")
    plt.ylabel("y-coordinate")
    plt.show()

#Generates a random point on circumference of the circle
def point_gen_on_circle():
    angle=random.uniform(-math.pi,math.pi)
    y=math.sin(angle)
    x=math.cos(angle)
    return (x,y)

#Generates a random point which is inside circle
def point_gen_in_circle():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    while (x**2 + y**2) >= 1:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
    return (x, y)    

#Calculates probability by randomly taking two points on circumference of the circle by checking whether that random chords' length is greater than side of inscribed equilateral triangle or not
def actual_prob(trials):
    selected_chords=[]
    favourable_outcomes=0
    val=1
    while val<=trials:
        first_point=point_gen_on_circle()
        second_point=point_gen_on_circle()
        if math.sqrt((first_point[0]-second_point[0])**2 + (first_point[1]-second_point[1])**2) > math.sqrt(3):
            favourable_outcomes+=1
        selected_chords.append((first_point,second_point))
        val+=1
    print("Probability that length of chord is greater than side of the equilateral triangle by randomly selecting a chord : "+ str(favourable_outcomes/trials))
    return selected_chords

#Calculates probability by considering mid point of the chord
def prob_midpoint_approach(trials):
    selected_points_in=[]
    selected_points_out=[]
    favourable_outcomes=0
    val=0
    while val<trials:
        point=point_gen_in_circle()
        dist=math.sqrt(point[0]**2 + point[1]**2)
        if dist<0.5:
            favourable_outcomes+=1
        if dist<0.5 and val%1500 == 0:
            selected_points_in.append(point)
        elif val%1500 == 0:
            selected_points_out.append(point)
        val+=1
    print("Probability when we create sample space considering mid point of the chord : "+str(favourable_outcomes/trials))
    return selected_points_in, selected_points_out

#Calculates probability by considering one point of chord as fixed point
def prob_fixedpt_approach(trials):
    selected_chords=[]
    favourable_outcomes=0
    val=1
    while val<=trials:
        point=point_gen_on_circle()
        if point[1] < -0.5:
            favourable_outcomes+=1
        selected_chords.append(((0,1),point))
        val+=1
    print("Probability when we create sample space considering one point of the chord fixed : "+str(favourable_outcomes/trials))
    return selected_chords 


#Calculates probability by considering distance of chord(from family of parallel chords) from center of circle 
def prob_parallel_chords_approach(trials):
    selected_chords=[]
    favourable_outcomes=0
    val=1
    while val<=trials:
        x=random.uniform(-1,1)
        first_point=(x,math.sqrt(1 - x**2))
        second_point=(x,-1*math.sqrt(1 - x**2))
        if x<0.5 and x>-0.5:
            favourable_outcomes+=1
        selected_chords.append((first_point,second_point))
        val+=1
    print("Probability when we create sample space by considering distance of chord from center : "+str(favourable_outcomes/trials))
    return selected_chords


trials = 1000000
actual_chords=actual_prob(trials)
points_in,points_out=prob_midpoint_approach(trials)
fixedpt_chords=prob_fixedpt_approach(trials)
parallel_chords=prob_parallel_chords_approach(trials)
chords_plotter(actual_chords[::3000], "Actual chords")  #Every 3000th element of actual_chords will be selected
points_plotter(points_in,points_out)
chords_plotter(fixedpt_chords[::3000], "chords\' with one point fixed")
chords_plotter(parallel_chords[::3000], "Parallel chords")