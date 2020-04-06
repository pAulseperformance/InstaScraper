from subprocess import call

# TODO: Add feature that watches system output from instagram scraper to verify instagram hasn't blocked the signin attempt.
# Have user be notified so they can go to the url and verify the access.

def igscrape(session):
    # default_attr = dict(username='', usernames=[], filename=None,
    #                     login_user=None, login_pass=None,
    #                     followings_input=False, followings_output='profiles.txt',
    #                     destination='./', retain_username=False, interactive=False,
    #                     quiet=False, maximum=0, media_metadata=False, profile_metadata=False, latest=False,
    #                     latest_stamps=False, cookiejar=None,
    #                     media_types=['image', 'video', 'story-image', 'story-video'],
    #                     tag=False, location=False, search_location=False, comments=False,
    #                     verbose=0, include_location=False, filter=None, proxies={}, no_check_certificate=False,
    #                                                 template='{urlname}')
    #
    os_system_call = ['instagram-scraper']

    username = '--login-user ' + str(session['username'])
    password = '--login-pass ' + str(session['password'])
    tag = '--tag ' + str(session['brand']) + ', ' + str(session['product'])
    media_types = '--media-types JPG'
    comments = '--comments' # session[comments] = bool
    # limit = '--maximum ' + int(3) #+ int(session['maximum']) # Maximum number of items to scrape.

    for k, v in session.items():
        if v:
            if k == 'brand':
                os_system_call.append('--tag')
                os_system_call.append(v)
            elif k == 'username':
                os_system_call.append('--login-user')
                os_system_call.append(v)
            elif k == 'password':
                os_system_call.append('--login-pass')
                os_system_call.append(v)


    os_system_call.append('--maximum')
    os_system_call.append('5')
    os_system_call.append(comments)
    os_system_call.append('--media_types')
    os_system_call.append('image')
    os_system_call.append("--destination")
    os_system_call.append("content/")
    os_system_call.append("--retain-username")
    os_system_call.append("--interactive")
    print(os_system_call)
    call(os_system_call)


