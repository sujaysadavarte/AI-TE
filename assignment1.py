"""A1: Simple Reflex Agent for the Vacuum Cleaner World."""
 
 
def simple_reflex_agent(location, status):
    """Condition-action rules based only on the current percept."""
    if status == "Dirty":
        return "SUCK"
    elif location == "A":
        return "RIGHT"
    else:
        return "LEFT"
 
 
def run(environment, location, steps=6):
    environment = dict(environment)
    cleans = 0
    moves = 0
    for step in range(1, steps + 1):
        status = environment[location]
        action = simple_reflex_agent(location, status)
        print("Step:", step, "| Location:", location,
              "| Status:", status, "| Action:", action)
        if action == "SUCK":
            environment[location] = "Clean"
            cleans += 1
        elif action == "RIGHT":
            location = "B"
            moves += 1
        else:
            location = "A"
            moves += 1
    print("Final Environment:", environment)
    print("Cleaning actions:", cleans, "| Movement actions:", moves)
    print()
 
 
if __name__ == "__main__":
    print("=== Test 1: A = Dirty, B = Dirty, start at A ===")
    run({"A": "Dirty", "B": "Dirty"}, "A")
    print("=== Test 2: A = Clean, B = Dirty, start at A ===")
    run({"A": "Clean", "B": "Dirty"}, "A")
    print("=== Test 3: A = Clean, B = Clean, start at B ===")
    run({"A": "Clean", "B": "Clean"}, "B")

 