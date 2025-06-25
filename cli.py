import argparse
from lru import LRUCache

# Ask user for capacity at runtime
while True:
    try:
        cap = int(input("Enter cache capacity: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

cache = LRUCache(capacity=cap)
print(f"Interactive LRU Cache (capacity={cap}). Type commands like:")
print("put 1 100")
print("get 1")
print("cache")
print("exit")

while True:
    try:
        cmd = input(">> ").strip().split()
        if not cmd:
            continue
        if cmd[0] == "exit":
            break
        elif cmd[0] == "put" and len(cmd) == 3:
            cache.put(int(cmd[1]), int(cmd[2]))
            print(f"Put key={cmd[1]}, value={cmd[2]}")
        elif cmd[0] == "get" and len(cmd) == 2:
            value = cache.get(int(cmd[1]))
            print(f"Value = {value}")
        elif cmd[0] == "cache":
            node = cache.head.next
            contents = []
            while node != cache.tail:
                contents.append((node.key, node.value))
                node = node.next
            print("Current Cache:", contents)
        else:
            print("Unknown command or wrong arguments.")
    except Exception as e:
        print(f"Error: {e}")

def handle_put(args):
    key = int(args.key)
    value = int(args.value)
    cache.put(key, value)
    print(f"Put key={key}, value={value}")

def handle_get(args):
    key = int(args.key)
    value = cache.get(key)
    print(f"Value = {value}")

def handle_show(args):
    node = cache.head.next
    contents = []
    while node != cache.tail:
        contents.append((node.key, node.value))
        node = node.next
    print("Current Cache:", contents)

def main():
    parser = argparse.ArgumentParser(description="LRU Cache CLI")
    subparsers = parser.add_subparsers(title="Commands")

    # PUT command
    put_parser = subparsers.add_parser("put", help="Put key and value into cache")
    put_parser.add_argument("key")
    put_parser.add_argument("value")
    put_parser.set_defaults(func=handle_put)

    # GET command
    get_parser = subparsers.add_parser("get", help="Get value by key from cache")
    get_parser.add_argument("key")
    get_parser.set_defaults(func=handle_get)

    # SHOW command
    show_parser = subparsers.add_parser("cache", help="Show current cache contents")
    show_parser.set_defaults(func=handle_show)

    # Parse and execute
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
