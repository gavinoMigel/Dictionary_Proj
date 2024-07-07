import json

words = {
     "BET":"Agreement or approval. Can be said as a question to ask if someone wants to do something or confirm.",
    "CLOUT": "Influence or power, especially in social media.",
    "KERI":"Can Do it All",
    "CHAROT":"Kidding Around",
    "HAY NAKU!" : "Uh oh/ OMG",
    "INTRUSIVE THOUGHTS" : "Unwanted thoughts that can cause distress.",
    "IYKYK" : "Stands for 'If you know, you know'. Used to describe an inside joke or something a certain community would understand.",
    "KAREN" : "Used to describe a stereotypical, often middle-aged white woman perceived as entitled or demanding beyond the scope of what is normal.",
    "MARECAKES" : "A female friend.",
    "NAOL / SANA ALL" : "Expresses desire to have what others have.",
    "OTW/OMW" : "On the way/On my way",
    "PM IS THE KEY" : "Send me a personal message to know more details.",
    "RIZZ" : "Charisma or charm, especially in attracting someone romantically.",
    "CHISMIS/CHIKA" : "Gossip",
    "CLOUTCHASER" : "Someone who seeks to gain fame and attention by associating with popular people or trends",
    "CRAVING SATISFIED" : "When a desire or craving is fulfilled.",
    "CRINGE" : "Feeling of embarrassment or awkwardness.",
    "DELULU" : "Delusional; having unrealistic beliefs or perceptions.",
    "DOGSHOW" : "An event or situation where someone or something is mocked or ridiculed, often in a playful or harsh manner.",
    "DRIP" : "A cool, sexy, or trendy sense of style. Another way of saying swag. When someone has good drip, people will hype them up by having them do a 'drip check', which is showing off your outfit.",
    "EGULS" : "Loss or deficit",
    "ERA" : "A distinct period in history or in a person’s life.",
    "FOR TODAY’S VIDEOW" : "Shares what they are up to.",
    "GASLIGHT" : "To manipulate someone into questioning their own reality or sanity.",
    "GATEKEEP" : "Controlling access to something, often information or resources.",
    "GBU" : "God bless you (short term for greeting someone)",
    "GHOSTING" : "Suddenly ending all communication with someone without explanation.",
    "GROOMING" : "Building a relationship to manipulate or exploit.",
    "GUIZE" : "Guys",
    "HIR NA ME" : "I’m here already!",
    "HITS DIFFERENT" : "When something is so uniquely good/better.",
    "HM" : "How much (short term for asking the price)",
    "HOW TO BE YOU PO?" : "Admiration",
    "I-ADD TO CART MO NA" : "Add to cart",
    "I-TULFO / NA-TULFO" : "Reported to Raffy Tulfo",
    "ICK" : "A sudden feeling of disgust or repulsion towards someone.",
    "INFLUENCER" : "A person with the ability to influence others, often on social media.",
    "INVALIDATE" : "To dismiss or undermine someone’s feelings.",
    "IT’S GIVING" : "Used to describe the vibe or energy something emits.",
    "KORIQUE" : "Correct",
    "KYAH" : "Big Brother",
    "LIT" : "Exciting or excellent.",
    "LIVING RENT-FREE" : "Can’t stop thinking about something. Also used as an insult when someone is upset about something.",
    "LODI / LODS" : "Idol",
    "LOVE BOMBING" : "Overwhelming someone with affection to influence them.",
    "LP" : "Lowest price (short term for showing the lowest discounted price)",
    "MARITESS" : "Refers to people who love to gossip.",
    "MASCULINE/FEMININE ENERGY" : "Traits traditionally associated with masculinity or femininity.",
    "MATSALA" : "Thank you",
    "MEKUS-MEKUS" : "Mix mix",
    "NAUR" : "No",
    "NO CAP/CAPPING" : "Cap is another word for lie. Saying 'no cap' means that you aren’t lying, or if you say someone is 'capping,' then you are saying they are lying.",
    "NONCHALANT" : "Appearing casually calm and relaxed; not displaying anxiety, interest, or enthusiasm.",
    "OL KA BA?" : "Are you online?",
    "PA-MINE" : "Claiming an item during online selling.",
    "PET PEEVE" : "Something that annoys a person.",
    "PETMALU" : "Incredible",
    "PICK ME" : "Someone who craves attention and approval by doing whatever it takes to stand out.",
    "PRANING" : "Crazy",
    "PTSD" : "Post-Traumatic Stress Disorder.",
    "PUSH MO ‘YAN" : "Go for it. Encourages someone to continue pushing or doing something.",
    "RED FLAG/GREEN FLAG" : "Red flag indicates a warning sign; green flag indicates a positive sign.",
    "RELAPSE" : "A deterioration after a period of improvement.",
    "SAFE SPACE" : "A place where one can feel secure.",
    "SAVAGE" : "Fierce, brutal, or ruthless.",
    "WER NA U?" : "Where are you?",
    "BARE MINIMUM" : "Doing the least amount of work necessary.",
    "BASIC" :"Lacking originality; mainstream.",
    "BEEF" : "Conflict or disagreement between individuals.",
    "BESHIE/BESH/BES" : "Best friend",
    "BOP" : "When a song, or album, is really good.",
    "BUDOL" : "Impulse buying",
    "CANCEL" : "To withdraw support from someone, often due to problematic behavior.",
    "CHIBUGAN NA" : "It’s eating time!",
    "DASURV":"Deserve",
    "AS A FRIEND" : "Excuse for friendly but potentially suspicious activities",
    "AUDACITY" : "Boldness or daring, often with a sense of arrogance",
    "SIP TEA" : "To sit back and watch drama unfold, often with amusement or interest.",
    "SIS/SIZST" : "Female endearment term.",
    "SKL" : "I just want to share",
    "SLAY" : "To do something exceptionally well.",
    "SOFT/HARD LAUNCH" : "Soft launch is subtly revealing a relationship; hard launch is publicly announcing it.",
    "STAN" : "When you’re a very big fan of someone famous. Also used when someone does something seen as morally nice and you are giving your approval.",
    "STRONG INDEPENDENT WOMAN" : "A woman who is self-sufficient and confident.",
    "SUSMARYOSEP" : "Jesus, Mary, and Joseph",
    "TARATITAT" : "A talkative person",
    "THE AUDACITY" : "Expression of someone's boldness or daring behavior, often inappropriate or disrespectful.",
    "THROW SHADE" : "To criticize or insult someone subtly or indirectly.",
    "TOLITS" : "Male version of Maritess",
    "TRAUMA" : "Emotional response to a distressing event.",
    "TRIGGERED" : "Having a strong emotional reaction to something.",
    "WALWAL" : "To party or be drunk",
    "WERPA" : "Power",
    "YARN" : "That",
    "BACKBURNER" : "Keeping someone as a second option while pursuing others",
    "AWIT" : "Ouch, it hurts",
    "FLEX":"To show off or boast.",
    "CHEUGY" : "Describes millennials who are trying too hard to be trendy or in style.",
    "GANERN" : "That’s how you do it!",
    "GIGIL MO KO" : "You’re pissing me off",
    "JOWA" : "Girlfriend/Boyfriend",
    "LOWKEY" : "To some extent, secretly or discreetly.",
    "PERIODT" : "Add emphasis to a point made.",
    "PROTECT AT ALL COST" : "Ensuring someone or something is kept safe no matter what.",
    "PUSUAN MO" : "Put a heart on it",
    "SHEESH" : "Used to hype someone up when they look good or do something good, like saying damn. The person getting hyped up uses the 'ice in my veins' pose made famous by basketball player D’Angelo Russell.",
    "SITUATIONSHIP" : "A relationship that is more than a friendship but not quite a committed relationship.",
    "SSOB" : "Boss",
    "VIBE CHECK" : "Checking someone’s energy or personality. Can be a permanent thing, or just based on something someone does. A pass/no pass situation.",
    "WOKE" : "Being aware of social injustices.",
    "YORME" : "Mayor",
    "AESTHETIC":"Concerning the appreciation of beauty or good taste", 
    "A FOREIGNER ASSIGNED TO MANILA (AFAM)":"Foreign men who are in relationships with Filipino women",
    "ALAM NA THIS":"We all know what’s gonna happen.",
    "ANYARE":"What happened?", 
    "APAKAGANDA":"Very Beautiful",
    "FORDA... ANG FERSON":"'for the person' Indicates what the person are up to."}

