import os
import game
import random


def generate_unique_number():

    unique_number_list = [0,1,2,3,4,5,6,7,8,9]

    guess_numbers = []
    while len(guess_numbers) < 3:

        unique_number = random.choice(unique_number_list)
        guess_numbers.append(str(unique_number))
        unique_number_list.remove(unique_number)

    return guess_numbers

def get_user_input():
    while True:
        user_input = input("Please write 3-digit number: ")
        if user_input.isdigit() and len(user_input) == 3 and len(set(user_input)) == len(user_input):
            break
        else:
            print("Number should be 3-digit!")
    return list(user_input)


def compare_user_answer(guess, correct_answer):
    hints = []
    for i in range(len(guess)):
        if guess[i] == correct_answer[i]:
            hints.insert(0, "hot")
        elif guess[i] in correct_answer:
            hints.append("warm")
    if not hints:
        hints = ["cold"]
    return hints


def fight_with_guardian(data):
    os.system('cls' if os.name == 'nt' else 'clear')
    if data["current_location"] == 1:    
        print('\x1b[1;33;40m' + '''
            |\___/|
            (,\  /,)\'
            /     /  \'
           (@_^_@)/   \'
            W//W_/     \'
          (//) |        \'
        (/ /) _|_ /   )  \'
      (// /) '/,_ _ _/  (~^-.
    (( // )) ,-{        _    `.
   (( /// ))  '/\      /      |
   (( ///))     `.   {       }
    ((/ ))    .----~-.\   \-'
             ///.----..>   \'
              ///-._ _  _ _}''' + '\x1b[0m')
    else:
        print('\x1b[1;31;40m'+'''                                      
             />\\//\\/>\                     /<\//\\//<\'
              \Y  \>                                     
            />  //\ />\ \>    .;`'`/`;<\   ;/> /> \>/ \\: \>
           />  //: />  \> \>    o o    /> /> />\>  \\  \>
          />  //  /> \> \> \>  oO Oo />        \\  \>      
         />  //  />   `;.;. . (  ..  )  .;`;`     \>  \\  \>
       />  //: />           \\  \>                             
      /> // />             \>                          <\ \\ <\'
      \\ \>                                                      
     />// />                  /`//\                      <\ \\<\'
    \\ \>                                                        
    />///>                   _//\ \/                       <\\\<\'
   \\\>                                                           
   />//>                                                     <\\<\'
  \\>                                                             
    \\(                                                       )//
      \\                                                     //
      '''+ '\x1b[0m')
    user_guesses = 10
    correct_answer = generate_unique_number()
    print(correct_answer)
    while user_guesses > 0:
        user_input = get_user_input()
        feedback = compare_user_answer(user_input, correct_answer)
        print(feedback)
        if feedback == ["hot", "hot", "hot"]:
            print("Guardian is confused with your quick answer, you manage to kill him without any troubles")
            if [data["current_location"] == 1:
                print("You found sword and chain shirt, you equip them")
                inv = data["inventory"]
                data["sword"][0] = 1:
                data["shirt"][0] = 1
            break
        user_guesses -= 1


if __name__ == '__fight_with_guardian__':
    fight_with_guardian()