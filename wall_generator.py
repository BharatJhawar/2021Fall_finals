import sys
import random
import numpy as np
import pygame
import matplotlib.pyplot as plt
import math

#Initialize the pygame module
pygame.init()
#Height and width of window in pixels
disp_width, disp_height = 1300,700
#Create window
disp = pygame.display.set_mode((disp_width, disp_height),)
clock = pygame.time.Clock()
pygame.time.wait(3000)

#Bools for input
isLeftPressed = False   #for left mouse button
isRightPressed = False  #for right mouse button
isKeyPressed = False    #for anykeyboard button
accessPoints = []       #store the access points in list
num_rooms = []          #store the rooms in a list
#scale -- 1px is equivalent to 0.033149677ft
SCALE = 0.033149677* 0.0003048 #px to ft to km
distance_hypo = []      #total distance between the wifi router and each accesspoints
average_strength = []   #strength in % between the wifi router and each accesspoints
wifi_position = []      #x and y coordinates of the wifi router during each iteration


def strengthLoss(distance,wall_thickness):
    """
    Calculate the percentage of loss in percentages
    for simplicity the strength decreases by 15% every time the signal goes
    through a wall with thickness of 1px
    :param distance: Euclidean between the wifi router and acces point
    :type distance: float
    :param wall_thickness: Wall thickness in pixels
    :type wall_thickness: int
    :return: percentage of strength
    :rtype: float
    >>>strengthLoss(10, 15, 2.4)
    8.735421910125167
    >>>strengthLoss(0,0,2.4)
    100.0
    >>>strengthLoss(5, 1200, 2.4)
    2.007755651979849e-83
    """
    return 100*(0.85**wall_thickness)

def detectCollisions(signal, rooms):
    """
    Returns True when a signal collides with the walls of a room
    :param signal: signal emitted by router
    :type signal: pygame Rect (object)
    :param rooms: rectangular rooms created
    :type rooms: pygame Rect (object)
    :return: True if signal position and wall position is same
    :rtype: bool
    """
    for wall in rooms:
        return signal.colliderect(wall)

def wifi_signal(wifi_pos, access_list, wifi,screen3, iteration):
    """
    Returns the strength and distance of a wifi to each access point.
    Updates the list of average strength, distance and position of the wifi router during each iteration
    :param wifi_pos:
    :type wifi_pos:
    :param access_list:
    :type access_list:
    :param wifi:
    :type wifi:
    :param screen3:
    :type screen3:
    :param iteration:
    :type iteration:
    :return:
    :rtype:
    """
    background3 = pygame.Surface( (disp_width, disp_height) )
    background3.blit(screen3, (0, 0))
    const_speed = 10
    total_hypo = 0
    total_strength = 0
    for i, points in enumerate(access_list):
        signal_pos = pygame.Rect(*wifi_pos, 5, 5)
        hypo = distanceStart(wifi_pos, points)/const_speed
        total_hypo += hypo
        radians = math.atan2(points[1]-wifi_pos[1], points[0]-wifi_pos[0])
        x_speed = math.cos(radians)*const_speed
        y_speed = math.sin(radians)*const_speed
        x,y = wifi_pos
        wall_thickness = 0
        while True:
            screen3.blit(background3, (0, 0))
            for event4 in pygame.event.get():
                if event4.type == pygame.KEYDOWN:
                    return True
                if event4.type == pygame.QUIT:
                    pygame.quit()
            if signal_pos.x >= disp_width or signal_pos.x <= 0 or signal_pos.y >= disp_height or signal_pos.y <= 0:
                break
            if hypo > 5:
                x += x_speed
                y += y_speed
                pixel_values = screen3.get_at((int(x), int(y)))
                if pixel_values[0] != 0:
                    wall_thickness += 1
                signal = pygame.draw.circle(screen3, (230, 230, 250), (x, y), 5, 0)
                hypo -= 1
            else:
                strength = strengthLoss(hypo + wall_thickness, wall_thickness)
                print(f"{strength} %")
                total_strength += strength
                break
            pygame.display.flip()
            clock.tick(120)
    distance_hypo.append((total_hypo, iteration))  ## total distance between wifi and the access points
    average_strength.append((total_strength/len(accessPoints),iteration)) ## average strength of wifi in %
    wifi_position.append((wifi_pos, iteration))
    return False

def CreateRooms(screen, pos1, pos2,thickness=5):
    """
    Create a rectangular box which resembles a room by giving the top-left and bottom-right corner points
    The thickness of the wall is by default 5px thick
    :param screen:
    :type screen:
    :param pos1:
    :type pos1:
    :param pos2:
    :type pos2:
    :param thickness:
    :type thickness:
    :return:
    :rtype:
    """
    x1, y1 = pos1
    x2, y2 = pos2
    room = pygame.draw.rect(screen, (255,0,0),(*pos1,x2-x1,y2-y1), thickness)
    num_rooms.append(room)

def distanceStart(wifi_pos, access_pos):
    """
    Calculate the Euclidean distance between 2 points
    :param wifi_pos:
    :type wifi_pos:
    :param access_pos:
    :type access_pos:
    :return:
    :rtype:
    >>>distanceStart(40,50)
    64.03124237432849
    >>>distanceStart(50,80)
    94.33981132056603
    >>>distanceStart(123.5,0)
    123.5
    """
    return math.hypot(access_pos[0]-wifi_pos[0], access_pos[1]-wifi_pos[1])


