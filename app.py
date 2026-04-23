import os
import json
from datetime import datetime

def main():
    while True:
        os.system('clear')
        print("================================================")
        print("    BYV GLOBAL AI | TREASURY: $456,199")
        print("    CEO: BARTHÉLEMY | PROFESSIONAL MODE")
        print("================================================")
        print("1. SaaS (Software)       2. AI HR Management")
        print("3. Creative & Art        4. Agriculture")
        print("5. Finance               6. Logistics")
        print("7. E-Commerce            8. Healthcare Tech")
        print("9. Education             10. Telecom & IT")
        print("11. Security             12. GITHUB SYNC (LIVE)")
        print("0. EXIT")
        print("------------------------------------------------")
        
        choice = input("\nCEO, Hitamo Ishami: ")
        if choice == "0": break
        
        nodes = {
            "1":"SaaS", "2":"AI_HR", "3":"Creative_Art", 
            "4":"Agriculture", "5":"Finance", "6":"Logistics",
            "7":"Commerce", "8":"Healthcare", "9":"Education",
            "10":"Telecom", "11":"Security"
        }
        
        if choice in nodes:
            name = nodes[choice]
            data = input(f"\nAndika raporo ya {name}: ")
            record = {"time": str(datetime.now()), "report": data}
            with open(f"{name}.json", "a") as f:
                f.write(json.dumps(record) + "\n")
            print(f"\n✅ {name} Data Saved Locally!")
            input("\nKanda Enter...")
        elif choice == "12":
            print("\n🚀 Irimo gusukura no kohereza kuri GitHub...")
            # Iki gice kigamije gusiba bya bindi bya kera no kuri GitHub
            os.system("git rm -r --cached . && git add . && git commit -m 'Force Clean Sync' && git push -f origin main")
            input("\nSync Yarangiye! Kanda Enter...")

if __name__ == "__main__":
    main()
