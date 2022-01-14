# Functions with Outputs

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title
    case version of the name."""
    if f_name == "" or l_name == "":
        return "Invalid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("First name: "), input("Last name: ")))
