In this section, We'll look into basic but yet significant technique of localization been followed by 
Self Driving Car, Sense and Move.

**In simple terms, a initial probability distribution of object (Car) is constant or uniformly distributed. 
When Sensor senses environment, the probability distribution is updated towards that environment. If required,
we can make a move based on the current probability distribution.**

### Localization

First, a robot starts out with some certainty/uncertainty about its position in a world, which is represented by an initial probability distribution, often called the initial belief or the prior. Then it cycles through sensor measurements and movements.

### Sense/Move Cycle

When a robot senses, a measurement update happens; this is a simple multiplication that is based off of Bayes' rule, which says that we can update our belief based on measurements! This step was also followed by a normalization that made sure the resultant distribution was still vald (and added up to 1).

When it moves, a motion update or prediction step occurs; this step is a convolution that shifts the distribution in the direction of motion.

After this cycle, we are left with an altered posterior distribution!


