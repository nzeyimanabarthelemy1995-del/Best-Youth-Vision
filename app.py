import os
import json
from datetime import datetime

def main():
    while True:
        os.system('clear')
        print("================================================")
        print("    BYV GLOBAL AI | CEO: BARTHÉLEMY")
        print("    STABILITY MODE: SECURE & PERMANENT")
        print("================================================")
        print("1. SaaS (Software)       2. AI HR Management")
        print("3. Creative & Art        4. Agriculture")
        print("5. Finance               6. Logistics")
        print("7. E-Commerce            8. Healthcare Tech")
        print("9. Education             10. Telecom & IT")
        print("11. Security             12. GITHUB SYNC (CLEAN)")
        print("0. EXIT")
        print("------------------------------------------------")
        
        choice = input("\nCEO, Hitamo Ishami ryo kwubaka: ")
        if choice == "0": break
        
        nodes = {
            "1":"SaaS", "2":"AI_HR", "3":"Creative_Art", "4":"Agri",
            "5":"Finance", "6":"Logistics", "7":"Commerce", "8":"Health",
            "9":"Education", "10":"Telecom", "11":"Security"
        }
        
        if choice in nodes:
            name = nodes[choice]
            data = input(f"\nWinjiye muri {name}. Andika inzego nshya: ")
            
            # Kubika mu buryo budashobora gufudika andi makuru
            filename = f"{name}_Database.json"
            record = {"timestamp": str(datetime.now()), "content": data}
            
            with open(filename, "a") as f:
                f.write(json.dumps(record) + "\n")
            
            print(f"\n✅ Inzego za {name} zinjijwe neza muri {filename}!")
            input("Kanda Enter usubire kuri Menu...")
            
        elif choice == "12":
            print("\n🚀 Irimo guhuza na GitHub (Secure Sync)...")
            os.system("git add . && git commit -m 'Structure Rebuilt: Zero-Error' && git push origin main")
            input("\nSync Done! Data ubu ifite umutekano muri Cloud. Enter...")

if __name__ == "__main__":
    main()
