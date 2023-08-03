
user_has_liked_post = True

if user_has_liked_post:
    like_icon = 'red_heart.jpg'
else:
    like_icon = 'heat_outline.jpg'


# Generate like message for a post

likes = 0

if likes == 0:   # the post does not have any likes
    message = 'Be the first to like this'
else:  # the post has at least 1 like
    # Nested if-else statement - here the post has at least 1 like
    # so we need to create a message with the correct plural/not plural for 'likes' or 'like'
    if likes == 1:
        message = '1 like'
    else:
        message = str(likes) + ' likes'

print(message)

# or we could do this,

if likes == 0:  # the post has no likes
    message = 'Be the first to like this'
elif likes == 1:  # handle the case with exactly 1 like to use singular 'like'
    message = '1 like'
else:  # all other values of likes will have a plural 'likes'
    message = str(likes) + ' likes'



print(message)


# Generate button text

following = True

if following:
    button_message = 'Following'
    button_color = 'blue'
else:
    button_message = 'Follow'
    button_color = 'white'


comment_text = ''

if len(comment_text) == 0:
    post_button_color = 'gray'
    post_button_active = False
else:
    post_button_color = 'blue'
    post_button_active = True

# TODO - the web app will look at post_button_color and post_button_active
#  and use the values of these variables to display the Post button

# Generating a lot of text to test the character limit
post_text = 'llama ' * 366  # Change the number to generate a shorter or longer string
print(post_text)  # Copy and paste into an instagram post


post_text = 'llama'

if len(post_text) > 2200:  # if more than 2200 characters are entered,
    # Truncate the post_text to just the first 2200 characters, cut off and discard the rest
    # Replace the post_text variable with the sliced version - only the first 2200 characters
    # This syntax is called string slicing
    post_text = post_text[:2200]

# No else needed, if len(post_text) is not larger than 2200, we don't need to make any changes
# post_text is fine as it is

# A better version of the previous if statement - creating another variable
# Advantages
# 1. It describes what the number 2200 represents - the maximum post length
# 2. If the maximum post length changes, we just need to change the variable in one place - compare to the previous
#    version where we would have to make the change in two places. That doesn't sound like a lot,
#    but some data might be used in lots of different places and if you have to make changes everywhere, that's
#    a lot of work and it's easy to miss one by mistake and now you have a bug in your program.

max_post_length = 2200

if len(post_text) > max_post_length:  # if more than max_post_length characters are entered,
    # Truncate the post_text to just the maximum number characters, cut off and discard the rest
    post_text = post_text[:max_post_length]  # Re-use the same variable here



