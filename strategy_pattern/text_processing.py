def process_text(text, operation):
    if operation == "uppercase":
        return text.upper()
    elif operation == "lowercase":
        return text.lower()
    elif operation == "capitalize":
        return text.capitalize()
    else:
        return text

input_text = "This is an example text."
operation = "uppercase"

output_text = process_text(input_text, operation)
print(output_text)