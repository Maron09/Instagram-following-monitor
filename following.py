import instaloader

def get_following_count(username):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    return profile.followees  # This returns the number of users that the given Instagram user is following
