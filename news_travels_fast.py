# Imports go at the top
from microbit import *
import speech

# Names is a dictionary
beavers = {0:'A',1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L'}
num_beavers = len(beavers)

# Beaver poles is a list of friends
beaver_poles = []
# Create empty list for each beaver
for i in range(len(beavers)):
    beaver_poles.append(i)

beaver_poles[0] = {1, 4, 7}
beaver_poles[1] = {0, 3, 9}
beaver_poles[2] = {4, 9}
beaver_poles[3] = {1, 8, 10}
beaver_poles[4] = {0, 2}
beaver_poles[5] = {6, 9}
beaver_poles[6] = {4, 9}
beaver_poles[7] = {0, 10}
beaver_poles[8] = {3}
beaver_poles[9] = {1, 5, 6, 11}
beaver_poles[10] = {3, 7}
beaver_poles[11] = {9}

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.is_pressed():
        
        # Hops: a friend to forward/jump message
        beaver_hops = {}
        # Initiate number of hops to zero
        for beaver in range(0, num_beavers):
            beaver_hops[beaver] = 0

        # Current fastest beaver
        min_hops = num_beavers
        beaver_min_hops = 0

        for start in range(0, num_beavers):
            route_list = [[start]]
            route_index = 0

            prev_beavers = {start}

            # Track beavers that was send to
            all_sent = False

            # Visit all beaver ropes
            while route_index < len(route_list) and not all_sent:
                current_route = route_list[route_index]
                last_beaver = current_route[-1]
                next_beavers = beaver_poles[last_beaver]

                # Check if all beavers have been sent
                if len(prev_beavers) == len(beavers):
                    all_sent = True
                    # Update current winner
                    if beaver_hops[start] < min_hops:
                        beaver_min_hops = start
                        min_hops = beaver_hops[start]

                else:
                    if len(next_beavers) > 1 or (len(next_beavers) == 1 and list(next_beavers)[0] not in prev_beavers):
                        # Jump through next friend
                        # Update the number of jumps
                        beaver_hops[start] += 1

                        # Send to beavers in the next jump
                        for beaver in next_beavers:
                            if beaver not in prev_beavers:
                                new_route = current_route[:]
                                new_route.append(beaver)
                                route_list.append(new_route)
                                # Track visited beavers
                                prev_beavers.add(beaver)

                # Continue to next beaver
                route_index += 1

        # Print(beaver_hops)
        # Print fastest beaver to start with
        speech.say("Start from " + beavers[beaver_min_hops] + ".")
        display.scroll(beavers[beaver_min_hops])







