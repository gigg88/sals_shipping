# import random function
import random

#create random weight between 1 - 100 kg
weight = random.randint(1,100)


#Ground Shipping


#Weight of Package 	Price per Pound 	Flat Charge
#2 lb or less 	$1.50 	$20.00
#Over 2 lb but less than or equal to 6 lb 	$3.00 	$20.00
#Over 6 lb but less than or equal to 10 lb 	$4.00 	$20.00
#Over 10 lb 	$4.75 	$20.00

 
if weight <= 2:
    cost_ground = weight * 1.5 + 20
elif weight <= 6:
    cost_ground = weight * 3.00 + 20
elif weight <= 10:
    cost_ground = weight * 4.00 + 20
else:
    cost_ground = weight * 4.75 + 20

print("Ground Shipping $", cost_ground)

#Ground Shipping Premium

cost_ground_premium = 125.00

print("Ground Shipping Premium $", cost_ground_premium)
 
#Drone Shipping

#Weight of Package 	Price per Pound 	Flat Charge
#2 lb or less 	$4.50 	$0.00
#Over 2 lb but less than or equal to 6 lb 	$9.00 	$0.00
#Over 6 lb but less than or equal to 10 lb 	$12.00 	$0.00
#Over 10 lb 	$14.25 	$0.00

if weight <= 2:
    cost_ground_drone = weight * 4.5 
elif weight <= 6:
    cost_ground_drone = weight * 9.00
elif weight <= 10:
    cost_ground_drone = weight * 12.00
else:
    cost_ground_drone = weight * 14.25

print("Drone Shipping $", cost_ground_drone)

#Decision for the customer which pricing to choose:

if cost_ground < cost_ground_premium and cost_ground < cost_ground_drone:
    print("You should choose Ground Shipping.")
elif cost_ground_premium < cost_ground and cost_ground_premium < cost_ground_drone:
    print("You should choose Ground Shipping Premium.")
else:
    print("You should choose Ground Shipping by Drone.")


