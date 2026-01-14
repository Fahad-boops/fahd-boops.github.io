# --- PART 1: THE INPUT (Simulating a loaded CSV file) ---
raw_data = """Date,Store,Category,Amount
2024-01-01,Paycheck,Income,3000.00
2024-01-02,Rent,Housing,-1500.00
2024-01-05,Netflix,Sub,-15.00
2024-01-08,ShopRite,Food,-200.00
2024-01-10,Shell,Gas,-45.50
2024-01-12,Spotify,Sub,-12.00"""

# --- PART 2: THE ENGINE (Processing the File) ---
lines = raw_data.split("\n")
header = lines.pop(0)  # Remove the "Date,Store..." line

total_income = 0
total_spent = 0
expenses = []  # We store expenses here to graph them later

for line in lines:
    parts = line.split(",")  # Break line into pieces
    
    store = parts[1]
    amount = float(parts[3]) # Convert text to number
    
    # Logic: Separate Income vs Expense
    if amount > 0:
        total_income = total_income + amount
    else:
        total_spent = total_spent + amount
        # Save this transaction to our list so we can graph it below
        expenses.append({"store": store, "amt": amount})

# --- PART 3: THE DASHBOARD (The Visual Output) ---
remaining = total_income + total_spent

print("\n========================================")
print("       FINANCIAL DASHBOARD v1.0        ")
print("========================================")
print(f" TOTAL INCOME:   ${total_income:,.2f}")
print(f" TOTAL SPENT:    ${total_spent:,.2f}")
print(f" REMAINING CASH: ${remaining:,.2f}")
print("========================================\n")

print("--- EXPENSE BREAKDOWN (VISUAL) ---")
for x in expenses:
    # 1. Convert negative amount to positive for the chart
    cost = abs(x['amt'])
    
    # 2. Draw 1 bar for every $50 spent
    bar_count = int(cost / 50)
    graph = "[]" * bar_count
    
    # 3. Print the row
    if bar_count == 0: 
        graph = "|" # Show a tiny line for small purchases
        
    print(f"{x['store']:10} {graph} (${x['amt']})")