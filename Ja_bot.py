import streamlit as st

# Set the title of the app
st.title("Welcome to My First Streamlit App")

# Add a text input
name = st.text_input("Enter your name:")

# Display the name entered by the user
if name:
    st.write(f"Hello, {name}! Welcome to the app.")
    responses = {
    "hi": ["hello,", "ypree", "wah gwan"],
    "whats your name?": ["mhi name karen, bout you?"],
    "how are you doing?": ["mhi a gwan good man, how things fhi you?"],
    "my name is jayden": ["oh nice to meet you"],
    "where can i buy a ps5?": ["can guh up a shopas fare dem give yuh the best deals"],
    "whats a good place to go and enjoy myself in jamaica?": ["can guh a e beach and cheack out some a e nice brownin dem and eat fry fish, jus doh turn inna one!"],
    "what is some activities would you recommend me doing to lose weight?": ["get up and start run until uh drop dung"],
    "whats jamaica national dish?": ["Ackee and salt fish, mek yuh mouth wata!"],
    "what hotel would be the best hotel to stay at for my summer holiday?": ["the best hotel woulda be RIO, nice pool, workers and everything"],
    "tell me a joke": ["wah mek tammy bring a ladda to the bar? because him hear seh rum deh pon e house!"],
    "tell me another joke": ["dis is why jamaicans dont play hide and seek.  EVERYBODY KNOW YUH BUSINESS!"],
    "im sad": ["with this version of karen the ai cannot help you with this statement right now. please try updating and try again. THANKS!"],
    "can you start replying in standard english?": ["ok, how may i assist you today?"],
    "im looking for walmarts online shopping platform but i cannot find it can you help?": ["https://www.walmart.com/ here you go, enjoy your shopping spree!"],
    "Can you give me a random fact?": ["Maine is the only state that has a one-syllable name"],
    "whats your favorite movie?": ["As an AI, I don't have personal preferences or feelings, so I don't have a favorite movie. However, I can help recommend movies based on your interests or discuss popular films if you'd like! What kind of movies do you enjoy?"],
    "Do you know any fun games?": ["Among Us, Rocket League, Overcooked 2, etc."],
    "Can you recommend a book to read?": ["The Great Gatsby, Harry Potter and the Sorcerer's Stone, The Catcher in the Rye, etc."],
    "bye": ["Goodbye! Have a great day."],
    "wah gwaan": ["Mi deh yah, yuh know! How can I help yuh today?"],
    "how yuh stay?": ["Mi good, thanks! Wah 'bout yuh?"],
    "how di weather stay?": ["Di sun hot today! Perfect fi go beach."],
    "wah fi eat today?": ["Yuh cyaan go wrong wid some ackee an' saltfish, or maybe a nice plate of jerk chicken!"],
    "tell mi 'bout bob marley": ["Bob Marley is a reggae legend from Jamaica, known fi hits like 'One Love' and 'No Woman, No Cry.'"],
    "wah is a patty?": ["A patty is a tasty Jamaican pastry filled wid meat or vegetables. Perfect fi a quick snack!"],
    "whe mi can visit in jamaica?": ["Yuh should check out Dunn's River Falls, Negril Beach, and the Bob Marley Museum!"],
    "wah is blue mountain coffee?": ["Blue Mountain Coffee is one of di best coffees in di world, grown right here in Jamaica!"]
}

while True:
  user_input = input("you: ")
  if user_input.lower()in responses:
   karen_reply = random.choice(responses[user_input.lower()])
  elif user_input.lower() == "bye":
    print("Okay,have a great day!")
    break
  else:
      print("karen:" "Im sorry i didnt get that please resend your message")


