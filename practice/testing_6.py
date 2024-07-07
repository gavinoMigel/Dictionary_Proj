import json

words = {
    "Bet":"Agreement or approval.  Can be said as a question to ask if someone wants to do something or confirm.", 
    "Clout": "Influence or power, especially in social media.", 
    "Keri":"Can Do it All", 
    "Charot":"Kidding Around", "Hay naku!" : "Uh oh/ OMG", "Intrusive thoughts" : "Unwanted thoughts that can cause distress.",
    "Iykyk" : "Stands for -If you know, you know-. Used to describe an inside joke or something a certain community would understand.", "Karen" : "Used to describe a stereotypical, often middle-aged white woman perceived as entitled or demanding beyond the scope of what is normal.",
    "Marecakes" : "A female friend.", "Naol / Sana All" : "Expresses desire to have what others have.", "OTW/OMW" : "On the way/On my way", "PM is the key" : "Send me a personal message to know more details.",
    "Rizz" : "Charisma or charm, especially in attracting someone romantically.",
    "Chismis/Chika" : "Gossip", "Cloutchaser" : "Someone who seeks to gain fame and attention by associating with popular people or trends", "Craving satisfied" : "When a desire or craving is fulfilled.",
    "Cringe" : "Feeling of embarrassment or awkwardness.", "Delulu" : "Delusional; having unrealistic beliefs or perceptions.","Dogshow" : "An event or situation where someone or something is mocked or ridiculed, often in a playful or harsh manner.",
    "Drip" : "A cool, sexy, or trendy sense of style. Another way of saying swag. When someone has good drip, people will hype them up by having them do a “drip check,” which is showing off your outfit.", "Eguls" : "Loss or deficit","Era" : "A distinct period in history or in a person’s life.",
    "For today’s videow" : "Shares what they are up to.", "Gaslight" : "To manipulate someone into questioning their own reality or sanity.","Gatekeep" : "Controlling access to something, often information or resources.",
    "God bless you(GBU)" : "It is a short term for greeting someone","Ghosting" : "Suddenly ending all communication with someone without explanation.","Grooming" : "Building a relationship to manipulate or exploit.",
    "Guize" : "Guys","Hir na me" : "I’m here already!","Hits different" : "When something is so uniquely good/better.",
    "How much(HM)" : "It is a short term for asking the price","How to be you po?" : "Admiration","I-add To Cart Mo Na" : "Add to cart",
    "I-Tulfo / Na-Tulfo" : "Reported to Raffy Tulfo","Ick" : "A sudden feeling of disgust or repulsion towards someone.","Influencer" : "A person with the ability to influence others, often on social media.",
    "Invalidate" : "To dismiss or undermine someone’s feelings.","It’s giving" : "Used to describe the vibe or energy something emits.",
    "Korique" : "Correct","Kyah" : "Big Brother","Lit" : "Exciting or excellent.",
    "Living rent-free" : "Can’t stop thinking about something. Also used as an insult when someone is upset about something.","Lodi / Lods" : "Idol","Love bombing" : "Overwhelming someone with affection to influence them.",
    "Lowest price(LP)" : "It a sign for showing the lowest discounted price","Maritess" : "Refers to people who love to gossip.","Masculine/Feminine Energy" : "Traits traditionally associated with masculinity or femininity.",
    "Matsala" : "Thank you","Mekus-Mekus" : "Mix mix","Naur" : "No",
    "No Cap/Capping" : "Cap is another word for lie. Saying “no cap” means that you aren’t lying, or if you say someone is “capping,” then you are saying they are lying.","Nonchalant" : "Appearing casually calm and relaxed; not displaying anxiety, interest, or enthusiasm.","OL ka ba?" : "Are you online?",
    "Pa-mine" : "Claiming an item during online selling.","Pet peeve" : "Something that annoys a person.",
    "Petmalu" : "Incredible","Pick me" : "Someone who craves attention and approval by doing whatever it takes to stand out.","Praning" : "Crazy",
    "PTSD" : "Post-Traumatic Stress Disorder.","Push Mo ‘Yan" : "Go for it. Encourages someone to continue pushing or doing something.","Red flag/Green flag" : "Red flag indicates a warning sign; green flag indicates a positive sign.",
    "Relapse" : "A deterioration after a period of improvement.","Safe space" : "A place where one can feel secure.","Savage" : "Fierce, brutal, or ruthless.",
    "Wer na u?" : "Where are you?", "Bare minimum" : "Doing the least amount of work necessary.", "Basic" :"Lacking originality; mainstream.", "Beef" : "Conflict or disagreement between individuals.", "Beshie/Besh/Bes" : "Best friend", "Bop" : "When a song, or album, is really good.", "Budol" : "Impulse buying",
    "Cancel" : "To withdraw support from someone, often due to problematic behavior.",
    "Chibugan Na" : "It’s eating time!", "Dasurv":"Deserve", "As A Friend" : "Excuse for friendly but potentially suspicious activities",
    "Audacity" : "Boldness or daring, often with a sense of arrogance",
    "Sip Tea" : "To sit back and watch drama unfold, often with amusement or interest.", "Sis/Sizst" : "Female endearment term.", "SKL" : "I just want to share",
    "Slay" : "To do something exceptionally well.", "Soft/Hard launch" : "Soft launch is subtly revealing a relationship; hard launch is publicly announcing it.", "Stan" : "When you’re a very big fan of someone famous. Also used when someone does something seen as morally nice and you are giving your approval.",
    "Strong independent woman" : "A woman who is self-sufficient and confident.", "Susmaryosep" : "Jesus, Mary, and Joseph", "Taratitat" : "A talkative person",
    "The audacity" : "Expression of someone's boldness or daring behavior, often inappropriate or disrespectful.", "Throw Shade" : "To criticize or insult someone subtly or indirectly.", "Tolits" : "Male version of Maritess", "Trauma" : "Emotional response to a distressing event.",
    "Triggered" : "Having a strong emotional reaction to something.", "Walwal" : "To party or be drunk","Werpa" : "Power",
    "Yarn" : "That", "Backburner" : "Keeping someone as a second option while pursuing others", "Awit" : "Ouch, it hurts",
    "Flex":"To show off or boast.", "Cheugy" : "Describes millennials who are trying too hard to be trendy or in style.", "Ganern" : "That’s how you do it!", "Gigil mo ko" : "You’re pissing me off", "Jowa" : "Girlfriend/Boyfriend",
    "Lowkey" : "To some extent, secretly or discreetly.", "Periodt" : "Add emphasis to a point made.", "Protect at all cost" : "Ensuring someone or something is kept safe no matter what.", "Pusuan Mo" : "Put a heart on it", "Sheesh" : "Used to hype someone up when they look good or do something good, like saying damn. The person getting hyped up uses the “ice in my veins” pose made famous by basketball player D’Angelo Russell.",
    "Situationship" : "A relationship that is more than a friendship but not quite a committed relationship.", "Ssob" : "Boss", "Vibe check" : "Checking someone’s energy or personality. Can be a permanent thing, or just based on something someone does. A pass/no pass situation.", "Woke" : "Being aware of social injustices.", "Yorme" : "Mayor", "Aesthetic":"Concerning the appreciation of beauty or good taste", 
    "A foreigner assigned to manila (AFAM)":"Foreign men who are in relationships with Filipino women", "Alam Na This":"We all know what’s gonna happen.", "Anyare":"What happened?", 
    "Apakaganda":"Very Beautiful", "Forda... Ang Ferson":" 'for the person' Indicates what the person are up to."}

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