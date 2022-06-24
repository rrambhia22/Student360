import streamlit as st

# Define the multipage class to manage the multiple apps in our program 
class MultiPage: 

    def __init__(self) -> None:
        self.pages = []
    
    def add_app(self, title, func) -> None: 

        self.pages.append({
          
                "title": title, 
                "function": func
            })

    def run(self):
        # Drodown to select the page to run  
        page = st.sidebar.selectbox(
            'App Navigation', 
            self.pages, 
            format_func=lambda page: page['title']
        )

        # run the app function 
        page['function']()