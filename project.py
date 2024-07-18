import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI
from PIL import Image, ImageTk 


# Define the background color
bg_color = "#6d326b"
text_bg_color = "#FFFECC"  # Background color for text areas
text_fg_color = "black"  # Foreground color for text

# Replace with your actual OpenAI API key


# Create the main window
root = tk.Tk()
root.title("Listnr")
root.geometry("600x600")
root.configure(bg="#FFFECC")

# create a frame widget
frame1 = tk.Frame(root, width=500, height=600, bg="#FFFECC")
frame1.grid(row=0, column=0)


def loadframe2():
    print("Welcome, I am Listnr")
     

#frame1 widgets
frame1.pack_propagate(False)
logo_img = ImageTk.PhotoImage (file="m_o_m-2.png")
logo_widget = tk.Label(frame1, image = logo_img)
logo_widget.image = logo_img
logo_widget.pack()

# button widget
tk. Button(
frame1,text="Enter", font=("TkHeadingFont", 20),
bg="#28393a",
fg="white",
cursor="hand2",
activebackground="#badee2",
activeforeground="black",
command= loadframe2()
).pack()


# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

def generate_response(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Use 'gpt-3.5-turbo' or 'gpt-4' based on your access
            messages=messages,
            max_tokens=150,  # Increase the max tokens to handle longer conversations
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I don't get that. Please repeat yourself."

def send_message(): 
    user_input = user_entry.get()
    if user_input.strip():
        messages.append({"role": "user", "content": user_input})
        chat_log.configure(state='normal')
        chat_log.insert(tk.END, f"You: {user_input}\n", "user")
        user_entry.delete(0, tk.END)
        chat_log.configure(state='disabled')
        chat_log.yview(tk.END)

        if user_input.upper() == 'PINEAPPLE JUICE':
            chat_log.configure(state='normal')
            chat_log.insert(tk.END, "Listnr: I hope I was able to help. Enjoy your day!\n", "bot")
            chat_log.configure(state='disabled')
            return

        response = generate_response(messages)
        if response:
            chat_log.configure(state='normal')
            chat_log.insert(tk.END, f"Listnr: {response}\n", "bot")
            chat_log.configure(state='disabled')
            chat_log.yview(tk.END)
            messages.append({"role": "assistant", "content": response})


# Initialize the OpenAI client
client = OpenAI(api_key = api_key)

def generate_response(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Use 'gpt-3.5-turbo' or 'gpt-4' based on your access
            messages=messages,
            max_tokens=150,  # Increase the max tokens to handle longer conversations
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return None


# Create the main window
root = tk.Tk()
root.title("Listnr")
root.geometry("600x600")
root.configure(bg=bg_color)


## Create the chat log (ScrolledText widget)
chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=60, height=20, bg=text_bg_color, fg=text_fg_color)
chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
chat_log.tag_config("user", foreground="#77C17A")
chat_log.tag_config("bot", foreground="#6d326b")
chat_log.configure(state='normal')
chat_log.insert(tk.END, "Hi, I'm Listnr, talk with me about how you've been feeling. I'm here to help you, just tell me a little bit about how you feel and I'll be here to help. If you feel satisfied with our conversation or are done with the conversation just say 'Pineapple Juice'. How are you? What's your name?\n", "bot")
chat_log.configure(state='disabled')



# Make the window resizable
root.resizable(True, True)

# Configure the grid to adjust widget sizes
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)

# Create the entry widget for user input
user_entry = tk.Entry(root, width=50, bg=text_bg_color, fg=text_fg_color)
user_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Create the send button
send_button = tk.Button(root, text="Send", command=send_message, bg=text_bg_color, fg=text_fg_color)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Initialize the conversation messages
messages = [{"role": "system", "content": (
    "You are a virtual therapist. Provide empathetic, supportive, and non-judgmental responses to help the user with their emotional and mental well-being. "
    "Offer actionable advice and coping strategies where possible, but always remind them to seek professional help for serious issues."
)}]


