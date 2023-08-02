
post_likes = 28

# if we like this post
post_likes = post_likes + 1
# todo - display the new number of likes

# if we un-like this post
post_likes = post_likes - 1
# todo - display the new number of likes


# Create a message to display the number of likes
# Instagram says "28 likes"
message = str(post_likes) + ' likes'


username = 'google'

page_title = '@' + username

print(page_title)



username = 'minneapolis_college'

followers = 1522

# If we follow this account...

followers = followers + 1

# Optional - printing with commas

print(f'{followers:,d}')   # prints 1,522