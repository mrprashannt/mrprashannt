import telebot
import instaloader
import re


# hack4youbot api 6108393549:AAG6_kSjk0pSk2LIe5jGQ5JueqIyZA59elA
bot = telebot.TeleBot('6243958470:AAHheYhPTdOJrtt_FOK3ZfVDhNPi9dOJkxI')
#swatibot api 6243958470:AAHheYhPTdOJrtt_FOK3ZfVDhNPi9dOJkxI
# Initialize the Instaloader
loader = instaloader.Instaloader()


# Define a command handler for the '/start' command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, """ Hi, my name is Swatibot. I am a large language model from Prashant , trained on a massive dataset of text and code. I can generate text, translate languages, write different kinds of creative content, and answer your questions in an informative way. I am still under development, but I have learned to perform many kinds of tasks, including");
   I will try my best to follow your instructions and complete your requests thoughtfully.");
   I will use my knowledge to answer your questions in a comprehensive and informative way, even if they are open ended, challenging, or strange.");
   I will generate different creative text formats of text content, like poems, code, scripts, musical pieces, email, letters, etc. I will try my best to fulfill all your requirements.");
   Please instruct me what you want me to do today.""")
    bot.send_message(
        message.chat.id, """🙏 Please Enter only searching instagram userid""")

# Define a message handler for text messages
@bot.message_handler(func=lambda message: True)
def download_profile(message):
    username = message.text.strip()

    try:
        
        profile = instaloader.Profile.from_username(loader.context, username)
        loader.login("swati7095_bot", "Swati@9598")
        bot.reply_to(message, f"Downloading profile: {username}")
        loader.download_profile(profile, profile_pic_only=True)
        bot.reply_to(message, f"Profile downloaded successfully for: {username}")
        wealth = instaloader.Profile.from_username(profile.context, "wealth")
        emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)        
        search_results = instaloader.TopSearchResults(profile.context, 'music')        
        profile_pic_url = profile.profile_pic_url
        pk = profile.userid
        username = profile.username
        fullname = profile.full_name
        bio = profile.biography
        follower = profile.followers
        following = profile.followees
        media = profile.mediacount
        private = profile.is_private
        verifed= profile.is_verified
        bot.send_photo(message.chat.id, f"Profile pic: {profile_pic_url}")
        bot.send_message(message.chat.id, f"ID: {pk}")
        bot.send_message(message.chat.id, f"Username: {username}")
        bot.send_message(message.chat.id, f"Full Name: {fullname}")
        bot.send_message(message.chat.id, f"Bio: {bio}")
        bot.send_message(message.chat.id, f"Followers: {follower}")
        bot.send_message(message.chat.id, f"Following: {following}")
        bot.send_message(message.chat.id, f"Posts: {media}")
        bot.send_message(message.chat.id, f"Private: {private}")
        bot.send_message(message.chat.id, f"Verified: {verifed}")
        bot.send_message(message.chat.id, f"Email: {emails}")
        bot.send_message(message.chat.id, f"search_results :{search_results}")
        bot.send_message(message.chat.id, f"weathe :{wealth}")
        bot.send_message(message.chat.id, f"instagram :https://www.instagram.com/spdf7095/")
    except Exception as e: 
        bot.send_message(message.chat.id, e)
    
        
        

# Start the bot
bot.polling()