def custom_key(word):
    return word.replace(" ", "")

slangWords = list(words.keys())

def checkingPerLetters(slangWords):
    n = len(slangWords) # checking the length of the list. This will be the indicator when to stop knowing that the sorting is done

    if n <= 1: 
        return

    for i in range(1, n):
        selected_word = slangWords[i]
        j = i - 1

        selected_word_key = custom_key(selected_word)

        # Move words[j] to words[j + 1] until the right position for selected_word is found
        while j >= 0:
            compared_word = slangWords[j]
            compared_word_key = custom_key(compared_word)

            # Compare character by character
            char_index = 0
            while char_index < min(len(selected_word_key), len(compared_word_key)): # Finding the length of both words and set as the criteria.
                if selected_word_key[char_index] == compared_word_key[char_index]: # If the character is the same; 
                    char_index += 1                                        # It will increment by one
                else:
                    break

            # Determine if we need to move the selected_word
            if char_index < min(len(selected_word_key), len(compared_word_key)): # current char_index
                if selected_word_key[char_index] < compared_word_key[char_index]: # the currect index of index of the word
                    slangWords[j + 1] = compared_word # {Apple,Apple.Application}
                    j -= 1  # j = -1 since the initial of j is 0
                else:
                    break
            else:
                if len(selected_word) < len(compared_word): 
                    slangWords[j + 1] = compared_word  # j = 0 which is index 0
                    j -= 1
                else:
                    break

        slangWords[j + 1] = selected_word

checkingPerLetters(slangWords)

updated_words = {key: words[key] for key in slangWords}
with open("sample.json", "w") as outfile:
    json.dump(updated_words, outfile)
print("Saved in sample.json")