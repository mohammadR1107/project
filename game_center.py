import random
import time
import os
os.system('cls')
def main():
    while True:
        print("*" * 40)
        print("Welcome to our Game Center!\n"
              "We know finding the right games for your PC can be tricky\n"
              ", so we’ve written this smart tool to help you choose easier and faster. Enjoy gaming!\n")
        print("*" * 40)
        time.sleep(10)
        os.system('cls')
        print("\n🖱️ Select Your Laptop Level:")

        level = get_level()
        game1 = generate_game(level)
        game2 = generate_game(level)
        game3 = generate_game(level)
        time.sleep(1)
        print("\n✨ Recommended Games for You:")
        print("-" * 40)
        print(f"{game1}\n{game2}\n{game3}")

        print("-" * 40)
        command = input("\nDo you want to do it again? (y/n): ")
        if command == "y" or command == "yes":
            continue
        else:
            print("*" * 40)
            print("Thank you for using our tool. Happy gaming!")
            break

def get_level():
    while True:
        try:
            level = print("""
                --------------------------------------------------
                1. Entry-Level:\n
                * CPU: Intel Core i3 / AMD Ryzen 3\n
                * Graphics: Intel UHD / Radeon Vega 3\n
                * RAM: 4-8 GB\n
                * Storage: 256GB SSD / 500GB HDD\n
                * Display: 1366x768 or 1920x1080\n
                * Battery: 4-6 hours\n""")
            time.sleep(10)
            print("""2. Mid-Range:\n
                * CPU: Intel i5 / AMD Ryzen 5\n
                * Graphics: GTX 1650 / RX 5600M\n
                * RAM: 8-16 GB\n
                * Storage: 512GB SSD / 1TB HDD\n
                * Display: 1920x1080\n
                * Battery: 6-8 hours\n""")
            time.sleep(10)
            print("""3. High-End:\n
                * CPU: Intel i7/i9 / AMD Ryzen 7/9\n
                * Graphics: RTX 3060, 3080 / RX 6800M\n
                * RAM: 16-32 GB\n
                * Storage: 1TB SSD or more\n
                * Display: 1080p or 4K\n
                * Battery: 8-12 hours\n
                Please enter your laptop level (1-3):
                """)
            time.sleep(10)
            os.system('cls')
            level = int(input("enter your laptap level💻:"))
            
            os.system('cls')
            if level not in [1, 2, 3]:
                print("Invalid input. Please select a valid level (1-3).")
                continue
            else:
                break
        except:
            continue
    return level
def generate_game(level):
    if level == 1:
        game = ["Fortnite (low settings)",
                "League of Legends",
                "Minecraft",
                "Stardew Valley",
                "Counter-Strike: Global Offensive",
                "Rocket League",
                "Among Us",
                "Dota 2",
                "Team Fortress 2",
                "Hearthstone",
                "Fall Guys",
                "Terraria",
                "Sims 4",
                "Apex Legends (low settings)",
                "Valorant",
                "Paladins",
                "World of Warcraft (low settings)",
                "Civilization VI",
                "Age of Empires II: Definitive Edition",
                "Guild Wars 2"]
        level = random.choice(game)
        return level
    elif level == 2:
        game = ["GTA",
                "Red Dead Redemption 2 (medium settings)",
                "The Witcher 3 (medium settings)",
                "Assassin’s Creed Odyssey",
                "Monster Hunter: World",
                "Shadow of the Tomb Raider"]
        level = random.choice(game)
        return level

    elif level == 3:
        game = ["Cyberpunk 2077 (high settings)",
                "Red Dead Redemption 2",
                "The Witcher 3 (ultra settings)",
                "Assassin’s Creed Valhalla",
                "Call of Duty: Modern Warfare II",
                "Battlefield 2042",
                "Far Cry 6",
                "Metro Exodus (ultra settings)",
                "Shadow of the Tomb Raider (high settings)",
                "Control",
                "Watch Dogs: Legion",
                "Horizon Zero Dawn",
                "Doom Eternal",
                "Resident Evil Village",
                "Spider-Man: Miles Morales",
                "Hitman 3",
                "Forza Horizon 5",
                "The Elder Scrolls V: Skyrim (modded)",
                "Call of Duty: Warzone 2.0",
                "Crysis Remastered"]
        level = random.choice(game)
        return level

if __name__=="__main__":
    main()


