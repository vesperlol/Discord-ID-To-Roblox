# Official D2R 
# By : vesper #0003/#8757
# Can be hosted on Desktop OR Replit

# Modules
import discord, requests, random

# Setup
channel_id = 0 # channel ID to receive information
token = 'token here' # Bot token
command = '!verify' # Command to verify a Discord ID 2 roblox
D2R = discord.Client()
######################################################################

def coloR():
    random_colors = random.choice([
    0x2ecc71, # green
    0xe74c3c, # red
    0xe67e22, # orange
    0xf1c40f, # gold
    0xe91e63, # magenta
    0x3498db # blue
    ])
    return random_colors

def info(id):
    robloxID = id
    profile = f"https://www.roblox.com/users/{id}/profile"
    r = requests.get(profile).text
    image = r.split('<meta property="og:image" content="')[1].split('"')[0]
    username = r.split('<title>')[1].split(" -")[0]
    friends = r.split(f'<div data-profileuserid="{id}"')[1].split('data-friendscount="')[1].split('"')[0]
    followers = r.split(f'<div data-profileuserid="{id}"')[1].split('data-followerscount="')[1].split('"')[0]
    following = r.split(f'<div data-profileuserid="{id}"')[1].split('data-followingscount="')[1].split('"')[0]
    try:
        p = r.split('<span class="icon-premium-')[1].split('"></span>')[0]
        if p == "medium" or p=="small":
            premium = True
    except:premium = False
    try:
        facebook = "https://www.facebook.com"+r.split("profile-social Facebook")[0].split('href="https://www.facebook.com')[1].split('"')[0]
    except:facebook = None
    try:
        twitter = "https://twitter.com"+r.split("profile-social Twitter")[0].split('href="https://twitter.com')[1].split('"')[0]
    except:twitter = None
    try:
        youtube = "https://youtube.com"+r.split("profile-social Youtube")[0].split('href="https://youtube.com')[1].split('"')[0]
    except:youtube = None
    try:
        twitch = "https://twitch.tv"+r.split("profile-social Twitch")[0].split('href="https://twitch.tv')[1].split('"')[0]
    except:twitch = None
    roli = requests.get(f"https://www.rolimons.com/player/{id}")
    if roli.status_code ==200:
        rolimon = f"https://www.rolimons.com/player/{id}"
    else:rolimon = "Not Found"
    return robloxID, profile, image, username, friends, followers, following, premium, facebook, twitter, twitch, youtube, rolimon

def check_Bloxlink(ID):
    r = requests.get(f"https://api.blox.link/v1/user/{ID}")
    if r.status_code == 200:
        try:
            id = r.json()["primaryAccount"]
        except:
            id = None
        return id
    else:return None
def check_Rover(ID):
    r = requests.get(f"https://verify.eryn.io/api/user/{ID}")
    if r.status_code==200:
        try:
            id = r.json()["robloxId"]
        except:
            id = None
        return id
    else:return None
@D2R.event
async def on_ready():
    print(f"[+] Connected To {D2R.user.name}")
@D2R.event
async def on_message(message):
    channel = D2R.get_channel(channel_id)
    if message.content.startswith(f'{command}'):
        ID = message.content.split(f'{command} ')[1]
        RobloxID1 = check_Bloxlink(ID)
        RobloxID2 = check_Rover(ID)
        if RobloxID1== None:await channel.send(f"{ID} Doesnt have any Roblox Account Linked to Bloxlink")
        else:
            try:
                colora = coloR()
                robloxID, profile, image, username, friends, followers, following, premium, facebook, twitter, twitch, youtube, rolimon = info(RobloxID1)
                embed=discord.Embed(title="D2R Bot", description="**Found Roblox Account (Bloxlink)**", color=colora)
                embed.set_thumbnail(url=image)
                embed.add_field(name=f"Roblox Account Of : {ID}\n", value=f"```Username : {username}\nRoblox ID : {robloxID}\nFriends : {friends}\nFollowers : {followers}\nFollowing : {following}\nPremium : {premium}```", inline=False)
                embed.add_field(name=f"Links\n", value=f"Roblox Profile : **{profile}**\n\nRolimon : **{rolimon}**\n\nFacebook : **{facebook}**\n\nTwitter : **{twitter}**\n\nTwitch : **{twitch}**\n\nYoutube : **{youtube}**", inline=False)
                await channel.send(embed=embed)
            except:await channel.send(f"{ID} Doesnt have any Roblox Account Linked to Bloxlink")
        if RobloxID2== None:await channel.send(f"{ID} Doesnt have any Roblox Account Linked to ROVER")
        else:
            try:
                colora = coloR()
                robloxID, profile, image, username, friends, followers, following, premium, facebook, twitter, twitch, youtube, rolimon = info(RobloxID2)
                embed=discord.Embed(title="D2R Bot", description="**Found Roblox Account (ROVER)**", color=colora)
                embed.set_thumbnail(url=image)
                embed.add_field(name=f"Roblox Account Of : {ID}\n", value=f"```Username : {username}\nRoblox ID : {robloxID}\nFriends : {friends}\nFollowers : {followers}\nFollowing : {following}\nPremium : {premium}```", inline=False)
                embed.add_field(name=f"Links\n", value=f"Roblox Profile : **{profile}**\n\nRolimon : **{rolimon}**\n\nFacebook : **{facebook}**\n\nTwitter : **{twitter}**\n\nTwitch : **{twitch}**\n\nYoutube : **{youtube}**", inline=False)
                await channel.send(embed=embed)
            except:await channel.send(f"{ID} Doesnt have any Roblox Account Linked to ROVER")
D2R.run(token)