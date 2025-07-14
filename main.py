from reddit_scraper import fetch_user_data
from persona_generator import generate_persona

def main():
    usernames = ["kojied", "Hungry-Move-6603"]
    for username in usernames:
        print(f"Processing {username}...")
        posts, comments = fetch_user_data(username)
        persona = generate_persona(username, posts, comments)
        with open(f"{username.lower().replace('-', '_')}_persona.txt", "w", encoding="utf-8") as f:
            f.write(persona)
        print(f"Finished writing persona for {username}")

if __name__ == "__main__":
    main()