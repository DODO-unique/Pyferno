import argparse

# we created a parse manager
parseManager = argparse.ArgumentParser(description="A simple greeter")

# This parse manager gets the first argument here, this is compulsory
parseManager.add_argument("--name", "-n", help="The name to be displayed", default="Victor")

# Extra:

parseManager.add_argument("--mood", "-m", help="The tone of greeting")

# Now, we parse command line into 'args'
args = parseManager.parse_args()


if args.mood == 'happy':
    print(f"Hello, {args.name}! Teehee~")
elif args.mood == 'sad':
    print(f"Hey, {args.name}...")
elif args.mood == 'curious':
    print(f"Whassup, {args.name}?")
elif args.mood == 'horny':
    print(f"Wanna see heaven with me?")
else:
    print(f"Hello, {args.name}!")
