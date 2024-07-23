import random

# irchvevs randomulad sityvebs romelic qvevit def funqciis daxmarebit aris gamokofili 
def choose_word():
    words = ["python", "coding", "html", "css", \
            "programming", "code", "goa", "visual", "studio"]

    # aq kodi tavisit irchvevs chamnotvlil sityvebs da is unda gamoicnos momxmarebelma 
    return random.choice(words)

# abrunebs sityvas stringit rom ufro gauadvildes momxmarebels sityvis gamocnooba
def word_status(word, guessed_letters):

    # es kodi ki gvexmareba imashi rom gavigot sad unda gamovicnot aso an sad unda chaiweros is chveni dapewvdis shemtxvevashi "_"
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter 
        else:
            display += "_"

    return display 

#def funqciis gamokenebit chven vushvebt funqcias saxelad gamoicani sityva 
def word_guessing_game():

    # chven am kodit shegvidzlia shevarchiot sityva da aseve shegvidzlia shevcvalot cdis sixshire
    secret_word = choose_word()
    guessed_letters = []
    attempts = 10
    
    # am kodis daxmarebit momxmarebeli gaigebs tu sityvashi ramdeni aso aris chasasmeli da daexmareba es mas gamocnobashi 
    print("Word Guessing Game")
    print("******************")
    print("Secret Word:", word_status(secret_word, guessed_letters))

    # iqamde grdzeldeba tamashi sanam 6'ive cdas ar davxarjavt
    while attempts > 0:

        # roca ukve amovardeba nishani/winadadeba (Guess A Letter) shegvidzlia ukve daviwkot misi gamocnoba .
        guess = input("Guess A Letter: ").lower()

        # Ichven mxolod da mxolod shegvidzlia 1 asos dawera da ara mtliani sityvis 
        if len(guess) != 1 or not guess.isalpha():
            print("You must enter a single letter.")
            continue  

        # aseve tu chven ukve davweret romelime aso da gamovicanit misi meored gamotana gamoitans aset winadadebas (you already guessed that letter.) mag: sityva "zuka" ____   gamoviccani aso "Z" misi meored dawera gamogvitans (you already guessed that letter.)    
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue 
        
        # tu gamovicanit sityvashi mocemuli aso mashin dagviwers (Letter Guess)
        guessed_letters.append(guess)

        # tu dafarul sityvashi araris is aso romelic  adgens am sityvas mashin momxmarebeli kargavs cdas (-1 attempt)
        if guess not in secret_word:
            attempts -= 1
            print(f"No letter '{guess}' occurs in the word.")
            print(f"You have {attempts} attempts remaining.")
        # roca chven gamovicnobt asos chven shegvidzlia gamovyot misi gamochenis dro 
        else:
            occurrences = secret_word.count(guess)
            print(f"Letter '{guess}' occurs {occurrences} times.")

        # axla ki davprintot sityvis axali statusi 
        current_status = word_status(secret_word, guessed_letters)
        print("Secret Word:", current_status)

        #tu ar darcha chasasmeli sityvebi mashin nishanvs rom moige 
        if "_" not in current_status:
            print("Congratulations! You guessed the word.")
            break

   #roca 6 cda morcheba waageb 
    if "_" in current_status:
        print(f"You ran out of attempts! The word was: {secret_word}")

# axla ki gamovidzaxot es damaliuli sityva 
word_guessing_game()