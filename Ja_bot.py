import streamlit as st

# Set the title of the app
st.title("Welcome to My First Streamlit App")

# Add a text input
name = st.text_input("Enter your name:")

# Display the name entered by the user
if name:
    st.write(f"Hello, {name}! Welcome to the app.")
```
Note the import statement that ends with "st".  Anytime you use the letters "st", it means you're about to use something from the streamlit library.

So lets take a quick look at this code so far.  

* st.title:  This is to give your application a title at the top of the page.  This is looking for a string.

* st.text_input: this is similar to you python input method.  Remember?  In regular python, the would look like `name=input("Enter Name")` but when dealing with streamlit, the syntax is `name=st.text_input("Enter Name")` where "name" is the variable.

* st.write: Anytime you see this, it means you're writing something on the page.  In the code, you see it refers to a variable with the curly brackets