def RandomWifi(screen2,pressedEnter = False):
    """
    Randomly places wifi on the display before running the signal function
    This function is triggered after the user creates the rooms on the display and then presses Enter
    :param screen2:
    :type screen2:
    :param pressedEnter:
    :type pressedEnter:
    :return:
    :rtype:
    """
    background2 = pygame.Surface((disp_width, disp_height))
    background2.blit(screen2, (0, 0))
    iteration = 0
    while True:
        iteration += 1
        screen2.blit(background2, (0, 0))
        x, y = random.randrange(disp_width), random.randrange(disp_height)
        wifi = pygame.Rect(x, y, 5, 5)
        pygame.time.wait(100)
        pygame.draw.rect(screen2, (0, 255, 0), (x, y, 5, 5), 0)
        pygame.display.update()
        interrupt_wifi = wifi_signal((x, y), accessPoints, wifi, screen2, iteration)
        print('Number of random wifi placement', iteration)
        for event3 in pygame.event.get():
            print(event3.type)
            if event3.type == pygame.QUIT:
                pygame.quit()
            if event3.type == pygame.KEYDOWN:
                if event3.key == pygame.K_RETURN:
                    pressedEnter = True
        if pressedEnter:
            return True
        if interrupt_wifi:
            screen2.blit(background2, (0, 0))
            pygame.display.update()
            return True

def PlotGraph(average_strength, distance_hypo):
    """
    Plots the graph of distance and strength
    :param average_strength: list of average strength percentage values
    :type average_strength: list
    :param distance_hypo: list of total distance values between the wifi router and acces points
    :type distance_hypo: list
    :return: matplotplotlib line plot
    :rtype: None
    """
    max_Y_strength = []
    min_dist = np.inf
    min_Y_distance = []
    min_X_distance = []
    for i,j in zip(average_strength, distance_hypo):
        if j[0] < min_dist:
            min_Y_distance.append(j[0])
            min_X_distance.append(j[1])
            max_Y_strength.append(round(i[0],2))
            min_dist = j[0]

    fig, ax = plt.subplots()
    ax.plot(min_X_distance, min_Y_distance)
    ax.set_xlabel('Distance')
    ax.set_ylabel('Iterations')
    plt.title('Distance vs Iterations')
    for i, txt in enumerate(max_Y_strength):
        ax.annotate(txt, (min_X_distance[i], min_Y_distance[i]))
    plt.show()

def optimalWifiPlacement(distance_hypo, wifi_pos):
    """
    From the distance list and wifi position list find the optimal wifi location
    :param distance_hypo: list of distance between wifi and access points
    :type distance_hypo: list
    :param wifi_pos: list of wifi router locations
    :type wifi_pos: list
    :return: tuple of X and Y coordinates
    :rtype: tuple
    >>> A = [(10,1),(50,2),(20,3),(8,4),(100,5)]
    >>> B = [((5,10),1),((3,9),2),((4,4),3),((10,12),4),((9,8),5)]
    >>> optimalWifiPlacement(A,B)
    (10, 12)
    """
    least_pos, iteration = min(distance_hypo, key=lambda x: x[0])
    (X,Y) = wifi_pos[iteration-1][0]
    return X,Y

#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP: # mouse button was released
            if isLeftPressed:
                CreateRooms(disp, initial_pos, pos, 13)
                isLeftPressed = False

        if event.type == pygame.MOUSEBUTTONDOWN: #left mouse button is pressed
            if pygame.mouse.get_pressed()[0]:
                isLeftPressed = True
                initial_pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[2]:
                isRightPressed = True
                pos = pygame.mouse.get_pos()
                pygame.draw.rect(disp, (0, 0, 255), (pos[0], pos[1], 10, 10), 0)
                # add this position to the accesspoints list
                accessPoints.append(pos)
            pos = pygame.mouse.get_pos()
            pygame.display.update()
        if event.type == pygame.MOUSEMOTION and isLeftPressed: # mouse is moving while we press the left mouse button
            pos = pygame.mouse.get_pos()
            # pygame.draw.rect(disp, (255, 0, 0), (pos[0], pos[1], 10, 10), 0)
            # pygame.display.update()
        if event.type == pygame.KEYDOWN:
            isKeyPressed = True

    if isKeyPressed:
        background = pygame.Surface((disp_width, disp_height))
        background.blit(disp, (0, 0))
        pygame.display.flip()
        interrupt = RandomWifi(disp, False)
        print("End of RandomWifi")
        isKeyPressed = False
        PlotGraph(average_strength, distance_hypo)
        X,Y = optimalWifiPlacement(distance_hypo, wifi_position)
        # pygame.draw.circle(disp, (255,255,0),(X,Y),5,5)
        pygame.draw.line(disp,(255,215,0),(X,Y-30),(X,Y+30),2)
        pygame.draw.line(disp,(255,215,0),(X-30,Y),(X+30,Y),2)
        pygame.display.update()
        if interrupt:
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

    pygame.display.flip()


