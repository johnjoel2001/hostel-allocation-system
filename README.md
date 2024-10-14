<b>Stable Roommate Matching in a Hostel using Gale-Shapley Algorithm </b>

The main objective of this project is to find the most stable pairings of roommates within a hostel environment. The matching process divides the hostellers into two distinct groups:

Group 1: Students with grades above 9.
Group 2: Students with grades below 9.

Each student ranks the members of the opposite group in order of their preference. The matching is considered stable if no two students would prefer each other over their assigned roommates based on the results. This project implements the Gale-Shapley algorithm, a well-established method used to achieve stable matchings between two groups.

To bring this idea to life, I developed a web application using Django, which facilitates the entire process—from collecting preferences to generating the final stable roommate pairs. The algorithm efficiently pairs students from the two groups, ensuring stability in the matchings.
