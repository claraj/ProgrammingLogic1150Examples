post_likes = 28

# user likes this post - need to update the value of the variable
post_likes = post_likes + 1  # modifying the value of post_likes with assignment

print(post_likes)

# User un-likes the post
post_likes = post_likes - 1  # modifying the value of post_likes with assignment

# Create a message to display with the number of likes
message = str(post_likes) + ' likes'

print(message)

# Create the page title from the username variable

username = 'google'

page_title = '@' + username

print(page_title)


# Switch to a different username

# Work with the number of followers

username = 'minneapolis_college'

followers = 1522

# If we follow this account...

followers = followers + 1

# Optional - printing with commas
print(f'{followers:,d}')   # prints 1,522

## Checking the length of post text

post_text = 'I met a llama this summer!'

post_text_length = len(post_text)

print(post_text_length)