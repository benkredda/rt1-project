# rt1-project  

## solution of the assignment 

the solution contains three parts (the code in python, the flowchart,and the readme file).

### the code in python

the code shows how the robot will choose the closest silver token to him and grab it, then put it near to the golden 

one. for the control of the linear distance and the orientation i changed the values of thresholds a_th and d_th in a 

way that suits the assignment,i added another integer j that is useful for iteration**in this assignment the process of 
finding a silver box grabing it and putting it close to the golden one has to be repeated six times until we pair them 
together**,besides the equation silver=true which lets the robot know if it has to look for a silver or for a golden 
marker, then i gave the useful functions that the robot use  inorder to move forward**drive**and to rotate**turn**to 
the left or the right, also how to find the closest silver or 
the golden token  

then i made the first condition if silver==true so as to look for a silver token, otherwise for a golden one, and we 
move the robot forward.  

the second condition if was used if there's no token detected we make the robot turn,but if we're close to the silver 
token we try to grab it  

we now try to turn the robot and modify the value of the variable silver, so that in the next step we will look for the 
other type of token which is the golden token.now i want to look for the closest golden token to pair them**while 
silver == False :** by using this while,and then dist has to be less than the d_th inorder to choose the golden token, 
once finding it the robot has to release the silver token,move backward and on the left, and repeat the same operation 
six times, that's why i wrote the equation**j = j+1**and j=6, after pairing all the boxes we excit and break to stop 
the robot.  

please find attached the flowchart in pdf named flowchart of the first assignment, and the code named assignment2.  

[flowchart of the first assignment.pdf](https://github.com/benkredda/rt1-project/files/10016418/flowchart.of.the.first.assignment.pdf)





