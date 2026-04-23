import os, json, subprocess
from datetime import datetime

def log_data(node_path, entry_name):
    # Kurema folder yigenga bidasubirwaho
    path = f"departments/{node_path}"
    os.makedirs(path, exist_ok=True)
    file_path = f"{path}/sovereign_records.json"
    
    records = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try: records = json.load(f)
            except: records = []
            
    records.append({"id": len(records)+1, "time": str(datetime.now()), "entry": entry_name})
    with open(file_path, 'w') as f:
        json.dump(records, f, indent=4)
    print(f"\n[DONE] Saved to {node_path}")

def main():
    while True:
        os.system('clear')
        print('==================================================')
        print('    BYV GLOBAL AI | CEO: BARTHÉLEMY')
        print('    STATUS: LIVE | INDEPENDENT NODES ACTIVE')
        print('==================================================')
        print('1. AGRI (Agri_Node)      2. LIVE (Livestock_Node)')
        print('3. FINANCE (Finance_Node) 4. HR (HR_Node)')
        print('5. SALES (Sales_Node)    6. ART (Art_Node)')
        print('7. MEDIA (Reports_Node)  9. GITHUB SYNC')
        print('0. EXIT')
        
        ch = input('\nCEO, Select Node: ')
        
        nodes = {
            '1': "Agriculture_and_Livestock/Agri_Node",
            '2': "Agriculture_and_Livestock/Livestock_Node",
            '3': "Finance_and_AI_HR/Finance_Node",
            '4': "Finance_and_AI_HR/HR_Node",
            '5': "Commerce_and_Sales/Sales_Node",
            '6': "Creative_and_Art/Art_Node",
            '7': "Media_and_Reports/Reports_Node"
        }
        
        if ch in nodes:
            val = input(f"Andika Data ya {ch}: ")
            log_data(nodes[ch], val)
            input("\nPress Enter to continue...")
        elif ch == '9':
            os.system('git add . && git commit -m "SYNC" && git push -f origin main')
            input("\nSynced to Cloud. Press Enter...")
        elif ch == '0': break

if __name__ == '__main__': main()
