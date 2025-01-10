import pandas as pd
import numpy as np
import tkinter as tk

follower = pd.read_json("followers_1.json")
following = pd.read_json("following.json")



def extract_followers_value():
    follower_data = []
    for items in follower["string_list_data"]:
        for values in items:
            follower_data.append(values['value'])
    return follower_data


def extract_following_value():
    following_data = []
    for items in following["relationships_following"]:
        for values in items["string_list_data"]:
            following_data.append(values['value'])
    return following_data



def display_followers_and_following():
    following_list = extract_following_value()
    followers_list = extract_followers_value()
    non_follower_list = list(set(following_list)-set(followers_list))
    root = tk.Tk()
    root.title("Instagram Followers and Following")

    followers_listbox = tk.Listbox(root)
    followers_listbox.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

    following_listbox = tk.Listbox(root)
    following_listbox.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT)

    non_follower_listbox = tk.Listbox(root)
    non_follower_listbox.pack(fill=tk.BOTH, expand=True, side=tk.BOTTOM)

# Insert column headings
    followers_listbox.insert(tk.END, "Followers")
    following_listbox.insert(tk.END, "Following")
    non_follower_listbox.insert(tk.END, "Non-Followers")

    for follower in followers_list:
        followers_listbox.insert(tk.END, follower)

    for following in following_list:
        following_listbox.insert(tk.END, following)

    for non_follower in non_follower_list:
        non_follower_listbox.insert(tk.END, non_follower)

    root.mainloop()

# Call the display_followers_and_following function to run the application
display_followers_and_following()