# Start the Tkinter event loop
root.mainloop()


# import tkinter as tk
# from tkinter import scrolledtext
# from openai import OpenAI
# from PIL import Image, ImageTk 


# # Define the background color
# bg_color = "#6d326b"
# text_bg_color = "#FFFECC"  # Background color for text areas
# text_fg_color = "black"  # Foreground color for text

# # Replace with your actual OpenAI API key

# # Initialize the OpenAI client
# client = OpenAI(api_key=api_key)

# def generate_response(messages):
#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o",  # Use 'gpt-3.5-turbo' or 'gpt-4' based on your access
#             messages=messages,
#             max_tokens=150,  # Increase the max tokens to handle longer conversations
#             temperature=0.7
#         )
#         return response.choices[0].message['content'].strip()
#     except Exception as e:
#         print(f"Error generating response: {e}")
#         return "Sorry, I don't get that. Please repeat yourself."

# def send_message(): 
#     user_input = user_entry.get()
#     if user_input.strip():
#         messages.append({"role": "user", "content": user_input})
#         chat_log.configure(state='normal')
#         chat_log.insert(tk.END, f"You: {user_input}\n", "user")
#         user_entry.delete(0, tk.END)
#         chat_log.configure(state='disabled')
#         chat_log.yview(tk.END)

#         if user_input.upper() == 'PINEAPPLE JUICE':
#             chat_log.configure(state='normal')
#             chat_log.insert(tk.END, "Listnr: I hope I was able to help. Enjoy your day!\n", "bot")
#             chat_log.configure(state='disabled')
#             return

#         response = generate_response(messages)
#         if response:
#             chat_log.configure(state='normal')
#             chat_log.insert(tk.END, f"Listnr: {response}\n", "bot")
#             chat_log.configure(state='disabled')
#             chat_log.yview(tk.END)
#             messages.append({"role": "assistant", "content": response})


# # Initialize the OpenAI client
# client = OpenAI(api_key = api_key)

# def generate_response(messages):
#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o",  # Use 'gpt-3.5-turbo' or 'gpt-4' based on your access
#             messages=messages,
#             max_tokens=150,  # Increase the max tokens to handle longer conversations
#             temperature=0.7
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         print(f"Error generating response: {e}")
#         return None


# # Create the main window
# root = tk.Tk()
# root.title("Listnr")
# root.geometry("600x600")
# root.configure(bg=bg_color)


# ## Create the chat log (ScrolledText widget)
# chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=60, height=20, bg=text_bg_color, fg=text_fg_color)
# chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
# chat_log.tag_config("user", foreground="#77C17A")
# chat_log.tag_config("bot", foreground="#6d326b")
# chat_log.configure(state='normal')
# chat_log.insert(tk.END, "Hi, I'm Listnr, talk with me about how you've been feeling. I'm here to help you, just tell me a little bit about how you feel and I'll be here to help. If you feel satisfied with our conversation or are done with the conversation just say 'Pineapple Juice'. How are you? What's your name?\n", "bot")
# chat_log.configure(state='disabled')

# # Make the window resizable
# root.resizable(True, True)

# # Configure the grid to adjust widget sizes
# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=0)

# # Create the entry widget for user input
# user_entry = tk.Entry(root, width=50, bg=text_bg_color, fg=text_fg_color)
# user_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# # Create the send button
# send_button = tk.Button(root, text="Send", command=send_message, bg=text_bg_color, fg=text_fg_color)
# send_button.grid(row=1, column=1, padx=10, pady=10)

# # Initialize the conversation messages
# messages = [{"role": "system", "content": (
#     "You are a virtual therapist. Provide empathetic, supportive, and non-judgmental responses to help the user with their emotional and mental well-being. "
#     "Offer actionable advice and coping strategies where possible, but always remind them to seek professional help for serious issues."
# )}]


# # Start the Tkinter event loop
# root.mainloop()

# # Start the Tkinter event loop
# root.mainloop()