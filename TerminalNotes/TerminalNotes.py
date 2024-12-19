import json
import argparse

# ----------------------------------------
# read json-file and return content
# ----------------------------------------
def read_json():
    try:
        with open("data_TNotes.json", "r") as f:
            data = json.load(f)
        return data
    except:
        data = {}
        with open("data_TNotes.json", "w") as f:
            json.dump(data, f, indent=4)
        read_json()

# ----------------------------------------
# add note to json
# ----------------------------------------
def add_note(title, content):
    try:
        with open("data_TNotes.json", 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data={}
    if title in data:
        uSure = input(f"{title} already exists. Do you want to overwrite \"{title}\" ? (Y/N): ")
        if uSure:
            if uSure.lower() == "y":
                data[title] = content
                with open("data_TNotes.json", 'w') as file:
                    json.dump(data, file, indent=4)
                return True
            else: return

# ----------------------------------------
# delete note
# ----------------------------------------
def delete_note(title):
    data = read_json()
    if title in data:
        uSure = input(f"Do you want to delete \"{title}\" ? (Y/N): ")
        if uSure:
            if uSure.lower() == "n":
                return
            elif uSure.lower() == "y":
                del data[title]
                print("\n>> Note '" + title + "' successfully deleted")
                with open("data_TNotes.json", 'w') as file:
                    json.dump(data, file, indent=4)
                    return
    else:
        print("\n>> NO TITLE FOUND" )
                
# ----------------------------------------
# show note
# ----------------------------------------
def show_note(title):
    data = read_json()
    if title in data:
        with open("data_TNotes.json", 'r') as file:
            obj = json.load(file)
            title_len = len(title)
            return f"\nNote {title}:\n"+ "‾"*(title_len + 6) + f"\n{obj[title]}\n\n>> End"
    else:
        return
        
# ----------------------------------------
# main funktion
# ----------------------------------------
def main():
    parser = argparse.ArgumentParser(prog="TerminalNotes")
    parser.add_argument("-n", "--new", action="store_true", help="add/create a note")
    parser.add_argument("-d", "--delete", action="store_true", help="delet a note")
    parser.add_argument("-p", "--print", action="store_true", help="shows all saved notes")
    parser.add_argument("-v", "--verbose", action="store_true", help="show more information")
    parser.add_argument("title", type=str, nargs='?', help="name of the note")
    parser.add_argument("content", type=str, nargs='?', help="content of the note")
    args = parser.parse_args()

    if args.verbose:
        print(args)

    if args.new:
        if args.title == None or args.content == None:
            parser.error("the following arguments are required in comination with '-n'/'--new': title content")
        else:
            if add_note(args.title, args.content):
                print(f"Note {args.title} was created successfully")

    elif args.delete and args.title:
        delete_note(args.title)

    if args.print:
        data = read_json()
        for title in sorted(data.keys(), key=str.casefold):
            print(title)

    if not args.new and not args.delete and not args.print:
        note = show_note(args.title)
        if note == None:
            print("\n>> NO TITLE FOUND" )
        else:
            print(note)
        

if __name__ == "__main__":
    main()