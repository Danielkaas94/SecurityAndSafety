#!/bin/bash
# #!/bin/bash is called a shebang and it tells the system to use the bash shell to interpret this script.
# Make sure to give execute permissions to this script using: chmod +x Bash_Example.sh

# Date of creation: 10-10-2025

# This is a simple bash script that introduces a person and their aspirations.
# It also demonstrates the use of variables and arrays in bash. 

# Define variables
name="Daniel"
age=31

# Output the introduction
echo "Hello, my name is $name and I am currently $age years old"
echo "I want to be financially free!" 
echo "So that I can say 'F*** YOU' to any soul-crushing experiences and people, like jobs, toxic family members, managers, and acquaintances."

# Additional motivational lines
echo "I want to be able to travel the world and experience new cultures."
echo "I want to be able to spend more time with my family and friends."
echo "I want to be able to pursue my passions and hobbies."
echo "I want to be able to live life on my own terms."
echo "I want to be able to help others and make a positive impact in the world."
echo "I want to be able to retire early and enjoy my golden years."
echo "I want to be able to live a life of freedom and adventure."
echo "I want to be able to say 'F*** YOU' to anyone who tries to hold me back or bring me down."
echo "I want to be able to live a life of purpose and meaning."
echo "I want to be able to say 'F*** YOU' to anyone who doubts me or my abilities."
echo "I want to be able to live a life of abundance and prosperity."
echo "I want to be able to say 'F*** YOU' to anyone who tries to tell me what I can or cannot do."
echo "I want to be able to live a life of joy and happiness."
echo "I want to be able to say 'F*** YOU' to anyone who tries to bring me down or make me feel small."
echo "I want to be able to live a life of freedom and independence."
echo "I want to be able to say 'F*** YOU' to anyone who tries to control me or my life."

echo

echo "I am tired of narcissistic, toxic people in my life."
echo "I am tired of people who try to bring me down or make me feel small."
echo "I am tired of people who try to control me or my life."
echo "I am tired of people who try to tell me what I can or cannot do."
echo "I am tired of people who doubt me or my abilities."
echo "I am tired of people who try to hold me back or bring me down."
echo "I am tired of people who are jealous of my success and try to sabotage me."
echo "I am tired of people who are negative and pessimistic."
echo "I am tired of people who are selfish and only care about themselves."
echo "I am tired of giving love to people who are not able to reciprocate it."
echo "I am tired of being around people who do not support me or my dreams."
echo "I am tired of being around people who are not willing to grow and change."
echo "I am tired of being around people who are not willing to take responsibility for their actions."
echo "I am tired of being around people who are not willing to be honest and authentic."
echo "I am tired of being around people who are not willing to be kind and compassionate."
echo "I am tired of being around people who are not willing to be grateful and appreciative."

echo

echo "F*** your tattos, F*** your piercings, F*** your haircuts, F*** your fashion choices."
echo "F*** your political views, F*** your religious beliefs, F*** your dietary choices."
echo "F*** your lifestyle choices, F*** your relationship choices, F*** your life choices."
echo "F*** your opinions, F*** your judgments, F*** your criticisms."
echo "F*** your negativity, F*** your pessimism, F*** your cynicism."
echo "F*** your selfishness, F*** your greed, F*** your entitlement."
echo "F*** your jealousy, F*** your envy, F*** your resentment."
echo "F*** your manipulation, F*** your deceit, F*** your lies."
echo "F*** your drama, F*** your chaos, F*** your toxicity."
echo "F*** your excuses, F*** your blame, F*** your victim mentality."
echo "F*** your lack of ambition, F*** your lack of drive, F*** your lack of vision."
echo "F*** your lack of integrity, F*** your lack of authenticity, F*** your lack of honesty."
echo "F*** your lack of kindness, F*** your lack of compassion, F*** your lack of empathy."
echo "F*** your lack of gratitude, F*** your lack of appreciation, F*** your lack of respect."
echo "F*** your inability to love, F*** your inability to forgive, F*** your inability to grow."
echo "F*** your inability to change, F*** your inability to evolve, F*** your inability to be better."
echo "F*** your inability to see the good in others, F*** your inability to see the good in yourself."
echo "F*** your inability to be happy, F*** your inability to be free, F*** your inability to be you."
echo "F*** your inability to live life to the fullest, F*** your inability to be true to yourself."
echo "F*** your inability to be the best version of yourself."
echo "F*** your inability to be the person you were meant to be."
echo "F*** your inability to be the person you want to be."
echo "F*** your inability to be the person you deserve to be."
echo "F*** your inability to be the person you are capable of being."
echo "F*** your inability to be the person you were born to be."
echo "F*** your inability to be the person you choose to be."
echo "F*** your inability to be the person you decide to be."
echo "F*** your inability to be the person you aspire to be."
echo "F*** your inability to be the person you dream to be."

echo

echo "Surround yourself with people who lift you up, inspire you, and support you."
echo "Surround yourself with people who challenge you to be better, who push you to grow"
echo "Don't hang around with dumb people,"
echo "Don't be afraid of the solitude that comes with raising your standards."
echo "Yet again, I am probably another case of Tall Poppy Syndrome 🤡🌹🥀🌹🤡"

# Alright rant is over...
# Now let's demonstrate some basic bash features

set -x  # Enable debugging mode to print each command before executing it
# This is useful for understanding the flow of the script and for debugging.

whoami  # This command prints the current user

id     # This command prints the user ID and group ID of the current user

set +x  # Disable debugging mode


# Parameters in Bash
echo "The name of this script is: $0"  # $0 is the name of the script
echo "The first parameter is: $1"      # $1 is the first parameter passed to the script
echo "The second parameter is: $2"     # $2 is the second parameter passed to the script
echo "The total number of parameters is: $#"  # $# is the total number of parameters passed to the script
echo "All parameters are: $*"          # $* is all the parameters passed to the script





# Arrays in Bash
transport=('car' 'train' 'bike' 'bus')

# This will print all elements in the array 
echo "${transport[@]}"

# This will print the second element in the array (index starts at 0)
echo "${transport[1]}"

unset transport[2]  # This will remove the third element ('bike') from the array
echo "${transport[@]}"  # Print the array after removing an element

transport[2]='plane'  # This will add 'plane' as the third element in the array
echo "${transport[@]}"  # Print the array after adding an element

